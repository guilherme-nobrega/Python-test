import random
import time
import os
import itertools
def jogar():
    clear = lambda: os.system('cls')
    # -
    # APRESENTAÇÃO
    apresentação(3, 1, 4)
    # -
    m = 0
    clear()
    while m == 0:
        # TELA DE BOAS VINDAS
        print("***************************************")
        print("*     BEM VINDO AO JOGO DA VELHA!     *")
        print("***************************************\n")
        print("||||||||||||||   MENU    ||||||||||||||")
        print("\n  1 - INICIAR\n  2 - SAIR")
        try:
            menu = int(input("\nESCOLHA UMA OPÇÃO: "))
        except ValueError:
            print("\nEscolha um número de 1 a 2 !!!".upper())
            time.sleep(1)
            clear()
            continue
        if menu == 1:
            g = 0
            while g == 0:
                clear()
                global tabuleiro
                global velha
                global ganhou
                global perdeu
                global cont
                global ga
                global gb
                global tt
                global npc
                global risk
                global z
                global y
                global w
                global x
                global k
                global np1
                global np2
                global np3
                global np4
                global np5
                acj = []
                tt = 0
                ga = 0
                gb = 0
                npc = 0
                velha = False
                ganhou = False
                perdeu = False
                tabuleiro = [ [0 for i in range(3)] for j in range(3)]
                cont = 0
                try:
                    mark = int(input("\nESCOLHA 1 PARA 'X' E -1 PARA 'O':  "))
                    if mark != 1:
                        if mark != -1:
                            continue
                except ValueError:
                    print("\nEscolha entre 1 e -1 !!!".upper())
                    time.sleep(1)
                    clear()
                    continue
                clear()
                while perdeu == False and velha == False and ganhou == False:
                    print("\n")
                    exibe()
                    try:
                        linha = int(input("\nESCOLHA A LINHA(L) DE 0 A 2:  "))
                        if linha < 0 or linha > 2:
                            print("\nEscolha um número de 0 a 2 !!!".upper())
                            time.sleep(1)
                            clear()
                            continue
                    except ValueError:
                        print("\nEscolha um número de 0 a 2 !!!".upper())
                        time.sleep(1)
                        clear()
                        continue
                    try:
                        coluna = int(input("\nESCOLHA A COLUNA(C) DE 0 A 2:  "))
                        if coluna < 0 or coluna > 2:
                            print("\nEscolha um número de 0 a 2 !!!".upper())
                            time.sleep(1)
                            clear()
                            continue
                    except ValueError:
                        print("\nEscolha um número de 0 a 2 !!!".upper())
                        time.sleep(1)
                        clear()
                        continue
                    cont += 1
                    if cont == 1:
                        acj.append([linha,coluna])
                    else:
                        bcj = [linha,coluna] in acj
                        if bcj == True:
                            cont -= 1
                            print("\nNão é possível marcar o mesmo lugar duas vezes!!!".upper())
                            time.sleep(1)
                            clear()
                            continue
                        else:
                            acj.append([linha,coluna])
                    tabuleiro[linha][coluna] = mark
                    check(mark)
                    if ganhou != True:
                        npc_joga(mark)
                        check(mark)
                        clear()                   
                    # input("\n\n\nPress enter to exit ;)")
                if ganhou == True:
                    clear()
                    print("\nPARABÉNS VOCÊ GANHOU !!!\n\n")
                    exibe()
                elif perdeu == True:
                    clear()
                    print("\nVOCÊ PERDEU !\n\n")
                    exibe()
                elif velha == True:
                    clear()
                    print("\nDEU VELHA !\n\n")
                    exibe()
                t = 0
                while t == 0:
                    print("\nDESEJA JOGAR NOVAMENTE ?")
                    resp = int(input("SIM = 1  |||  NÃO = 0: "))
                    if resp == 1:
                        clear()
                        t = 1
                    elif resp == 0:
                        print("\nVOLTANDO AO MENU PRINCIPAL...")
                        time.sleep(1)
                        clear()
                        g = 1
                        t = 1
                    else:
                        print("ESCOLHA ENTRE SIM(1) E NÃO(0) !!!")

        elif menu == 2:
            print("\nVOLTANDO AO MENU DE JOGOS !")
            print("\nENCERRANDO...")
            m = 1
            time.sleep(1)
            clear()
        else:
            # EXCEÇÃO PARA CAPTAR ERROS
            print("\nEscolha um número de 1 a 2 !!!".upper())
            time.sleep(1)
            clear()


        
        

