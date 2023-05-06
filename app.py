# PROJETO 4 - PYTONISTA AUTODIDATA - PEDRA PAPEL E TESOURA

from random import choice
import os


lista = ['papel','pedra','tesoura']

nome = input('Digite o nome do jogador: ')
    
while True:
    # Sortear a escolha do bot
    escolha_bot = choice(lista)
    escolha_jogador = input(nome + ' - ' + 'Escolha uma - ' + 'pedra|papel|tesoura: ')

    if escolha_jogador in lista:
        if escolha_jogador == escolha_bot :
            print('EMPATOU! - bot escolheu: ' + escolha_bot)

        elif escolha_jogador == 'pedra' and escolha_bot == 'tesoura':
            print('GANHOU! - bot escolheu: ' + escolha_bot)

        elif escolha_jogador == 'tesoura' and escolha_bot == 'papel':
            print('GANHOU! - bot escolheu: ' + escolha_bot)

        elif escolha_jogador == 'papel' and escolha_bot == 'pedra':
            print('GANHOU! - bot escolheu: ' + escolha_bot)

        else:
            print('PERDEU! - bot escolheu: ' + escolha_bot)
    
    elif escolha_jogador == 'sair':
        break

    else:
        print('Escolha inválida! Reiniciando o jogo')

os.system('cls') 

    





