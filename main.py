import pygame
import game_field
import screen
import soldier
import consts


def check_mine():
    legs = soldier.get_legs_indexes()
    for i in range(len(legs)):
        r = legs[i][0]
        c = legs[i][1]
        if s_m[r][c] == consts.SOLDIER and m[r][c] == consts.MINE:
            return True
    return False



m = [] #המטריצה של הפצצות
b_m = [] # המטריצה של השיחים
s_m = [] #המטריצה של החייל

game_field.create_empty_board(m)
game_field.create_empty_bushes_board(b_m)
game_field.create_soldier_board(s_m)

game_field.reserve_soldier_spot(m)
game_field.reserve_flag_spot(m)

game_field.place_bushes(b_m)
game_field.place_mines(m)

game_field.update_soldier_board(s_m, soldier.soldier_row, soldier.soldier_col)

s = screen.init_screen()

run = True
is_grid_view = False
enter_press_time = 0

soldier_state = "alive"
explosion_time = 0

while run:
    current_time = pygame.time.get_ticks()

    if is_grid_view == True:
        if current_time - enter_press_time >= 1000:
            is_grid_view = False

    if soldier_state == "exploded":
        if current_time - explosion_time >= 1000:
            soldier_state = "injured"

    evs = pygame.event.get()
    for e in evs:
        if e.type == pygame.QUIT:
            run = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN and is_grid_view == False:
                is_grid_view = True
                enter_press_time = pygame.time.get_ticks()

            if is_grid_view == False and soldier_state == "alive":
                if e.key == pygame.K_DOWN:
                    soldier.move_soldier("down")
                if e.key == pygame.K_UP:
                    soldier.move_soldier("up")
                if e.key == pygame.K_RIGHT:
                    soldier.move_soldier("right")
                if e.key == pygame.K_LEFT:
                    soldier.move_soldier("left")

                game_field.update_soldier_board(s_m, soldier.soldier_row, soldier.soldier_col)

                is_boom = check_mine()
                if is_boom == True:
                    soldier_state = "exploded"
                    explosion_time = pygame.time.get_ticks()

    screen.draw_board(s, m, b_m, soldier.soldier_row, soldier.soldier_col, is_grid_view, soldier_state)

pygame.quit()