def exibe():
    print("C->  0   1   2\nL:")
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                if j == 0 and i == 0:
                    print(" 0  ___|", end='')
                elif j == 0 and i == 1:
                    print(" 1  ___|", end='')
                elif j == 1 and i < 2:
                    print("___|", end='')
                elif j == 2 and i < 2:
                    print("___", end='')
                elif j == 0 and i == 2:
                    print(" 2     |", end='')
                elif j == 1 and i == 2:
                    print("   |", end='')
                elif j == 2 and i == 2:
                    print("   ", end='')
            elif tabuleiro[i][j] == 1:
                if j == 0 and i == 0:
                    print(" 0  _X_|", end='')
                elif j == 0 and i == 1:
                    print(" 1  _X_|", end='')
                elif j == 1 and i < 2:
                    print("_X_|", end='')
                elif j == 2 and i < 2:
                    print("_X_", end='')
                elif j == 0 and i == 2:
                    print(" 2   X |", end='')
                elif j == 1 and i == 2:
                    print(" X |", end='')
                elif j == 2 and i == 2:
                    print(" X ", end='')
            elif tabuleiro[i][j] == -1:
                if j == 0 and i == 0:
                    print(" 0  _O_|", end='')
                elif j == 0 and i == 1:
                    print(" 1  _O_|", end='')
                elif j == 1 and i < 2:
                    print("_O_|", end='')
                elif j == 2 and i < 2:
                    print("_O_", end='')
                elif j == 0 and i == 2:
                    print(" 2   O |", end='')
                elif j == 1 and i == 2:
                    print(" O |", end='')
                elif j == 2 and i == 2:
                    print(" O ", end='')
        print("\n")

def check(mark):
    global ganhou
    global perdeu
    global velha
    vlinha = 0
    vcoluna = 0
    vdiag1 = 0
    vdiag2 = 0
    if mark == 1:
        CM = True
        DM = False
    else:
        CM = False
        DM = True
    for i in range(3):
        soma = tabuleiro[i][0]+tabuleiro[i][1]+tabuleiro[i][2]
        if soma == 3:
            ganhou = CM
            perdeu = DM
            vlinha = 0
            break
        elif soma == -3:
            perdeu = CM
            ganhou = DM
            vlinha = 0
            break
        else:
            vlinha = 1

    if ganhou == False:
        for i in range(3):
            soma = tabuleiro[0][i]+tabuleiro[1][i]+tabuleiro[2][i]
            if soma == 3:
                ganhou = CM
                perdeu = DM
                vcoluna = 0
                break
            elif soma == -3:
                perdeu = CM
                ganhou = DM
                vcoluna = 0
                break
            else:
                vcoluna = 1

    if ganhou == False:
        diagonal1 = tabuleiro[0][0]+tabuleiro[1][1]+tabuleiro[2][2]
        if diagonal1 == 3:
            ganhou = CM
            perdeu = DM
            vdiag1 = 0
        elif diagonal1 == -3:
            perdeu = CM
            ganhou = DM
            vdiag1 = 0
        else:
            vdiag1 = 1

    if ganhou == False:
        diagonal2 = tabuleiro[0][2]+tabuleiro[1][1]+tabuleiro[2][0]
        if diagonal2 == 3:
            ganhou = CM
            perdeu = DM
            vdiag2 = 0
        elif diagonal2 == -3:
            perdeu = CM
            ganhou = DM
            vdiag2 = 0
        else:
            vdiag2 = 1

    if ganhou == False:
        somavelha = vlinha+vcoluna+vdiag1+vdiag2
        if somavelha == 4 and cont > 3:
            velha = True
    return ganhou
    

