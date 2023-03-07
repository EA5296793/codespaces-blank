import os
import random

# Configuración inicial del juego
width = 20
height = 10
player_x = width // 2
player_y = height // 2
score = 0
game_over = False

# Función para imprimir el tablero
def print_board():
    os.system('clear')
    for y in range(height):
        for x in range(width):
            if x == player_x and y == player_y:
                print('P', end='')
            elif random.random() < 0.1:
                print('.', end='')
            else:
                print(' ', end='')
        print()

# Función para mover al jugador
def move_player(dx, dy):
    global player_x, player_y, score
    new_x = player_x + dx
    new_y = player_y + dy
    if new_x >= 0 and new_x < width and new_y >= 0 and new_y < height:
        player_x = new_x
        player_y = new_y
        if random.random() < 0.1:
            score += 10

# Loop principal del juego
while not game_over:
    print_board()
    print('Score: {}'.format(score))
    move = input('Move: ')
    if move == 'a':
        move_player(-1, 0)
    elif move == 'd':
        move_player(1, 0)
    elif move == 'w':
        move_player(0, -1)
    elif move == 's':
        move_player(0, 1)
    elif move == 'q':
        game_over = True