from random import randint
from math import sqrt
game_width = 10
game_height = 10

key_x = randint(0, game_width)
key_y = randint(0, game_height)

player_x = 0
player_y = 0
player_found_key = False
steps = 0

distance_before_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)
# print(key_x, key_y)

while not player_found_key:
    steps += 1
    print()
    print('Możesz udać się w kierunkach określonych jako [W/A/S/D]: ')

    move = input('Dokąd idziesz? ')
    match move.lower():
        case 'w':
            player_y += 1
            if player_y > game_height:
                print('Auć!, uderzasz w ściane')
                player_y = game_height
        case 's':
            player_y -= 1
            if player_y < 0:
                print('Auć! uderzasz w ściane!')
                player_y = 0
        case 'a':
            player_x -= 1
            if player_x < 0:
                print('Auć! uderzasz w ściane')
                player_x = 0
        case 'd':
            player_x += 1
            if player_x > game_width:
                print('Auć! uderzasz w ściane!')
                player_x = game_width
        case 'q':
            quit('Koniec gry!')
        case '_':
            print('Nie wiem dokąd idziesz...')
            continue

    if player_x == key_x and player_y == key_y:
        print('Klucz jest Twój, możesz iść otworzyć skarb!')
        print(f'Wykonałeś/wykonałeś {steps} ruchów')

    distance_after_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

    # print('before', distance_before_move)
    # print('after', distance_after_move)

    if distance_before_move > distance_after_move:
        print('Cieplej!')
    else:
        print('Zimno!')

    distance_before_move = distance_after_move


    # print(player_x, player_y)
