def create_playing_table():
    playing_table = []
    for row in range(6):
        playing_table.append([0] * 8)

    return playing_table


def rules():
    return ('\nChoose the number of the column,\nin witch you want to make your move:\n\n'
            ' 1  2  3  4  5  6  7  8')


def player_to_make_move(player):
    return f"It's {player} player move!"


def is_table_full(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 0:
                return False

    return True


def is_move_valid(col, table):
    if col not in range(len(table[0])):
        return False

    for row in range(len(table)):
        if table[row][col] == 0:
            return True

    return False


def player_move(player, col, table):
    if is_move_valid(col, table):

        for row in range(len(table) - 1, -1, -1):
            if table[row][col] == 0:
                table[row][col] = player
                return row, col

    return False


def is_four_in_row(player, last_move, table):
    in_line = 0
    row = last_move[0]
    col = 0

    for i in range(len(table[0])):

        if table[row][col] == player:
            in_line += 1

            if in_line == 4:
                return True
        else:
            in_line = 0
        col += 1
    return False


def is_four_in_column(player, last_move, table):
    in_line = 0
    row = last_move[0]
    col = last_move[1]

    for i in range(4):
        if row >= len(table):
            return False

        if table[row][col] == player:
            in_line += 1

            if in_line == 4:
                return True
        else:
            in_line = 0
        row += 1
    return False


def is_four_in_right_diag(player, last_move, table):
    in_line = 0
    row = last_move[0]
    col = last_move[1]
    while row > 0 and col > 0:
        row -= 1
        col -= 1
    for i in range(row, len(table)):
        if row >= len(table) or col >= len(table[0]):
            return False
        if table[row][col] == player:
            in_line += 1
        else:
            in_line = 0

        if in_line == 4:
            return True
        row += 1
        col += 1
    return False


def is_four_in_left_diag(player, last_move, table):
    in_line = 0
    row = last_move[0]
    col = last_move[1]
    while row < len(table) - 1 and col > 0:
        row += 1
        col -= 1
    for i in range(row, -1, -1):
        if col >= len(table[0]):
            return False
        if table[i][col] == player:
            in_line += 1
        else:
            in_line = 0

        if in_line == 4:
            return True
        col += 1
    return False


def is_wining(player, last_move, table):
    if is_four_in_row(player, last_move, table):
        return True

    if is_four_in_column(player, last_move, table):
        return True

    if is_four_in_left_diag(player, last_move, table):
        return True

    if is_four_in_right_diag(player, last_move, table):
        return True

    return False
