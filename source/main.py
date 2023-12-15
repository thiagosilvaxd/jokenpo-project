from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
 [ 0 ]Pedra
 [ 1 ]Papel
 [ 2 ]Tesoura''')

jogador = int(input('Qual a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' *11)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('-=' *11)

if computador == 0:
    if jogador == 0:
        print('Ambos empataram')
    elif jogador == 1:
        print('Jogador Venceu')
    elif jogador == 2:
        print('Computador Venceu')    
if computador == 1:
    if jogador == 0:
        print('Computador Venceu')
    if jogador == 1:
        print('Ambos emptaram')
    if jogador == 2:
        print('Jogador Venceu')
if computador == 2:
    if jogador == 0:
        print('Computador Venceu')
    if jogador == 1:
        print('Jogador Venceu')
    if jogador == 2:
        print('Ambos empataram')