def npc_joga(mark):
    global tt
    global ga
    global gb
    global npc
    global ab
    global ac
    if mark == 1:
        npc = -1
    else:
        npc = 1
    tt += 1
    if tt < 2:
        a = random.randint(0, 2)
        b = random.randint(0, 2)
        jogada = tabuleiro[a][b]
        while jogada == mark or jogada == npc:
            a = random.randint(0, 2)
            b = random.randint(0, 2)
            jogada = tabuleiro[a][b]
        tabuleiro[a][b] = npc
        ga = a
        gb = b
    elif tt > 1: 
        bater = check_npc(mark)
        if bater == 1:
            tabuleiro[np2][np3] = npc
            ga = np2
            gb = np3
        elif bater == 2:
            tabuleiro[np3][np2] = npc
            ga = np3
            gb = np2
        elif bater == 3:
            tabuleiro[np3][np3] = npc
            ga = np3
            gb = np3
        elif bater == 4:
            tabuleiro[np3][np5] = npc
            ga = np3
            gb = np5
        elif bater == 0:
            risco = check_player(mark)
            if risco == 0:
                if ga == 0:
                    if gb == 0:
                        # CHECK ABAIXO
                        if check_ab() == True:
                            if ab1 == False or ab2 == True:
                                tabuleiro[ga+1][gb] = npc
                                ga = ga + 1
                            elif ab1 == True:
                                tabuleiro[ga+2][gb] = npc
                                ga = ga + 2
                        # CHECK DIREITA
                        elif check_dir() == True:
                            if d1 == False or d2 == True:
                                tabuleiro[ga][gb+1] = npc
                                gb = gb + 1
                            elif d1 == True:
                                tabuleiro[ga][gb+2] = npc
                                gb = gb + 2
                        # CHECK DIAGONAL DIREITA BAIXO
                        elif check_diadirb == True:
                            if ddb1 == False or ddb2 == True:
                                tabuleiro[ga+1][gb+1]
                                ga = ga + 1
                                gb = gb + 1
                            elif ddb1 == True:
                                tabuleiro[ga+2][gb+2]
                                ga = ga + 2
                                gb = gb + 2
                    elif gb == 1:
                        # CHECK ABAIXO
                        if check_ab() == True:
                            if ab1 == False or ab2 == True:
                                tabuleiro[ga+1][gb] = npc
                                ga = ga + 1
                            elif ab1 == True:
                                tabuleiro[ga+2][gb] = npc
                                ga = ga + 2
                        # CHECK LADOS
                        elif check_lad() == True:
                            if lade == False or ladd == True:
                                tabuleiro[ga][gb-1] = npc
                                gb = gb - 1
                            elif lade == True:
                                tabuleiro[ga][gb+1] = npc
                                gb = gb + 1
                    elif gb == 2:
                        # CHECK ABAIXO
                        if check_ab() == True:
                            if ab1 == False or ab2 == True:
                                tabuleiro[ga+1][gb] = npc
                                ga = ga + 1
                            elif ab1 == True:
                                tabuleiro[ga+2][gb] = npc
                                ga = ga + 2
                        # CHECK DIAGONAL ESQUERDA BAIXO
                        elif check_diaesqb() == True:
                            if deb1 == False or deb2 == True:
                                tabuleiro[ga+1][gb-1] = npc
                                ga = ga + 1
                                gb = gb - 1
                            elif deb1 == True:
                                tabuleiro[ga+2][gb-2] = npc
                                ga = ga + 2
                                gb = gb - 2
                        # CHECK ESQUERDA
                        elif check_esq() == True:
                            if e1 == False or e2 == True:
                                tabuleiro[ga][gb-1] = npc
                                gb = gb - 1
                            elif e1 == True:
                                tabuleiro[ga][gb-2] = npc
                                gb = gb - 2
                elif ga == 1:
                    if gb == 0:
                        # CHECK ABAIXO E ACIMA 
                        if check_abac() == True:
                            if ab == False or ac == True:
                                tabuleiro[ga+1][gb] = npc
                                ga = ga + 1
                            elif ab == True:
                                tabuleiro[ga-1][gb] = npc
                                ga = ga - 1
                        # CHECK DIREITA 
                        elif check_dir() == True:
                            if d1 == False or d2 == True:
                                tabuleiro[ga][gb+1] = npc
                                gb = gb + 1
                            elif d1 == True:
                                tabuleiro[ga][gb+2] = npc
                                gb = gb + 2
                    elif gb == 1:
                        # CHECK ABAIXO E ACIMA 
                        if check_abac() == True:
                            if ab == False or ac == True:
                                tabuleiro[ga+1][gb] = npc
                                ga = ga + 1
                            elif ab == True:
                                tabuleiro[ga-1][gb] = npc
                                ga = ga - 1
                        # CHECK LADOS
                        elif check_lad() == True:
                            if lade == False or ladd == True:
                                tabuleiro[ga][gb-1] = npc
                                gb = gb - 1
                            elif lade == True:
                                tabuleiro[ga][gb+1] = npc
                                gb = gb + 1
                        # CHECK DIAGONAL CENTRAL DIREITA
                        elif check_diagxdir() == True:
                            if dxdb2 == False or dxdc1 == True:
                                tabuleiro[ga+1][gb+1] = npc
                                ga = ga + 1
                                gb = gb + 1
                            elif dxdb2 == True:
                                tabuleiro[ga-1][gb-1] = npc
                                ga = ga - 1
                                gb = gb - 1
                        # CHECK DIAGONAL CENTRAL ESQUERDA
                        elif check_diagxesq() == True:
                            if dxeb == False or dxec == True:
                                tabuleiro[ga+1][gb-1] = npc
                                ga = ga + 1
                                gb = gb - 1
                            elif dxeb == True:
                                tabuleiro[ga-1][gb+1] = npc
                                ga = ga - 1
                                gb = gb + 1
                    elif gb == 2:
                        # CHECK ABAIXO E ACIMA
                        if check_abac() == True:
                            if ab == False or ac == True:
                                tabuleiro[ga+1][gb] = npc
                                ga = ga + 1
                            elif ab == True:
                                tabuleiro[ga-1][gb] = npc
                                ga = ga - 1
                        # CHECK ESQUERDA 
                        elif check_esq() == True:
                            if e1 == False or e2 == True:
                                tabuleiro[ga][gb-1] = npc
                                gb = gb - 1
                            elif e1 == True:
                                tabuleiro[ga][gb-2] = npc
                                gb = gb - 2
                elif ga == 2:
                    if gb == 0:
                        # CHECK DIREITA 
                        if check_dir() == True:
                            if d1 == False or d2 == True:
                                tabuleiro[ga][gb+1] = npc
                                gb = gb + 1
                            elif d1 == True:
                                tabuleiro[ga][gb+2] = npc
                                gb = gb + 2
                        # CHECK ACIMA
                        elif check_ac() == True:
                            if ac1 == False or ac2 == True:
                                tabuleiro[ga-1][gb] = npc
                                ga = ga - 1
                            elif ac1 == True:
                                tabuleiro[ga-2][gb] = npc
                                ga = ga - 2
                        # CHECK DIAGONAL DIREITA CIMA
                        elif check_diagdirc() == True:
                            if ddc1 == False or ddc2 == True:
                                tabuleiro[ga-1][gb+1] = npc
                                ga = ga - 1
                                gb = gb + 1
                            elif ddc1 == True:
                                tabuleiro[ga-2][gb+2] = npc
                                ga = ga - 2
                                gb = gb + 2
                    elif gb == 1:
                        # CHECK LADOS
                        if check_lad() == True:
                            if lade == False or ladd == True:
                                tabuleiro[ga][gb-1] = npc
                                gb = gb - 1
                            elif lade == True:
                                tabuleiro[ga][gb+1] = npc
                                gb = gb + 1
                        # CHECK ACIMA
                        elif check_ac() == True:
                            if ac1 == False or ac2 == True:
                                tabuleiro[ga-1][gb] = npc
                                ga = ga - 1
                            elif ac1 == True:
                                tabuleiro[ga-2][gb] = npc
                                ga = ga - 2
                    elif gb == 2:
                        # CHECK ACIMA
                        if check_ac() == True:
                            if ac1 == False or ac2 == True:
                                tabuleiro[ga-1][gb] = npc
                                ga = ga - 1
                            elif ac1 == True:
                                tabuleiro[ga-2][gb] = npc
                                ga = ga - 2
                        # CHECK ESQUERDA 
                        elif check_esq() == True:
                            if e1 == False or e2 == True:
                                tabuleiro[ga][gb-1] = npc
                                gb = gb - 1
                            elif e1 == True:
                                tabuleiro[ga][gb-2] = npc
                                gb = gb - 2
                        # CHECK DIAGONAL ESQUERDA CIMA
                        elif check_diagesqc() == True:
                            if dec1 == False or dec2 == True:
                                tabuleiro[ga-1][gb-1] = npc
                                ga = ga - 1
                                gb = gb - 1
                            elif dec1 == True:
                                tabuleiro[ga-2][gb-2] = npc
                                ga = ga - 2
                                gb = gb - 2
            elif risco == 1:
                tabuleiro[y][w] = npc
                ga = y
                gb = w
            elif risco == 2:
                tabuleiro[w][y] = npc
                ga = w
                gb = y
            elif risco == 3:
                tabuleiro[w][w] = npc
                ga = w
                gb = w
            elif risco == 4:
                tabuleiro[w][k] = npc
                ga = w
                gb = k

    return ga, gb, tt

