import json
import random

from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

from .models import RegisterToken
from gomoku.settings import EMAIL_REGEX, TOKEN_ALPHABET, TOKEN_LEN

def is_valid_email(email):
    return EMAIL_REGEX.match(email)

def is_valid_password(password):
    if len(password) < 6:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    for i in password:
        has_upper |= i.isupper()
        has_lower |= i.islower()
        has_digit |= i.isdigit()
    return has_upper and has_lower and has_digit

def user_exists(email):
    try:
        u = User.objects.get(username=email)
    except User.DoesNotExist:
        return False
    return True

def token_exists(token):
    try:
        t = RegisterToken.objects.get(token=token)
    except RegisterToken.DoesNotExist:
        return False
    return True

def gen_random_token():
    result = ""
    token_alphabet_len = len(TOKEN_ALPHABET)
    for i in range(TOKEN_LEN):
        result += TOKEN_ALPHABET[random.randint(0, token_alphabet_len - 1)]
    return result

def create_register_token(email, password):
    token = gen_random_token()
    while token_exists(token):
        token = gen_random_token()
    RegisterToken.objects.create(token=token, email=email, password=password)
    return token

def send_confirm(email, token):
    send_mail(
        'Confirm Your Account',
        '',
        'me@y-pan.co',
        [email],
        fail_silently=True,
        html_message='<p>Click <a target="_blank" href="http://y-pan.co/api/user/confirm?token=%s">http://y-pan.co/api/user/confirm?token=%s</a> to confirm your account!</p>' % (token, token))

@require_http_methods(["POST"])
@csrf_exempt
def create_user(request):
    try:
        body = json.loads(request.body)
    except:
        response = JsonResponse({'message': 'invalid JSON'})
        response.status_code = 400
        return response

    try:
        email = body['email'].lower()
        password = body['password']
    except KeyError:
        response = JsonResponse({'message': 'invalid fields'})
        response.status_code = 400
        return response

    if not is_valid_email(email):
        response = JsonResponse({'message': 'invalid email address'})
        response.status_code = 400
        return response

    if not is_valid_password(password):
        response = JsonResponse({'message': 'invalid password'})
        response.status_code = 400
        return response

    if user_exists(email):
        response = JsonResponse({'message': 'user exists'})
        response.status_code = 409
        return response

    token = create_register_token(email, password)
    send_confirm(email, token);
    
    return JsonResponse({'message': 'confirmation sent'})
