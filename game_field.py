import random
import consts
import soldier
import pygame

def create_empty_board(board_matrix):
    for i in range(consts.NUM_ROWS):
        row = []
        for j in range(consts.NUM_COLS):
            row.append(consts.EMPTY)
        board_matrix.append(row)

def create_empty_bushes_board(bushes_matrix):
    for i in range(consts.NUM_ROWS):
        row = []
        for j in range(consts.NUM_COLS):
            row.append(consts.EMPTY)
        bushes_matrix.append(row)

def reserve_soldier_spot(board_matrix):
    for i in range(consts.SOLDIER_H):
        for j in range(consts.SOLDIER_W):
            board_matrix[i][j] = consts.SOLDIER

def reserve_flag_spot(board_matrix):
    start_r = consts.NUM_ROWS - consts.FLAG_H
    start_c = consts.NUM_COLS - consts.FLAG_W
    for i in range(start_r, consts.NUM_ROWS):
        for j in range(start_c, consts.NUM_COLS):
            board_matrix[i][j] = consts.FLAG

def place_bushes(bushes_matrix):
    bushes_count = 0
    while bushes_count < consts.BUSHES_AMOUNT:
        rand_row = random.randint(0, consts.NUM_ROWS - consts.BUSH_H)
        rand_col = random.randint(0, consts.NUM_COLS - consts.BUSH_W)

        is_free = True
        for i in range(consts.BUSH_H):
            for j in range(consts.BUSH_W):
                if bushes_matrix[rand_row + i][rand_col + j] != consts.EMPTY:
                    is_free = False

        if is_free == True:
            for i in range(consts.BUSH_H):
                for j in range(consts.BUSH_W):
                    bushes_matrix[rand_row + i][rand_col + j] = consts.BUSH
            bushes_count += 1

def place_mines(board_matrix):
    mines_count = 0
    while mines_count < consts.MINES_AMOUNT:
        rand_row = random.randint(0, consts.NUM_ROWS - consts.MINE_H)
        rand_col = random.randint(0, consts.NUM_COLS - consts.MINE_W)

        is_free = True
        for i in range(consts.MINE_H):
            for j in range(consts.MINE_W):
                if board_matrix[rand_row + i][rand_col + j] != consts.EMPTY:
                    is_free = False

        if is_free == True:
            for i in range(consts.MINE_H):
                for j in range(consts.MINE_W):
                    board_matrix[rand_row + i][rand_col + j] = consts.MINE
            mines_count += 1

def check_win(s):
    start_r = consts.NUM_ROWS - consts.FLAG_H
    start_c = consts.NUM_COLS - consts.FLAG_W

    if soldier.soldier_row + consts.SOLDIER_H - 1 >= start_r and soldier.soldier_col + consts.SOLDIER_W - 1 >= start_c:
        font = pygame.font.SysFont('arial', 60, True)
        win_text = font.render("You Win!", True, consts.TEXT_COLOR)
        s.blit(win_text, (380, 200))
        pygame.display.flip()

        pygame.event.pump()
        pygame.time.delay(3000)

        soldier.soldier_row = 0
        soldier.soldier_col = 0