def check_ab():
    global ab1
    global ab2
    ab1 = False
    ab2 = False
    res = 0
    if tabuleiro[ga+1][gb] == 0 or tabuleiro[ga+1][gb] == npc:
        if tabuleiro[ga+1][gb] == npc:
            res += 1
            ab1 = True
        else:
            res += 1
    if tabuleiro[ga+2][gb] == 0 or tabuleiro[ga+2][gb] == npc:
        if tabuleiro[ga+2][gb] == npc:
            res += 1
            ab2 = True
        else:
            res += 1
    if res == 2:
        return True
    else:
        return False

def check_ac():
    global ac1
    global ac2
    ac1 = False
    ac2 = False
    res = 0
    if tabuleiro[ga-1][gb] == 0 or tabuleiro[ga-1][gb] == npc:
        if tabuleiro[ga-1][gb] == npc:
            res += 1
            ac1 = True
        else:
            res += 1
    if tabuleiro[ga-2][gb] == 0 or tabuleiro[ga-2][gb] == npc:
        if tabuleiro[ga-2][gb] == npc:
            res += 1
            ac2 = True
        else:
            res += 1
    if res == 2:
        return True
    else:
        return False

def check_abac():
    global ab
    global ac
    ab = False
    ac = False
    res = 0
    if tabuleiro[ga+1][gb] == 0 or tabuleiro[ga+1][gb] == npc:
        if tabuleiro[ga+1][gb] == npc:
            res += 1
            ab = True
        else:
            res += 1
    if tabuleiro[ga-1][gb] == 0 or tabuleiro[ga-1][gb] == npc:
        if tabuleiro[ga-1][gb] == npc:
            res += 1
            ac = True
        else:
            res += 1
    if res == 2:
        return True
    else:
        return False

