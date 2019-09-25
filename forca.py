import random
import time
import os
def jogar():
    clear = lambda: os.system('cls')
    # -
    # APRESENTAÇÃO
    apresentação(3, 1, 4)
    # -
    # FERRAMENTAS PARA CRIAÇÃO DO RANKING DO JOGO
    global ranking
    global lista_rankingf
    global lista_rankingm
    global lista_rankingd
    global nivel
    ranking = []
    # -
    # MENU INICIAL
    m = 0
    clear()
    while m == 0:
        # CARREGA O RANKING ATUAL DE ARQUIVO EXTERNO
        carrega_ranking()
        # TELA DE BOAS VINDAS
        print("***************************************")
        print("*     BEM VINDO AO JOGO DA FORCA!     *")
        print("***************************************\n")
        print("||||||||||||||   MENU    ||||||||||||||")
        print("\n  1 - RANKING\n  2 - INICIAR\n  3 - SAIR")
        menu = int(input("\nESCOLHA UMA OPÇÃO: "))
        # OPÇÃO 1 = RANKING
        if menu == 1:
            clear()
            # SISTEMA DE CONSULTA DE RANKING
            consulta_ranking()
        elif menu == 2:
            g = 0
            # RESETANDO VARIÁVEIS PARA DEFINIR DIFICULDADE DO JOGO
            dificuldade = ""
            nivel = 0
            # RANKING
            ranking = []
            while g == 0:
                # LISTAS DE PALAVRAS POR DIFICULDADE
                carrega_palavras()
                # CAPTAÇÃO NOME
                clear()
                nome = input("\nDIGITE SEU NOME: ")
                # ESCOLHA DA DIFICULDADE
                print("\nEscolha um nível de dificuldade %s:" % nome)
                print("(1) FÁCIL  (2) MÉDIO  (3) DIFÍCIL\n(1) 12x -- (2) 09x -- (3) 06x")
                a = 0
                while a == 0:
                    nivel = int(input("NÍVEL: "))
                    if nivel == 1:
                        m_erros = 12
                        a = 1
                        ranking = lista_rankingf
                        dificuldade = "FÁCIL"
                        lista_palavras = lista_palavrasf
                    elif nivel == 2:
                        m_erros = 9
                        a = 1
                        ranking = lista_rankingm
                        dificuldade = "MÉDIO"
                        lista_palavras = lista_palavrasm
                    elif nivel == 3:
                        m_erros = 6
                        a = 1
                        ranking = lista_rankingd
                        dificuldade = "DIFÍCIL"
                        lista_palavras = lista_palavrasd
                    else:
                        # EXCEÇÃO PARA CAPTAR ERROS
                        print("Escolha um número de 1 a 3 !!!".upper())
                # VERIFICANDO O TAMANHO DA LISTA
                c = len(lista_palavras)
                # ESCOLHENDO UMA PALAVRA DA LISTA DE PALAVRAS COM RANDINT
                palavra_secreta = lista_palavras[random.randint(0, c-1)].strip()
                # LISTA DE CHUTES DA PESSOA
                chutes = []
                # BOOLEANOS DE ENFORCAMENTO E ACERTO
                enforcou = False
                acertou = False
                # CONTAGEM DE ERROS
                erros = 0
                # VERIFICANDO O TAMANHO DA PALAVRA E INSERINDO ESPAÇOS VAZIOS ("__") NA MESMA
                # QUANTIDADE DAS LETRAS DA PALAVRA NA LISTA lista USANDO List Comprehension
                b = len(palavra_secreta)
                lista = ["__" for letra in palavra_secreta]
                # CONTADOR DE CHUTES E LETRAS RESTANTES
                c_chutes = 0
                c_letras = 0
                clear()
                # TELA INICIAL
                print("***************************************")
                print("*     BEM VINDO AO JOGO DA FORCA!     *")
                print("***************************************")
                print("\n")
                while not enforcou and not acertou:
                    # print("\nPALAVRA S = %s" % palavra_secreta)
                    print("A PALAVRA SECRETA CONTÉM %d LETRAS" % b)
                    print("AINDA FALTA %d LETRAS PARA FINALIZAR" % (b - c_letras))
                    print("\n")
                    print(" ".join(lista))
                    print("\nSEUS CHUTES: ", chutes)
                    print("NÚMERO DE CHUTES: ", c_chutes)
                    print("TOTAL DE ERROS: %d de %d" % (erros, m_erros))
                    chute = input("\nDIGITE UMA LETRA: ").upper()
                    index = 0
                    chutes.append(chute)
                    if chute in palavra_secreta:
                        for letra in palavra_secreta:
                            if chute == letra:
                                lista[index] = chute
                                index += 1
                                c_letras += 1
                            else:
                                index += 1
                            if "".join(lista) == palavra_secreta:
                                acertou = True
                                break
                        clear()
                        print("\n||| LETRA %s ESTÁ NA PALAVRA !!!! |||" % chute)
                        print("------------------------------------")
                        print("\n")
                    else:
                        clear()
                        print("\n||| NÃO FOI ENCONTRADA A LETRA %s |||" % chute)
                        print("------------------------------------")
                        print("\n")
                        erros += 1
                    c_chutes += 1
                    if erros == m_erros:
                        enforcou = True
                clear()
                # VERIFICANDO SE ACERTOU OU ESTOUROU
                if acertou:
                    print("\nPARABÉNS VOCÊ ACERTOU A PALAVRA !")
                    print("\nRESUMO:")
                    print("RESPOSTA = %s" % palavra_secreta)
                    print("SEUS CHUTES: ", chutes)
                    print("NÚMERO DE CHUTES: ", c_chutes)
                    print("TOTAL DE ERROS: %d de %d" % (erros, m_erros))
                    print("\nVERIFICANDO RANKING...")
                    time.sleep(3)
                    # VERIFICAÇÃO E ATUALIZAÇÃO DE NOVO TOP 3 E QUEBRA DE RECORDE
                    verifica_ranking(erros, ranking, nome, dificuldade)
                    if nivel == 1:
                        lista_rankingf = ranking
                        atualiza_ranking()
                    elif nivel == 2:
                        lista_rankingm = ranking
                        atualiza_ranking()
                    else:
                        lista_rankingd = ranking
                        atualiza_ranking()
                else:
                    print("\nVOCÊ FALHOU !")
                    print("\nRESUMO:")
                    print("RESPOSTA = %s" % palavra_secreta)
                    print("SEUS CHUTES: ", chutes)
                    print("NÚMERO DE CHUTES: ", c_chutes)
                    print("TOTAL DE ERROS: %d de %d" % (erros, m_erros))
                    time.sleep(3)
                b = 0
                while b == 0:
                    print("\nDESEJA JOGAR NOVAMENTE ?")
                    resp = int(input("SIM = 1  |||  NÃO = 0: "))
                    if resp == 1:
                        clear()
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
            print("\nVOLTANDO AO MENU DE JOGOS !")
            print("\nENCERRANDO...")
            m = 1
            time.sleep(1)
            clear()
        else:
            # EXCEÇÃO PARA CAPTAR ERROS
            print("Escolha um número de 1 a 3 !!!".upper())

    # input()

