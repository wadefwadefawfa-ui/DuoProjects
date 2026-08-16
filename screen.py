import pygame
import consts

g_img = None
m_img = None
f_img = None
s_img = None
e_img = None
i_img = None


def init_screen():
    global g_img
    global m_img
    global f_img
    global s_img
    global e_img
    global i_img

    pygame.init()
    s = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    pygame.display.set_caption("The Flag")

    t_g = pygame.image.load('grass.png')
    g_img = pygame.transform.scale(t_g, (consts.CELL_SIZE * consts.BUSH_W, consts.CELL_SIZE * consts.BUSH_H))

    t_m = pygame.image.load('mine.png')
    m_img = pygame.transform.scale(t_m, (consts.CELL_SIZE * consts.MINE_W, consts.CELL_SIZE * consts.MINE_H))

    t_f = pygame.image.load('flag.png')
    f_img = pygame.transform.scale(t_f, (consts.CELL_SIZE * consts.FLAG_W, consts.CELL_SIZE * consts.FLAG_H))

    t_s = pygame.image.load('soldier.png')
    s_img = pygame.transform.scale(t_s, (consts.CELL_SIZE * consts.SOLDIER_W, consts.CELL_SIZE * consts.SOLDIER_H))

    t_e = pygame.image.load('explotion.png')
    e_img = pygame.transform.scale(t_e, (consts.CELL_SIZE * consts.SOLDIER_W, consts.CELL_SIZE * consts.SOLDIER_H))

    t_i = pygame.image.load('injury.png')
    i_img = pygame.transform.scale(t_i, (consts.CELL_SIZE * consts.SOLDIER_W, consts.CELL_SIZE * consts.SOLDIER_H))

    return s


def draw_board(s, m, b_m, soldier_r, soldier_c, is_grid_view, state):
    if is_grid_view == True:
        s.fill(consts.bgdark)

        for i in range(consts.NUM_COLS + 1):
            x = i * consts.CELL_SIZE
            pygame.draw.line(s, consts.gridcolor, (x, 0), (x, consts.WINDOW_HEIGHT))

        for i in range(consts.NUM_ROWS + 1):
            y = i * consts.CELL_SIZE
            pygame.draw.line(s, consts.gridcolor, (0, y), (consts.WINDOW_WIDTH, y))

        for r in range(consts.NUM_ROWS):
            for c in range(consts.NUM_COLS):
                item = m[r][c]
                x = c * consts.CELL_SIZE
                y = r * consts.CELL_SIZE

                if item == consts.MINE and (c == 0 or m[r][c - 1] != consts.MINE) and (
                        r == 0 or m[r - 1][c] != consts.MINE):
                    s.blit(m_img, (x, y))

        s_x = soldier_c * consts.CELL_SIZE
        s_y = soldier_r * consts.CELL_SIZE

        if state == "alive":
            s.blit(s_img, (s_x, s_y))
        if state == "exploded":
            s.blit(e_img, (s_x, s_y))
        if state == "injured":
            s.blit(i_img, (s_x, s_y))

    else:
        s.fill(consts.bglight)

        for r in range(consts.NUM_ROWS):
            for c in range(consts.NUM_COLS):
                item = b_m[r][c]
                x = c * consts.CELL_SIZE
                y = r * consts.CELL_SIZE

                if item == consts.BUSH and (c == 0 or b_m[r][c - 1] != consts.BUSH) and (
                        r == 0 or b_m[r - 1][c] != consts.BUSH):
                    s.blit(g_img, (x, y))

        flag_r = consts.NUM_ROWS - consts.FLAG_H
        flag_c = consts.NUM_COLS - consts.FLAG_W

        for r in range(consts.NUM_ROWS):
            for c in range(consts.NUM_COLS):
                item = m[r][c]
                x = c * consts.CELL_SIZE
                y = r * consts.CELL_SIZE

                if item == consts.FLAG and r == flag_r and c == flag_c:
                    s.blit(f_img, (x, y))

        s_x = soldier_c * consts.CELL_SIZE
        s_y = soldier_r * consts.CELL_SIZE

        if state == "alive":
            s.blit(s_img, (s_x, s_y))
        if state == "exploded":
            s.blit(e_img, (s_x, s_y))
        if state == "injured":
            s.blit(i_img, (s_x, s_y))

        font = pygame.font.SysFont('arial', 20, True)
        t1 = font.render("Welcome to The Flag game.", True, consts.TEXT_COLOR)
        t2 = font.render("Have Fun!", True, consts.TEXT_COLOR)

        s.blit(t1, (70, 20))
        s.blit(t2, (70, 50))

    pygame.display.flip()