def check_dir():
    global d1
    global d2
    d1 = False
    d2 = False
    res = 0
    if tabuleiro[ga][gb+1] == 0 or tabuleiro[ga][gb+1] == npc:
        if tabuleiro[ga][gb+1] == npc:
            res += 1
            d1 = True
        else:
            res += 1
    if tabuleiro[ga][gb+2] == 0 or tabuleiro[ga][gb+2] == npc:
        if tabuleiro[ga][gb+2] == npc:
            res += 1
            d2 = True
        else:
            res += 1
    if res == 2:
        return True
    else:
        return False

def check_esq():
    global e1
    global e2
    e1 = False
    e2 = False
    res = 0
    if tabuleiro[ga][gb-1] == 0 or tabuleiro[ga][gb-1] == npc:
        if tabuleiro[ga][gb-1] == npc:
            res += 1
            e1 = True
        else:
            res += 1
    if tabuleiro[ga][gb-2] == 0 or tabuleiro[ga][gb-2] == npc:
        if tabuleiro[ga][gb-2] == npc:
            res += 1
            e2 = True
        else:
            res += 1
    if res == 2:
        return True
    else:
        return False

def check_diadirb():
    global ddb1
    global ddb2
    ddb1 = False
    ddb2 = False
    res = 0
    if tabuleiro[ga+1][gb+1] == 0 or tabuleiro[ga+1][gb+1] == npc:
        if tabuleiro[ga+1][gb+1] == npc:
            res += 1
            ddb1 = True
        else:
            res += 1
    if tabuleiro[ga+2][gb+2] == 0 or tabuleiro[ga+2][gb+2] == npc:
        if tabuleiro[ga+2][gb+2] == npc:
            res += 1
            ddb2 = True
        else:
            res += 1
    if res == 2:
        return True
    else:
        return False

