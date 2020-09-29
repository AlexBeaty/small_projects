import pygame

# initialise pygame
pygame.init()

# screen properties
screen_size = 300
screen_rows = 3
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Tic Tac Toe")

white_col = (255, 255, 255)
black_col = (0,0,0)

# images
o_icon = pygame.transform.scale(pygame.image.load("images/o.png"), (90, 90))
x_icon = pygame.transform.scale(pygame.image.load("images/x.png"), (90, 90))
font = pygame.font.Font('freesansbold.ttf', 42)

# game variables
grid = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]
turn = True # True == player x, False == player o


def draw_screen():
    '''draws background and the current grid to screen'''
    screen.fill(white_col)

    # draw background grid
    for i in range(screen_rows + 1):
        pygame.draw.line(screen, black_col, (i*100, 0), (i*100, screen_size), 3)
        pygame.draw.line(screen, black_col, (0, i*100), (screen_size, i*100), 3)

    # draw x and o to board
    gp = 5 # some margin space so image is centered in grid cell
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 1:
                screen.blit(x_icon, (i*100+gp,j*100+gp))
            elif grid[i][j] == 0:
                screen.blit(o_icon, (i*100+gp,j*100+gp))
    pygame.display.update()


def check_game():
    '''check whether either player has won, or the game is drawn'''
    # check if either player wins
    for i in range(2):
        # check cols
        check_cols = any([all([True if x == i else False for x in col]) for col in grid])
        # check rows, same as cols but grid is first transposed
        check_rows = any([all([True if x == i else False for x in row]) for row in [list(y) for y in zip(*grid)]])
        # check diags
        diag_1 = [grid[0][0], grid[1][1], grid[2][2]]
        diag_2 = [grid[0][2], grid[1][1], grid[2][0]]
        check_diags = any([all([True if x == i else False for x in diag_1]), all([True if x == i else False for x in diag_2])])
        if any([check_rows, check_cols, check_diags]):
            return(i)

    # check if game is drawn, e.g board is filled but no player wins
    return(2 if all([True if None not in i else False for i in grid]) else -1)


def user_click(mouse_pos, turn_loc):
    '''update grid based on user input. User clicks to add o or x'''
    global turn

    # convert mouse click location to cell in grid
    mouse_x, mouse_y = mouse_pos
    i, j = mouse_x // 100, mouse_y // 100

    # check grid cell is empty, update cell to which user clicked
    if grid[i][j] == None:
        grid[i][j] = 1 if turn_loc else 0
        turn = not turn


def end_game(message):
    '''displays the winner of the game on the screen'''
    global grid
    pygame.time.delay(500)
    screen.fill(white_col)
    message_text = font.render(message, 1, black_col)
    screen.blit(message_text, ((screen_size - message_text.get_width()) // 2, (screen_size - message_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(3000)

    # reset grid for rematch
    grid = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]


def main():
    '''main function, runs pygame loop'''
    while True:
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                user_click(pygame.mouse.get_pos(), turn)

        # draw screen
        draw_screen()
        # check game state
        game_state = check_game()
        # end message and reset game
        if game_state == -1:
            pass
        elif game_state == 0:
            end_game('Player: O wins')
        elif game_state == 1:
            end_game('Player: X wins')
        elif game_state == 2:
            end_game('Draw')


while True:
    if __name__ == "__main__":
        main()