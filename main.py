import pygame
import game_field
import screen
import soldier

m = []
b_m = []
game_field.create_empty_board(m)
game_field.create_empty_bushes_board(b_m)

game_field.reserve_soldier_spot(m)
game_field.reserve_flag_spot(m)

game_field.place_bushes(b_m)
game_field.place_mines(m)

s = screen.init_screen()

run = True
is_grid_view = False
enter_press_time = 0

while run:
    current_time = pygame.time.get_ticks()

    if is_grid_view == True:

        if current_time - enter_press_time >= 1000:
            is_grid_view = False

    evs = pygame.event.get()
    for e in evs:
        if e.type == pygame.QUIT:
            run = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN and is_grid_view == False:
                is_grid_view = True
                enter_press_time = pygame.time.get_ticks()

            if is_grid_view == False:
                if e.key == pygame.K_DOWN:
                    soldier.move_soldier("down")
                if e.key == pygame.K_UP:
                    soldier.move_soldier("up")
                if e.key == pygame.K_RIGHT:
                    soldier.move_soldier("right")
                if e.key == pygame.K_LEFT:
                    soldier.move_soldier("left")

    screen.draw_board(s, m, b_m, soldier.soldier_row, soldier.soldier_col, is_grid_view)

pygame.quit()