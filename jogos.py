import time
import os
import forca
import adivinhacao
import velha
clear = lambda: os.system('cls')
# clear()                "
# MENU INICIAL
m = 0
while m == 0:
    print("***************************************")
    print("*     BEM VINDO AO MENU DE JOGOS!     *")
    print("***************************************\n")
    print("||||||||||||||   MENU    ||||||||||||||")
    print("\n  1 - ADIVINHAÇÃO\n  2 - FORCA\n  3 - JOGO DA VELHA\n  4 - SAIR")
    menu = int(input("\nESCOLHA UMA OPÇÃO: "))
    if menu == 1:
        print("\nINICIALIZANDO ADIVINHAÇÃO...")
        time.sleep(1)
        clear()
        print("LOADING....")
        time.sleep(1)
        clear()
        adivinhacao.jogar()

    elif menu == 2:
        print("\nINICIALIZANDO FORCA...")
        time.sleep(1)
        clear()
        print("LOADING....")
        time.sleep(1)
        clear()
        forca.jogar()

    elif menu == 4:
        print("\nENCERRANDO...")
        m = 1

    elif menu == 3:
        print("\nINICIALIZANDO JOGO DA VELHA...")
        time.sleep(1)
        clear()
        print("LOADING....")
        time.sleep(1)
        clear()
        velha.jogar()
    else:
        # EXCEÇÃO PARA CAPTAR ERROS
        print("Escolha um número de 1 a 4 !!!".upper())

time.sleep(1)
