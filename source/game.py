from time import sleep
from random import randint

itens = ["Pedra", "Papel", "Tesoura"]

jogador = -1
computador = -1

player_score = 0
computer_score = 0

max_turn = 3
turn = 0

def process_result():
    global turn, jogador, computador, player_score, computer_score, max_turn

    computador = randint(0, 2)

    print('\nJO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)

    print('')
    print('-=' *11)
    print(f'Rodada: {turn + 1}')
    print(f'O computador jogou {itens[computador]}')
    print(f'O jogador jogou {itens[jogador]}')
    print('-=' *11)
    print('')

    if computador == 0:
        if jogador == 0:
            print('Ambos empataram a rodada !\n')
        elif jogador == 1:
            print('Jogador venceu a rodada !\n')
            turn = turn + 1
            player_score = player_score + 1
        elif jogador == 2:
            print('Computador venceu a rodada !\n')
            turn = turn + 1
            computer_score = computer_score + 1
    elif computador == 1:
        if jogador == 0:
            print('Computador venceu a rodada !\n')
            turn = turn + 1
            computer_score = computer_score + 1
        elif jogador == 1:
            print('Ambos emptaram a rodada !\n')
        elif jogador == 2:
            print('Jogador venceu a rodada !\n')
            turn = turn + 1
            player_score = player_score + 1
    elif computador == 2:
        if jogador == 0:
            print('Jogador venceu a rodada !\n')
            turn = turn + 1
            player_score = player_score + 1
        elif jogador == 1:
            print('Computador venceu a rodada !\n')
            turn = turn + 1
            computer_score = computer_score + 1
        elif jogador == 2:
            print('Ambos venceu a rodada !\n')

    print(f'Pontuação do Jogador: {player_score}')
    print(f'Pontuação do Computador: {computer_score}\n')

    if turn == max_turn:
        if(player_score > computer_score):
            print('O jogador venceu o jogo !')
        else:
            print('O computador venceu o jogo !')

        return True
    else:
        return False

def start():
    global jogador, itens

    while(True):
        print("Suas opções: \n")
        for index in range(len(itens)):
            print(f'[ {index} ] {itens[index]}')

        jogador = int(input("\nSua escolha: "))

        if jogador > len(itens):
            print("Opção invalida ! Escolha um valor valido.")
        else:
            stop = process_result()

            if stop:
                print("Fim de jogo !")
                break