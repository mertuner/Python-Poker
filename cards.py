import random

class Card:
    #
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def __eq__(self, other):
        #print("Worked! A")
        return self.value == other.value

    def __lt__(self, other):
        #print("Worked B")
        return self.value < other.value

    def __gt__(self, other):
        #print("Worked C")
        return self.value > other.value
    def __hash__(self):
        return (self.value)

    def __getitem__(self, item):
        return str(self.suit)[item]
    def __setitem__(self, item, value):
        str(self.value)[item] = value
    
    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value
    def __repr__(self):
        text = ""
        if self.value == 11:
            text = "J"
        elif self.value == 12:
            text = "Q"

        elif self.value == 13:
            text = "K"

        elif self.value == 14:
            text = "A"

        else:
            text = str(self.value)

        return text + " of " + self.suit



class Deck():
    # Building the deck and initializing
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffledeck()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearths"]:
            for v in range(2,15):
                self.cards.append(Card(s,v))


    def showd(self):
        # Number of cards in the deck
        print(len(self.cards))

        

    def shuffledeck(self):
           #Shuffling the deck
        random.shuffle(self.cards)

    def drawcard(self):
        return  self.cards.pop()



class Player():
    # Here we assinging a hand to players
    def __init__(self, deck):
        self.hand = []
        self.deck = deck
        self.draw(self.deck)

    def draw(self, deck):
        for i in range(0,2):
            self.hand.append((deck.drawcard()))









