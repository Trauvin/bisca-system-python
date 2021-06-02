import random

def mistura_baralho():
    
    naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}
    valores = {'2', '3', '4', '5', '6', '7', 'J', 'K', 'Q', 'A'}
    baralho = []

    # cria um baralho de 40 cartas
    for naipe in naipes:
        for valor in valores:
            baralho.append(valor + ' ' +naipe)

    # mistura o baralho
    random.shuffle(baralho)

    return baralho



def distribui_carta(baralho, participante):

    carta = baralho.pop()
    participante.append(carta)
    return carta

def turno():
    baralho = mistura_baralho()
    # while(baralho != 0):
    jogador1 = []
    jogador2 = []
    jogador3 = []
    jogador4 = []

    # distribui a mão inicial dos jogadores
    for i in range(3):
        distribui_carta(baralho, jogador1)
        distribui_carta(baralho, jogador2)
        distribui_carta(baralho, jogador3)
        distribui_carta(baralho, jogador4)

    print("{:>7}{:>7}{:>7}".format(jogador1[0], jogador1[1], jogador1[2]))
    print("{:>7}{:>7}{:>7}".format(jogador2[0], jogador2[1], jogador2[2]))
    print("{:>7}{:>7}{:>7}".format(jogador3[0], jogador3[1], jogador3[2]))
    print("{:>7}{:>7}{:>7}".format(jogador4[0], jogador4[1], jogador4[2]))
    

    return jogador1, jogador2, jogador3, jogador4


def trunfo():
    naipes = ['\u2660', '\u2661', '\u2662', '\u2663']

    trunfo = random.choices(naipes)

    print("{}".format(trunfo))


def total(mao):

    valores = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 10, 
    'J': 3, 'K': 4, 'Q': 2, 'A': 10 }


# trunfo()
turno()
    
