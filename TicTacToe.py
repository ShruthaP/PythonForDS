import pygame
import sys
from pygame.locals import *

# Initialize the game
pygame.init()

# Variables
screen_width = 300  # width of the window
screen_height = 300  # height of the window
line_width = 8  # grid
board = []  # list which holds the Xs and Os
click = False  # a variable to allow user clicks
player = 1  # Players: 1: Player 1 (X), -1: Player 2 (O)
winner = 0  # Winner of the game : 1: Player 1, 2: Player 2, 0: Tie
end_game = False  # Variable to decide whether to continue playing

# Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
grid = (0, 0, 0)

# Define the screen, caption & font
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Python for ML: TicTacToe")
font = pygame.font.SysFont(None, 35)


# Function to draw grid lines
def draw_grid():
    """
    Sets the background color and draws the grid lines.
    """
    screen.fill(white)
    for x_cord in range(1, 3):  # Two horizontal & two vertical grid lines
        # Horizontal grids
        pygame.draw.line(screen, grid, (0, x_cord * 100), (screen_width, x_cord * 100), line_width)
        # Vertical grids
        pygame.draw.line(screen, grid, (x_cord * 100, 0), (x_cord * 100, screen_height), line_width)


# Function to draw Xs and Os
def draw_XO():
    """
    Draws markers X or O based on players
    """
    x_pos = 0  # x co-ordinate for marking X
    for xo in board:
        y_pos = 0  # y co-ordinate for marking X
        for y in xo:
            # If the cell value is 1, then draw two cross lines to indicate X i.e. the cross
            if y == 1:
                # First cross line - bottom-to-top
                pygame.draw.line(screen, red, (x_pos * 100 + 25, y_pos * 100 + 25), (x_pos * 100+65, y_pos * 100 + 65), line_width)
                # Second cross line - top-to-bottom
                pygame.draw.line(screen, red, (x_pos * 100 + 25, y_pos * 100 + 65),(x_pos * 100 + 65, y_pos * 100 + 25), line_width)
            # If the cell value is -1, then draw a circle to indicate O i.e. the naught
            if y == -1:
                pygame.draw.circle(screen, green, (x_pos * 100 + 50, y_pos * 100 + 50), 25, line_width)
            y_pos += 1
        x_pos += 1


# Function to check the winner
def check_winner():
    """
    Checks the winner
    """
    global winner
    global end_game
    y_pos = 0
    for xo in board:
        # Horizontal check
        # If sum is 3 then Player 1 has Xs in the consecutive cells & is the winner
        if sum(xo) == 3:
            winner = 1
            end_game = True
        # If sum is -3 then Player 2 has Os in the consecutive cells & is the winner
        if sum(xo) == -3:
            winner = 2
            end_game = True

        # Vertical check
        if board[0][y_pos] + board[1][y_pos] + board[2][y_pos] == 3:
            winner = 1
            end_game = True
        if board[0][y_pos] + board[1][y_pos] + board[2][y_pos] == -3:
            winner = 2
            end_game = True

    # Diagonal wise check
    if board[0][0] + board[1][1] + board[2][2] == 3 or board[2][0] + board[1][1] + board[0][2] == 3:
        winner = 1
        end_game = True
    if board[0][0] + board[1][1] + board[2][2] == -3 or board[2][0] + board[1][1] + board[0][2] == -3:
        winner = 2
        end_game = True

    # Check if it is a tie
    if end_game == False:
        tie = True
        # Check if any of the cells doesn't contain Xs or Os
        # If any cell is 0 then game is still on and not a tie
        for row in board:
            for i in row:
                if i == 0:
                    tie = False
        # if it is a tie, then end game and set winner to 0
        if tie == True:
            end_game = True
            winner = 0


def print_winner(winner):
    """
    Prints the winner status
    """
    if winner == 0:
        text = "Game ended in tie"
    elif winner == 1:
        text = 'Winner is Player 1 (X)!'
    else:
        text = 'Winner is Player 2 (O)!'
    winner_img = font.render(text, True, blue)
    screen.fill(white)
    screen.blit(winner_img, (screen_width // 2 - 125, screen_height // 2 - 50))


# Main program
run = True  # Variable to decide when to quit the game

# Initialize the board to hold 0s
for x in range(3):
    row = [0] * 3
    board.append(row)


while run:
    draw_grid()  # Draw the grid
    draw_XO()  # Draw X or O on the board
    # Possible events
    for event in pygame.event.get():  # for every event
        if event.type == pygame.QUIT:  # If exit the game window
            run = False
        if end_game == 0:  # if the game is still ON
            if event.type == pygame.MOUSEBUTTONDOWN and click == False:
                click = True
            if event.type == pygame.MOUSEBUTTONUP and click == True:
                click = False
                cell_x, cell_y = pygame.mouse.get_pos()  # get the position of the cell
                if board[cell_x // 100][cell_y // 100] == 0:  # if the cell value is 0, allow the player to make a move
                    board[cell_x // 100][cell_y // 100] = player
                    player *= -1  # next player
                    check_winner()  # check the winner

    if end_game == True:  # Once the game has ended, print the winner
        print_winner(winner)

    pygame.display.update()

pygame.quit()


