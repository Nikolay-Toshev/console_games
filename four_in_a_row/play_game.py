from functions import *

table = create_playing_table()

print(rules())
for i in table:
    print(i)

players = {
    'player one': 1,
    'player two': 2,
}

player = players['player one']
while True:
    print(player_to_make_move(player))
    move = input()
    if not move.isdigit():
        print('Invalid move! try again')
        continue

#
    last_move = player_move(player, int(move) - 1, table)

    if not last_move:
        print('Invalid move! try again')
        continue

    print(rules())

    for i in table:
        print(i)

    if is_wining(player, last_move, table):
        print(f"Player {player} Won!")
        break
    if is_table_full(table):
        print("Draw!!!")
        break
    if player == players['player one']:
        player = players['player two']
    else:
        player = players['player one']

