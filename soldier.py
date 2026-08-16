import consts

soldier_row = 0
soldier_col = 0

def get_legs_indexes():
    legs = []
    for c in range(consts.SOLDIER_W):
        legs.append([soldier_row + consts.SOLDIER_H - 1, soldier_col + c])
    return legs

def get_body_indexes():
    body = []
    for r in range(consts.SOLDIER_H - 1):
        for c in range(consts.SOLDIER_W):
            body.append([soldier_row + r, soldier_col + c])
    return body

def move_soldier(direction):
    global soldier_row, soldier_col
    if direction == "down" and soldier_row + consts.SOLDIER_H < consts.NUM_ROWS:
        soldier_row += 1
    if direction == "up" and soldier_row > 0:
        soldier_row -= 1
    if direction == "right" and soldier_col + consts.SOLDIER_W < consts.NUM_COLS:
        soldier_col += 1
    if direction == "left" and soldier_col > 0:
        soldier_col -= 1

def check_mine():
    legs = soldier.get_legs_indexes()
    for i in range(len(legs)):
        r = legs[i][0]
        c = legs[i][1]
        if s_m[r][c] == consts.SOLDIER and m[r][c] == consts.MINE:
            return True
    return False