def apresentação(a, b, c):
    # a: NÚMERO DE VEZES QUE A MENSAGEM É EXIBIDA
    # b: TEMPO ENTRE UMA MENSAGEM E OUTRA EM SEGUNDOS
    # c: LINHAS PARA PULAR ENTRE UMA MENSAGEM E OUTRA
    bva = "***************************************"
    bvt = "*     BEM VINDO AO JOGO DA FORCA!     *"
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

def carrega_palavras():
    # CAPTAÇÃO DE PALAVRAS DE UM ARQUIVO TXT
    arquivo = open("palavras.txt", "r")
    lista_palavras = []
    global lista_palavrasf
    global lista_palavrasm
    global lista_palavrasd
    lista_palavrasf = []
    lista_palavrasm = []
    lista_palavrasd = []
    for linha in arquivo:
        if linha == "FACIL\n":
            lista_palavrasf = lista_palavras
            lista_palavras = []
        elif linha == "MEDIO\n":
            lista_palavrasm = lista_palavras
            lista_palavras = []
        elif linha == "DIFICIL":
            lista_palavrasd = lista_palavras
        else:
            lista_palavras.append(linha.strip())
    lista_palavras = []
    arquivo.close()\

def carrega_ranking():
    # CAPTAÇÃO DE PALAVRAS DE UM ARQUIVO TXT
    arquivo = open("ranking.txt", "r")
    lista_ranking = []
    global lista_rankingf
    global lista_rankingm
    global lista_rankingd
    lista_rankingf = []
    lista_rankingm = []
    lista_rankingd = []
    for linha in arquivo:
        if linha == "FACIL\n":
            lista_rankingf = lista_ranking
            lista_ranking = []
        elif linha == "MEDIO\n":
            lista_rankingm = lista_ranking
            lista_ranking = []
        elif linha == "DIFICIL":
            lista_rankingd = lista_ranking
        else:
            lista_ranking.append(linha.strip())
    lista_ranking = []
    arquivo.close()\

