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
    jogador1 = []
    jogador2 = []

    # distribui a mão inicial dos jogadores
    for i in range(3):
        distribui_carta(baralho, jogador1)
        distribui_carta(baralho, jogador2)

    print("{:>7}{:>7}{:>7}".format(jogador1[0], jogador1[1], jogador1[2]))
    print("{:>7}{:>7}{:>7}".format(jogador2[0], jogador2[1], jogador2[2]))
    
    mesa = []
    jogadores = [jogador1, jogador2]
    
    # coloca as cartas na mesa de acordo com o número selecionado pelo jogador
    for jogador in jogadores:
        selecione = int(input("Jogador #{} escolha um número de 1 a 3: ".format(jogador)))

        if selecione == 1:
            n1 = jogador.pop(0)
            mesa.append(n1)

        elif selecione == 2:
            n1 = jogador.pop(1)
            mesa.append(n1)

        elif selecione == 3:
            n1 = jogador.pop(2)
            mesa.append(n1)

    print(mesa)

    return mesa


def trunfo():
    naipes = ['\u2660', '\u2661', '\u2662', '\u2663']

    trunfo = random.choices(naipes)

    print("{}".format(trunfo))


def total(mesa):

    valores = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0, 'Q': 2,  
    'J': 3, 'K': 4, '7': 10, 'A': 10 }

    pts = 0
    for carta in mesa:
        p1 = valores[carta[0]]
        pts += p1


    return pts

def ganhador_turno():
    
    mesa = turno()

    if mesa[0] > mesa[1]:
        print("Vencedor jogador1")
        pts_p1 = total(mesa)
        print("Pontuação turno = ", pts_p1)
    elif mesa[1] > mesa[0]:
        print("Vencedor jogador2 ")
        pts_p2 = total(mesa)
        print("Pontuação turno = ", pts_p2)
# ganhador_turno()
# mesa = turno()
# total(mesa)

ganhador_turno()