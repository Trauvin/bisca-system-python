from random import shuffle
from card import Card

class Baralho:

    def shuffle_pack(self):
        pack = []
        naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}
        values = {'2', '3', '4', '5', '6', '7', 'Q', 'J', 'K', 'A'}
        
        for value in values:
            for naipe in naipes:
                pack.append(Card(value, naipe))
                
        shuffle(pack)
        
        return pack
    
    def return_card(self):
        pack = self.shuffle_pack()
        card = pack.pop()
        return card
    
b1 = Baralho()
print(b1.return_card().get())

