import math

def get_distance(p0, p1):
    # calculate the distance of two points
    return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)

def pos_in_board(x, y):
    # calculate the positions in board of points in game
    return x * 30 + 25, y * 30 + 25

def pos_in_game(x, y):
    # calculate the positions in game of points in board
    return int((x - 25) / 30), int((y - 25) / 30)

def pos_to_draw(*args):
    # calculate the left, right, up, and down positions in board
    x, y = args
    return x - 11, y - 11, x + 11, y + 11

def click_in_board(x , y):
    # Check whether the cursor is in the canvas or not
    return 10 < x < 460 and 10 < y < 460
