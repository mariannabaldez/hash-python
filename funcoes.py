import random

def joga(jogador, tabuleiro):
    while True:
        while True:
            linha = input("Jogador {}, digite a posição em linha: ".format(jogador))
            coluna = input("Jogador {}, digite a posição em coluna: ".format(jogador))
            if linha.isnumeric() and coluna.isnumeric():
                linha = int(linha)
                coluna = int(coluna)
                break
            else: print("Invalido,digite novamente!")

        if coluna >= 0 and coluna <= 2 and linha >= 0 and linha <= 2:
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogador
                break
            else: print("esse espaço ja foi ocupado")
        else:
            print("O numero de colunas e/ou linhas precisa ser de 0 a 2, digite novamente.")
    return tabuleiro

def desenho(algumacoisa):
    for valores in algumacoisa:
        print(valores)

def quem_joga():
    jogadores = ['x', 'o']
    jogador1 = random.choice(jogadores)
    jogador2 = jogadores.remove(jogador1)
    jogador2 = jogadores[0]
    ordem_de_jogo = [jogador1, jogador2]
    return ordem_de_jogo

def ganhou_linha(tabuleiro, jogador):
    for linha in tabuleiro:
        contador = 0
        for coluna in linha:
            if coluna == jogador:
                contador += 1
        if contador == 3:
            venceu = True
            break
        else: venceu = False
    return venceu

def ganhou_coluna(tabuleiro,jogador):
    for coluna in range(0,3):
        contador = 0
        for linha in range(0,3):
            if tabuleiro[linha][coluna] == jogador:
                contador += 1
        if contador == 3:
            venceu = True
            break
    else: venceu = False
    return venceu

def ganhou_diagonal(tabuleiro, jogador):
    for coluna in range(0,3):
        contador = 0
        for linha in range(0,3):
            if coluna == linha:
                if tabuleiro[linha][coluna] == jogador:
                    contador += 1
        if contador == 3:
            venceu = True
            break
        else: venceu = False
    return venceu

def ganhou_inversa(tabuleiro, jogador):
    for linha in range(0,3):
        for coluna in range(3,0,-1):
            if tabuleiro[0][2] == jogador \
                    and tabuleiro[1][1] == jogador \
                    and tabuleiro[2][0] ==jogador:
                venceu = True
                break
            else: venceu = False
    return venceu


def ganhou(tabuleiro,jogador):
    venceu = []
    venceu.append([ganhou_linha(tabuleiro, jogador),
                  ganhou_coluna(tabuleiro,jogador),
                  ganhou_diagonal(tabuleiro, jogador),
                  ganhou_inversa(tabuleiro, jogador)])
    if venceu[0].count(True) >= 1:
        venceu = True

    return venceu

