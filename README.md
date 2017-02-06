# gomoku-ai-platform

An online platform for Gomoku AI competitions.

### Game Rules

Black plays first, and players alternate in placing a stone of their color on an empty intersection. The winner is the first player to get an unbroken row of five stones horizontally, vertically, or diagonally.

The three-and-three, four-and-four and overlines ban are applied to Black.

1. Three-and-Three
   
   The rule of three-and-three bans a move that simultaneously forms two open rows of three stones (rows not blocked by an opponent's stone at either end).
   
2. Four-and-Four
   
   The rule of four-and-four bans a move that simultaneously forms two rows of four stones (open or not).
   
3. Overlines
   
   Rows of six or more, called overlines, do not count.

### Functions to Be Implemented

Your task is to implement the following functions in Python:

1. Initialization
   
   ``` python
   def init(n, play_first)
   ```
   
   The platform calls this function at the very beginning of a game. No values are expected to be returned.
   
   The first argument `n` is an integer satisfying. Typically `n` equals `19`. which means that the size of the chessboard is `n*n`.
   
2. Next Step
   
   ``` python
   def next(pos_x, pos_y, sha1)
   ```
   
   The platform calls this function every time it is your turn to place a stone on the chessboard.
   
   The arguments `pos_x` and `pos_y` represent the x-coordinate and the y-coordinate of the stone the other party placed in his/her last turn. Both of the arguments are ranging from `0` to `n - 1` and it is guaranteed that the position `(pos_x, pos_y)` has not been occupied before.
   
   The argument `sha1` is a SHA1 hash value for the current situation of the chessboard (including the stone at `(pos_x, pos_y)`). A situation of the chessboard can be represents by an `n*n`-bit string, each character of which is either `0`, `b` or `w`. `0` represents the position has not been occupied, `b` represents the position has been occupied by Black (who plays first), and `w` represents the position has been occupied by White (who plays second). In Python, you can import the `hashlib` library and call `hashlib.sha1(string).hexdigest()` to obtain the SHA1 hash of a string.
   
   You are expected to return a two-element tuple `(x, y)`, which represents the position on the chessboard at which you are going to place a stone. If you hope to skip the turn, return a string `"SKIP"` instead. Please note the your choice should follow the game rules described above; otherwise, you lose the game immediately.