def atualiza_ranking():
    # CAPTAÇÃO DE PALAVRAS DE UM ARQUIVO TXT
    arquivo = open("ranking.txt", "w")
    for nString in range(0, len(lista_rankingf)):
        arquivo.write(lista_rankingf[nString] + "\n")
    arquivo.write("FACIL\n")
    for nString in range(0, len(lista_rankingf)):
        arquivo.write(lista_rankingm[nString] + "\n")
    arquivo.write("MEDIO\n")
    for nString in range(0, len(lista_rankingf)):
        arquivo.write(lista_rankingd[nString] + "\n")
    arquivo.write("DIFICIL")
    arquivo.close()\

def consulta_ranking():
    # CONSULTA DE RANKING PELO USUÁRIO
    clear = lambda: os.system('cls')
    la = "\n***************************************"
    lt = "\n---------------------------------------"
    lt2 = "---------------------------------------"
    la1 = "  TOP 3 NÍVEL %s\n  1º: %s - %s ERROS                    "
    la2 = "  2º: %s - %s ERROS                    \n  3º: %s - %s ERROS                    "
    # SISTEMA DE CONSULTA DE RANKING
    print("||||||||||||||  RANKING  ||||||||||||||")
    c = 0
    # ESCOLHA DO NÍVEL A SER APRESENTADO
    while c == 0:
        print("\nEscolha um nível de dificuldade :\n\n(1) FÁCIL  (2) MÉDIO  (3) DIFÍCIL  (4) MENU")
        nivel = int(input("\nNÍVEL: "))
        if nivel == 1:
            ranking = lista_rankingf
            dificuldade = "FÁCIL"
            clear()
        elif nivel == 2:
            ranking = lista_rankingm
            dificuldade = "MÉDIO"
            clear()
        elif nivel == 3:
            ranking = lista_rankingd
            dificuldade = "DIFÍCIL"
            clear()
        elif nivel == 4:
            clear()
            c = 11
            break
        else:
            # EXCEÇÃO PARA CAPTAR ERROS
            print("Escolha um número de 1 a 4 !!!".upper())
        # EXIBIÇÃO DO RANKING COM VARIÁVEIS CONTENDO A FORMATAÇÃO
        print("||||||||||||||  RANKING  ||||||||||||||")
        print(la, lt)
        print(la1 % (dificuldade, ranking[0], ranking[1]))
        print(la2 % (ranking[2], ranking[3], ranking[4], ranking[5]))
        print(lt2, la)

def verifica_ranking(erros, ranking, nome, dificuldade):
    #VERIFICAÇÃO DE QUEBRA DE RECORDE
    la = "\n***************************************"
    lt = "\n---------------------------------------"
    lt2 = "---------------------------------------"
    la1 = "  TOP 3 NÍVEL %s\n  1º: %s - %s ERROS                    "
    la2 = "  2º: %s - %s ERROS                    \n  3º: %s - %s ERROS                    "
    if erros < int(ranking[1]):
        print("\nPARABÉNS VOCÊ ENTROU NO TOP 3 !")
        print("\n|||||||||||  NOVO  RECORDE  |||||||||||")
        print("\nVOCÊ FICOU EM 1º LUGAR !")
        ranking[5] = ranking[3]
        ranking[4] = ranking[2]
        ranking[3] = ranking[1]
        ranking[2] = ranking[0]
        ranking[0] = nome
        ranking[1] = str(erros)
    elif erros < int(ranking[3]):
        print("\nPARABÉNS VOCÊ ENTROU NO TOP 3 !")
        print("\nVOCÊ FICOU EM 2º LUGAR !")
        ranking[5] = ranking[3]
        ranking[4] = ranking[2]
        ranking[2] = nome
        ranking[3] = str(erros)
    elif erros < int(ranking[5]):
        print("\nPARABÉNS VOCÊ ENTROU NO TOP 3 !")
        print("\nVOCÊ FICOU EM 3º LUGAR !")
        ranking[4] = nome
        ranking[5] = str(erros)
    else:
        dif = erros - int(ranking[5])
        print("\nSEM QUEBRA DE RECORDES!")
        print("\nVOCÊ NÃO ENTROU NO TOP 3 POR %d ERROS" % dif)
    print(la, lt)
    print(la1 % (dificuldade, ranking[0], ranking[1]))
    print(la2 % (ranking[2], ranking[3], ranking[4], ranking[5]))
    print(lt2, la)

if(__name__ == "__main__"):
    jogar()