def check_diaesqb():
    global deb1
    global deb2
    deb1 = False
    deb2 = False
    res = 0
    if tabuleiro[ga+1][gb-1] == 0 or tabuleiro[ga+1][gb-1] == npc:
        if tabuleiro[ga+1][gb-1] == npc:
            res += 1
            deb1 = True
        else:
            res += 1
    if tabuleiro[ga+2][gb-2] == 0 or tabuleiro[ga+2][gb-2] == npc:
        if tabuleiro[ga+2][gb-2] == npc:
            res += 1
            deb2 = True
        else:
            res += 1
    if res == 2:
        return True
    else:
        return False

def check_diagxdir():
    global dxdc1
    global dxdb2
    dxdc1 = False
    dxdb2 = False
    res = 0
    if tabuleiro[ga-1][gb-1] == 0 or tabuleiro[ga-1][gb-1] == npc:
        if tabuleiro[ga-1][gb-1] == npc:
            res += 1
            dxdc1 = True
        else:
            res += 1
    if tabuleiro[ga+1][gb+1] == 0 or tabuleiro[ga+1][gb+1] == npc:
        if tabuleiro[ga+1][gb+1] == npc:
            res += 1
            dxdb2 = True
        else:
            res += 1
    if res == 2:
        return True
    else:
        return False

def check_diagxesq():
    global dxeb
    global dxec
    dxec = False
    dxeb = False
    res = 0
    if tabuleiro[ga-1][gb+1] == 0 or tabuleiro[ga-1][gb+1] == npc:
        if tabuleiro[ga-1][gb+1] == npc:
            res += 1
            dxec = True
        else: 
            res += 1
    if tabuleiro[ga+1][gb-1] == 0 or tabuleiro[ga+1][gb-1] == npc:
        if tabuleiro[ga+1][gb-1] == npc:
            res += 1
            dxeb = True
        else:
            res += 1
    if res == 2:
        return True
    else:
        return False

def check_diagdirc():
    global ddc1
    global ddc2
    ddc1 = False
    ddc2 = False
    res = 0
    if tabuleiro[ga-1][gb+1] == 0 or tabuleiro[ga-1][gb+1] == npc:
        if tabuleiro[ga-1][gb+1] == npc:
            res += 1
            ddc1 = True
        else:
            res += 1
    if tabuleiro[ga-2][gb+2] == 0 or tabuleiro[ga-2][gb+2] == npc:
        if tabuleiro[ga-2][gb+2] == npc:
            res += 1
            ddc2 = True
        else:
            res += 1
    if res == 2:
        return True
    else:
        return False

def check_diagesqc():
    global dec1
    global dec2
    dec1 = False
    dec2 = False
    res = 0
    if tabuleiro[ga-1][gb-1] == 0 or tabuleiro[ga-1][gb-1] == npc:
        if tabuleiro[ga-1][gb-1] == npc:
            res += 1
            dec1 = True
        else:
            res += 1
    if tabuleiro[ga-2][gb-2] == 0 or tabuleiro[ga-2][gb-2] == npc:
        if tabuleiro[ga-2][gb-2] == npc:
            res += 1
            dec2 = True
        else:
            res += 1
    if res == 2:
        return True
    else:
        return False

def check_lad():
    global lade
    global ladd
    lade = False
    ladd = False
    res = 0
    if tabuleiro[ga][gb-1] == 0 or tabuleiro[ga][gb-1] == npc:
        if tabuleiro[ga][gb-1] == npc:
            res += 1
            lade = True
        else:
            res += 1
    if tabuleiro[ga][gb+1] == 0 or tabuleiro[ga][gb+1] == npc:
        if tabuleiro[ga][gb+1] == npc:
            res += 1
            ladd = True
        else:
            res += 1
    if res == 2:
        return True
    else:
        return False


def apresentação(a, b, c):
    # a: NÚMERO DE VEZES QUE A MENSAGEM É EXIBIDA
    # b: TEMPO ENTRE UMA MENSAGEM E OUTRA EM SEGUNDOS
    # c: LINHAS PARA PULAR ENTRE UMA MENSAGEM E OUTRA
    bva = "***************************************"
    bvt = "*     BEM VINDO AO JOGO DA VELHA!     *"
    bvp = "\n"
    lbv = [bva, bvt, bva, bvp*c]
    # "\n\n\n\n"
    t = 1
    if a < 1:
        print(exit("ERRO! VALOR NÃO PODE SER MENOR QUE 1!"))
    else:
        while t <= a:
            for percorrel in range(0, len(lbv)):
                print(lbv[percorrel])
            t += 1
            time.sleep(b)
    time.sleep(1)
    
