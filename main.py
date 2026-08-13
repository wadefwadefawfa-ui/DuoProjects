import random

"""
2. קובץ game_field.py:
board_matrix - הרשימה הדו-מימדית שלנו ללוח
create_empty_board() - לולאה בתוך לולאה שממלאת את המטריצה במילה "empty"
place_flag() - לולאה שרושמת "flag" במשבצות של הפינה הימנית למטה
randomize_bushes() - לולאת while עד 20, מגרילה שורה ועמודה, בודקת שריק ומכניסה "bush"
randomize_mines() - לולאת while עד 20, מגרילה שורה, עמודה רק עד 47, בודקת ש-3 משבצות ברצף ריקות ושמה "mine"
"""
def create_empty_board(board_matrix):
    for i in range(25):
        row = []
        for j in range(50):
            row.append("empty")
        board_matrix.append(row)

def place_bushes(board_matrix):
    bushes_count = 0
    while bushes_count < 20:
        rand_row = random.randint(0, 24)
        rand_col = random.randint(0, 49)
        if board_matrix[rand_row][rand_col] == "empty":
            board_matrix[rand_row][rand_col] = "bush"
            bushes_count += 1

def place_mines(board_matrix):
    mines_count = 0
    while mines_count < 20:
        rand_row = random.randint(0, 24)
        rand_col = random.randint(0, 47)
        if board_matrix[rand_row][rand_col] == "empty" and board_matrix[rand_row][rand_col + 1] == "empty" and board_matrix[rand_row][rand_col + 2] == "empty":
            board_matrix[rand_row][rand_col] = "mine"
            board_matrix[rand_row][rand_col + 1] = "mine"
            board_matrix[rand_row][rand_col + 2] = "mine"
            mines_count += 1

board_matrix = []
create_empty_board(board_matrix)
place_bushes(board_matrix)
place_mines(board_matrix)