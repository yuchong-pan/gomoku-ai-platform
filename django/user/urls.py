from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^create/', create_user),
    url(r'^confirm/', confirm_register),
    url(r'^authenticate/', auth_user),
]