def check_player(mark):
    global z
    global y
    global w
    global x
    global k
    z = 0 #a 
    y = 0 #b
    w = 0 #c
    x = 0 #d
    k = 0 #e
    mk2 = 0
    if mark == 1:
        mk2 = 2
    else:
        mk2 = -2
    # d=1 - linha, 2 - coluna, 3 - diagonal dirbai, 4  - diagonal esqbai
    global risk
    risk = False
    for i in range(3):
        z = 0
        for j in range(3):
            z = z + tabuleiro[i][j]
        if z == mk2:
            risk = True
            y = i
            x = 1
            break

    # SE NÃO ACHOU NA LINHA PROCURAR NA COLUNA
    if risk == False:
        z = 0
        for i in range(3):
            z = 0
            for j in range(3):
                z = z + tabuleiro[j][i]
            if z == mk2:
                risk = True
                y = i
                x = 2
                break

    # SE NÃO ACHOU NA COLUNA PROCURAR NAS DIAGONAIS
    # DIAGONAL DIREITA P BAIXO
    if risk == False:
        z = 0
        for i in range(3):
            z = z + tabuleiro[i][i]
        if z == mk2:
            risk = True
            x = 3
        # tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2]

    # DIAGONAL ESQUERDA P BAIXO
    if risk == False:
        z = 0
        for i, j in zip(range(3), range(2, -1, -1)):
            z = z + tabuleiro[i][j]
        if z == mk2:
            risk = True
            x = 4
        
        # tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0]

    if risk == True:
        if x == 1:
            for i in range(3):
                if tabuleiro[y][i] == 0:
                    w = i
                    break
        elif x == 2:
            for i in range(3):
                if tabuleiro[i][y] == 0:
                    w = i
                    break
        elif x == 3:
            for i in range(3):
                if tabuleiro[i][i] == 0:
                    w = i
                    break
        elif x == 4:
            for i, j in zip(range(3), range(2, -1, -1)):
                if tabuleiro[i][j] == 0:
                    w = i
                    k = j
                    break
    return x

def check_npc(mark):
    global np1
    global np2
    global np3
    global np4
    global np5
    np1 = 0 #a 
    np2 = 0 #b
    np3 = 0 #c
    np4 = 0 #d
    np5 = 0 #e
    omk = 0
    if mark == 1:
        omk = -2
    else:
        omk = 2
    # d=1 - linha, 2 - coluna, 3 - diagonal dirbai, 4  - diagonal esqbai
    global rwin
    rwin = False
    for i in range(3):
        np1 = 0
        for j in range(3):
            np1 = np1 + tabuleiro[i][j]
        if np1 == omk:
            rwin = True
            np2 = i
            np4 = 1
            break

    # SE NÃO ACHOU NA LINHA PROCURAR NA COLUNA
    if rwin == False:
        np1 = 0
        for i in range(3):
            np1 = 0
            for j in range(3):
                np1 = np1 + tabuleiro[j][i]
            if np1 == omk:
                rwin = True
                np2 = i
                np4 = 2
                break

    # SE NÃO ACHOU NA COLUNA PROCURAR NAS DIAGONAIS
    # DIAGONAL DIREITA P BAIXO
    if rwin == False:
        np1 = 0
        for i in range(3):
            np1 = np1 + tabuleiro[i][i]
        if np1 == omk:
            rwin = True
            np4 = 3
        # tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2]

    # DIAGONAL ESQUERDA P BAIXO
    if rwin == False:
        np1 = 0
        for i, j in zip(range(3), range(2, -1, -1)):
            np1 = np1 + tabuleiro[i][j]
        if np1 == omk:
            rwin = True
            np4 = 4
        
        # tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0]

    if rwin == True:
        if np4 == 1:
            for i in range(3):
                if tabuleiro[np2][i] == 0:
                    np3 = i
                    break
        elif np4 == 2:
            for i in range(3):
                if tabuleiro[i][np2] == 0:
                    np3 = i
                    break
        elif np4 == 3:
            for i in range(3):
                if tabuleiro[i][i] == 0:
                    np3 = i
                    break
        elif np4 == 4:
            for i, j in zip(range(3), range(2, -1, -1)):
                if tabuleiro[i][j] == 0:
                    np3 = i
                    np5 = j
                    break
    return np4






if(__name__ == "__main__"):
    jogar()
