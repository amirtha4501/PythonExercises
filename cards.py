import itertools
import random


class CardDeck:
    
    def __init__(self):
        self.create()
        self.deck = []

    def create(self):
        faces = ['A','2','3','4','5','6','7','8','9','10','J','K',"Q" ]
        suits = ['H','S','D','C']
        self.deck = list(itertools.product(faces, suits))

    def show(self):
        for face, suit in self.deck:
            print('%s_%s' % (suit,face), end=" , ")

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
            card_val = self.deck.pop()
            print("\nHi", self.name.title() + "!\nYour card is: ", card_val)
            print("\nTotal Card count", len(self.deck))

    def play(self):
        ch = 'no'
        print("\n____________________________________________________________\n\n\t\tWELCOME TO CARD DRAW GAME\n____________________________________________________________")
        self.name = str(input("\n\nPlayer Name: "))
        self.create()
        
        while ch != "yes":
            print("\n\t1. Draw the card\n\t2. Shuffle the cards\n\t3. Show available cards")
            favour = int(input('\nYour wish: '))
        
            if favour == 1: 
                if len(self.deck) != 0:
                    self.shuffle()
                    self.draw_card()
                else:
                    print("\nHi", self.name.title() + "!\nCard is over")

            elif favour == 2:
                if len(self.deck) != 0:
                    self.shuffle()
                else:
                    print("\nHi", self.name.title() + "!\nCard is over")
    
            elif favour == 3:
                if len(self.deck) != 0:
                    self.show()
                    print("\n\nTotal Card count", len(self.deck))
                else:
                    print("\nHi", self.name.title() + "!\nCard is over")

            else:
                print("\nYour Choice is invalid")
                self.play()

            ch = str(input("\nDo you want to quit?\n(yes/no) : "))

cd = CardDeck()
cd.play()