import funcoes as jogo
tabuleiro = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
# Atualizar tabuleiro.
##JOGO:

ordem = jogo.quem_joga()
#test
for rodada in range(0,5):
    for jogador in ordem:
        jogo.desenho(tabuleiro)

        tabuleiro = jogo.joga(jogador,tabuleiro)

        vencedor = jogo.ganhou(tabuleiro,jogador)

        if vencedor == True:
            break

    if vencedor == True:
        x = jogo.desenho(tabuleiro)
        print(f'O jogador {jogador} ganhou')
        break

if vencedor == False:
    x = jogo.desenho(tabuleiro)
    print('Velha!!!!')

