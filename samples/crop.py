# This script crops a picture to get only the important parts out.

# Width 946 height 560 of the screen
# Goal is to remove all surroundings so we only have the
# game board, the next boxes (split into the 5 consequtive bricks coming up)
# and the hold box.
# should it once try to find the black area and then update its search?
from PIL import Image
import glob, os
import ImageChops


# Global variables
gamebox_w = 946;
gamebox_h = 560;
img_empty = Image.open("pics/screenshot6.png");
img_game  = Image.open("pics/screenshot9.png");
no_rows   = 20;
no_cols   = 10;
# Functions

# TODO: Identify the currently moving object
# TODO: Split the "current world" and the moving object
# TODO: Make a simple test to see that we can actually play with the keysim
# TODO: Make an A* implementation with a "minimal height and trapped squares"-heuristic and test
# TODO: How do we handle updates in the world based on how the world changes (time-steps downwards that is)
# TODO: Find a solution to "reasoning without certainty" for a more sophisticated AI.
# Possible TODO: merge all extract functions to a single more sophisticated function

# Compare two images
def equal_img(im1, im2):
    return ImageChops.difference(im1, im2).getbbox() is None

# Extract the game box from the screentshot, its a 946x560 image
def extract_game_box(img):

    imgw, imgh = img.size;
    left       = (imgw - gamebox_w)/2;
    right      = left + gamebox_w;
    upper      = 97                           # No good with hard coded values
    lower      = upper + gamebox_h;
    box        = [left, upper, right, lower];
    img        = img.crop(box);
    img.save("pics/game_box.png","png");
    return img;

# Extract the game board from the game box
def extract_game_board(img):
    left   = 83;
    right  = 263;
    upper  = 129;                             # Removing the top row that is only half.
    lower  = 489;
    box    = [left, upper, right, lower];
    img    = img.crop(box);
    img.save("pics/game_board.png","png");
    return img;

# Extract a single game cell from the game board
def get_game_cell_img(img):
    imgw, imgh  = img.size;
    rows        = 20;
    cols        = 10;
    left, upper = 0, 0;
    right       = imgw/10;
    lower       = imgh/20;
    box         = [left, upper, right, lower];
    img         = img.crop(box);
    img.save("pics/empty_cell.png","png");
    return img;

def extract_grey_cell(img):
    imgw, imgh  = img.size;
    rows_img    = get_rows(img);
    last_row    = rows_img[len(rows_img)-1];
    square_imgs = get_squares(last_row);
    square_imgs[5].save("pics/grey_cell.png", "png");

def get_game_row_img(img):
    imgw, imgh = img.size;
    left       = 0;
    upper      = 0;
    right      = imgw;
    lower      = imgh/20;
    box        = [left, upper, right, lower];
    img        = img.crop(box);
    img.save("pics/game_row.png", "png");
    return img;

def get_rows(img):
    imgw, imgh = img.size;
    left  = 0;
    right = imgw;
    imgs  = [];
    for i in range(20):
        lower = imgh/20 * (i+1);
        upper = imgh/20 * i;
        box   = [left, upper, right, lower];
        imgs.append(img.crop(box));
    return imgs;

# Input is a 10 column row, extract each square image
def get_squares(img):
    squares = [];
    imgw, imgh = img.size;
    for i in range(10):
        bw = imgw/10;
        box = [i*bw, 0, (i+1)*bw, imgh];
        squares.append(img.crop(box));

    return squares;
# The game world has 200 squares, we represent an empty square as 0 and a "filled" square as 1
def get_game_world(img):
    res = [];
    # Get blank row and blank cell from game board
    game_board = extract_game_board(extract_game_box(img_empty));
    empty_cell = get_game_cell_img(game_board);
    empty_row  = get_game_row_img(game_board);
    grey_cell  = Image.open("pics/grey_cell.png");
    # Now get the current game board
    current_board  = extract_game_board(extract_game_box(img));
    current_board.show();
    board_rows     = get_rows(current_board);
    board_rows.reverse();
    contains_block = [];
    row_counter = 0;
    for i in board_rows:
        if not equal_img(empty_row, i):
            squares = get_squares(i);
            row = [];
            for s in squares:
                if equal_img(empty_cell, s) or equal_img(grey_cell, s):
                    row.append(0);
                else:
                    row.append(1);
            contains_block.append(row);

        else:
            for i in range(no_rows - row_counter):
                contains_block.append([0]*10);
            break;
        row_counter = row_counter + 1;
    contains_block.reverse();
    return contains_block;
# Run main

img = extract_game_box(img_empty);
img = extract_game_board(img);
img_cell = get_game_cell_img(img);
img_row  = get_game_row_img(img);
blocks = get_game_world(img_game);
game_board = extract_game_board(extract_game_box(img_game));
extract_grey_cell(game_board);
for row in blocks:
    for elem in row:
        if elem == 1:
            print "x",
        else:
            print "_",
    print ""

