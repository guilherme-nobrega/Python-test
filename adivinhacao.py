import random
import time
import os
def jogar():
    clear = lambda: os.system('cls')
    # clear()
    # APRESENTAÇÃO
    bva = "***************************************"
    bvt = "*  BEM VINDO AO JOGO DA ADIVINHAÇÃO!  *"
    lbv = [bva, bvt, bva, "\n\n\n\n"]
    t = 1
    while t <= 3:
        for percorrel in range(0, len(lbv)):
            print(lbv[percorrel])
        t += 1
        time.sleep(1)
    time.sleep(1)
    # VARIÁVEIS PARA DEFINIR DIFICULDADE DO JOGO
    dificuldade = ""
    nivel = 0
    # FERRAMENTAS PARA CRIAÇÃO DO RANKING DO JOGO
    ranking_f = [["Zé", 950], ["Maria", 900], ["Pedro", 850]]
    ranking_m = [["Gabriel", 951], ["Fernanda", 901], ["Bruna", 851]]
    ranking_d = [["Ana", 972], ["Vinícius", 962], ["Rebecca", 952]]
    ranking = []
    la = "\n***************************************"
    lt = "\n---------------------------------------"
    lt2 = "---------------------------------------"
    la1 = "  TOP 3 NÍVEL %s\n  1º: %s - %d PONTOS                   "
    la2 = "  2º: %s - %d PONTOS                   \n  3º: %s - %d PONTOS                   "
    # MENU INICIAL
    m = 0
    clear()
    while m == 0:
        print("***************************************")
        print("*  BEM VINDO AO JOGO DA ADIVINHAÇÃO!  *")
        print("***************************************\n")
        print("||||||||||||||   MENU    ||||||||||||||")
        print("\n  1 - RANKING\n  2 - INICIAR\n  3 - SAIR")
        menu = int(input("\nESCOLHA UMA OPÇÃO: "))
        if menu == 1:
            clear()
            # SISTEMA DE CONSULTA DE RANKING
            print("||||||||||||||  RANKING  ||||||||||||||")
            c = 0
            # ESCOLHA DO NÍVEL A SER APRESENTADO
            while c == 0:
                print("\nEscolha um nível de dificuldade :\n\n(1) FÁCIL  (2) MÉDIO  (3) DIFÍCIL  (4) MENU")
                nivel = int(input("\nNÍVEL: "))
                if nivel == 1:
                    ranking = ranking_f
                    dificuldade = "FÁCIL"
                    clear()
                elif nivel == 2:
                    ranking = ranking_m
                    dificuldade = "MÉDIO"
                    clear()
                elif nivel == 3:
                    ranking = ranking_d
                    dificuldade = "DIFÍCIL"
                    clear()
                elif nivel == 4:
                    clear()
                    c = 1
                    break
                else:
                    # EXCEÇÃO PARA CAPTAR ERROS
                    print("Escolha um número de 1 a 4 !!!".upper())
                # EXIBIÇÃO DO RANKING COM VARIÁVEIS CONTENDO A FORMATAÇÃO
                print("||||||||||||||  RANKING  ||||||||||||||")
                print(la, lt)
                print(la1 % (dificuldade, ranking[0][0], ranking[0][1]))
                print(la2 % (ranking[1][0], ranking[1][1], ranking[2][0], ranking[2][1]))
                print(lt2, la)
        elif menu == 2:
            g = 0
            # VARIÁVEIS PARA DEFINIR DIFICULDADE DO JOGO
            dificuldade = ""
            nivel = 0
            # RANKING
            ranking = []
            while g == 0:
                # LIMPA A TELA
                clear()
                # CRIAÇÃO DO NÚMERO SECRETO COM RANDINT
                numero_secreto = random.randint(1, 100)
                # CAPTAÇÃO NOME E CRIAÇÃO VARIÁVEIS DE TENTATIVAS E PONTUAÇÃO
                nome = input("\nDIGITE SEU NOME: ")
                tentativas = 0
                pontos = 1000
                cont_tentativas = 0
                l_chutes = []
                # ESCOLHA DA DIFICULDADE
                print("\nEscolha um nível de dificuldade %s:" % nome)
                print("(1) FÁCIL  (2) MÉDIO  (3) DIFÍCIL\n(1) 20x -- (2) 10x -- (3) 5x")
                a = 0
                while a == 0:
                    nivel = int(input("NÍVEL: "))
                    if nivel == 1:
                        tentativas = 20
                        a = 1
                        ranking = ranking_f
                        dificuldade = "FÁCIL"
                        x = 21
                    elif nivel == 2:
                        tentativas = 10
                        a = 1
                        ranking = ranking_m
                        dificuldade = "MÉDIO"
                        x = 11
                    elif nivel == 3:
                        tentativas = 5
                        a = 1
                        ranking = ranking_d
                        dificuldade = "DIFÍCIL"
                        x = 6
                    else:
                        # EXCEÇÃO PARA CAPTAR ERROS
                        print("Escolha um número de 1 a 3 !!!".upper())
                # EXIBIÇÃO DOS PONTOS INICIAIS
                clear()
                print("R: ", numero_secreto)
                print("INÍCIO - USE 0 PARA VOLTAR AO MENU PRINCIPAL")
                print("\nPONTOS: ", pontos)
                # FOR PARA OS CHUTES DO USUÁRIO
                for tentativas in range(tentativas, 0, -1):
                    print("\nVocê tem %d tentativas !" % tentativas)
                    chute = int(input("\nDigite o seu número: "))
                    print("\nVocê chutou:", chute)
                    if chute == 0:
                        print("\nSAINDO E VOLTANDO AO MENU PRINCIPAL...")
                        time.sleep(2)
                        g = 1
                        break
                    if chute < 1 or chute > 100:
                        # EXCEÇÃO PARA CAPTAR ERROS
                        print("Você deve escolher um número entre 1 e 100 !")
                        l_chutes.append(chute)
                        continue
                    if numero_secreto == chute:
                        print("\nVocê acertou !")
                        l_chutes.append(chute)
                        cont_tentativas += 1
                        time.sleep(2)
                        clear()
                        break
                    elif chute > numero_secreto:
                        print("\nVocê chutou um número maior que a resposta !")
                        l_chutes.append(chute)
                    else:
                        print("\nVocê chutou um número menor que a resposta !")
                        l_chutes.append(chute)
                    # CÁLCULO DOS PONTOS
                    pontos_perdidos = abs(numero_secreto - chute)
                    pontos -= pontos_perdidos
                    cont_tentativas = x - tentativas
                if chute == 0:
                    clear()
                    break
                # RESUMO DA PARTIDA
                print("|||||||||  RESUMO DA PARTIDA  |||||||||")
                print("\nRESPOSTA: %d" % numero_secreto)
                print("NOME: %s\nPONTUAÇÃO FINAL: %d\nTENTATIVAS O: %d" % (nome, pontos, cont_tentativas))
                print("TENTATIVAS N: %d\nCHUTES : %s" % (len(l_chutes), l_chutes))
                print("\nVERIFICANDO RANKING...")
                time.sleep(3)
                # VERIFICAÇÃO E ATUALIZAÇÃO DE NOVO TOP 3 E QUEBRA DE RECORDE
                if pontos > ranking[0][1]:
                    print("\nPARABÉNS VOCÊ ENTROU NO TOP 3 !")
                    print("\n|||||||||||  NOVO  RECORDE  |||||||||||")
                    print("\nVOCÊ FICOU EM 1º LUGAR !")
                    ranking[2][0] = ranking[1][0]
                    ranking[2][1] = ranking[1][1]
                    ranking[1][0] = ranking[0][0]
                    ranking[1][1] = ranking[0][1]
                    ranking[0][0] = nome
                    ranking[0][1] = pontos
                elif pontos > ranking[1][1]:
                    print("\nPARABÉNS VOCÊ ENTROU NO TOP 3 !")
                    print("\nVOCÊ FICOU EM 2º LUGAR !")
                    ranking[2][0] = ranking[1][0]
                    ranking[2][1] = ranking[1][1]
                    ranking[1][0] = nome
                    ranking[1][1] = pontos
                elif pontos > ranking[2][1]:
                    print("\nPARABÉNS VOCÊ ENTROU NO TOP 3 !")
                    print("\nVOCÊ FICOU EM 3º LUGAR !")
                    ranking[2][0] = nome
                    ranking[2][1] = pontos
                else:
                    dif = ranking[2][1] - pontos
                    print("\nSEM QUEBRA DE RECORDES!")
                    print("\nVOCÊ NÃO ENTROU NO TOP 3 POR %s PONTOS" % dif)
                print(la, lt)
                print(la1 % (dificuldade, ranking[0][0], ranking[0][1]))
                print(la2 % (ranking[1][0], ranking[1][1], ranking[2][0], ranking[2][1]))
                print(lt2, la)
                if nivel == 1:
                    ranking_f = ranking
                elif nivel == 2:
                    ranking_m = ranking
                else:
                    ranking_d = ranking
                b = 0
                while b == 0:
                    print("\nDESEJA JOGAR NOVAMENTE ?")
                    resp = int(input("SIM = 1  |||  NÃO = 0: "))
                    if resp == 1:
                        clear()
                        g = 0
                        b = 1
                    elif resp == 0:
                        print("\nVOLTANDO AO MENU PRINCIPAL...")
                        time.sleep(1)
                        clear()
                        g = 1
                        b = 1
                    else:
                        print("ESCOLHA ENTRE SIM(1) E NÃO(0) !!!")
        # OPÇÃO SAIR
        elif menu == 3:
            print("\nENCERRANDO...")
            m = 1
            time.sleep(1)
            clear()
        else:
            # EXCEÇÃO PARA CAPTAR ERROS
            print("Escolha um número de 1 a 3 !!!".upper())

    time.sleep(1)

if(__name__ == "__main__"):
    jogar()
