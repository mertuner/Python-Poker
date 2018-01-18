from cards import Deck
from cards import Player
from cards import Card
import itertools



class Poker():
    def __init__(self):
        self.deck = Deck()

    def dealcards(self):
        self.player1 = Player(self.deck)
        print(self.deck.showd())
        return self.player1.hand

    def dealcards2(self):
        self.player2 = Player(self.deck)
        print(self.deck.showd())
        return self.player2.hand


    def p1cardswithboard(self, hand):
        # Here we givind board cards to player1
        self.p1fullhand = []
        for j in range(len(hand)):
            self.p1fullhand.append(hand[j])
        for i in range(5):
            self.p1fullhand.append(self.boardcards[i])

        return self.p1fullhand

    def p2cardswithboard(self, hand):
        # Here we givind board cards to player2
        self.p2fullhand = []
        for i in range(len(hand)):
            self.p2fullhand.append(hand[i])
        for j in range(5):
            self.p2fullhand.append(self.boardcards[j])
        return self.p2fullhand

    def best5(self, hand):
        #Here we'r determining the best 5 cards out of 7
        self.allcomb = []
        self.eachhand = list(itertools.combinations(hand, 5))
        for i in range(len(self.eachhand)):
            self.allcomb.append(poker.hand_rank1(self.eachhand[i]))

        self.besthandindex = max(self.allcomb)
        for j in range(len(self.allcomb)):
            if self.besthandindex == self.allcomb[j]:
                self.besthand = self.eachhand[j]

        print(self.besthand)
        return self.besthand

    def board(self):
        self.boardcards = []
        for i in  range(5):
            self.boardcards.append(self.deck.drawcard())

        return self.boardcards



    def hand_rank(self, hand):
        "Return a value indicating the ranking of a hand"
        self.ranks = poker.card_ranks(hand)
        if poker.straight(self.ranks) and poker.flush(hand):
            print("Straight Flush")
            return (8,max(self.ranks))
        elif poker.kind(4, self.ranks):
            print("Four of kind")
            return (7, poker.kind(4,self.ranks))
        elif poker.kind(3, self.ranks) and poker.kind(2, self.ranks):
            print("Full House")
            return (6, poker.kind(3, self.ranks), poker.kind(2, self.ranks))
        elif poker.flush(hand):
            print("Flush")
            return (5, self.ranks)
        elif poker.straight(self.ranks):
            print("Straight")
            return (4, max(self.ranks))
        elif poker.kind(3, self.ranks):
            print("Three of kind")
            return (3, poker.kind(3, self.ranks), self.ranks)
        elif poker.two_pairs(self.ranks):
            print("Two Pairs")
            return (2, poker.two_pairs(self.ranks), self.ranks)
        elif poker.kind(2, self.ranks):
            print("One pair")
            return  (1, poker.kind(2, self.ranks), self.ranks)
        else:
            print("High Card")
            return (0,self.ranks)
    def hand_value(self, hand):
        "Return a value indicating the ranking of a hand"
        self.ranks = poker.card_ranks(hand)
        if poker.straight(self.ranks) and poker.flush(hand):
            return "Straight flush"
        elif poker.kind(4, self.ranks):
            return "4 of a kind"
        elif poker.kind(3, self.ranks) and poker.kind(2, self.ranks):
            return "Full House"
        elif poker.flush(hand):
            return "Flush"
        elif poker.straight(self.ranks):
            return "Straight"
        elif poker.kind(3, self.ranks):
            return "3 of a kind"
        elif poker.two_pairs(self.ranks):
            return "Two Pairs"
        elif poker.kind(2, self.ranks):
            return "One pair"
        else:
            return "High Card"
    def hand_rank1(self, hand):
        "Return a value indicating the ranking of a hand"
        self.ranks = poker.card_ranks(hand)
        if poker.straight(self.ranks) and poker.flush(hand):
            return (8,max(self.ranks))
        elif poker.kind(4, self.ranks):
            return (7, poker.kind(4,self.ranks))
        elif poker.kind(3, self.ranks) and poker.kind(2, self.ranks):
            return (6, poker.kind(3, self.ranks), poker.kind(2, self.ranks))
        elif poker.flush(hand):
            return (5, self.ranks)
        elif poker.straight(self.ranks):
            return (4, max(self.ranks))
        elif poker.kind(3, self.ranks):
            return (3, poker.kind(3, self.ranks), self.ranks)
        elif poker.two_pairs(self.ranks):
            return (2, poker.two_pairs(self.ranks), self.ranks)
        elif poker.kind(2, self.ranks):
            return  (1, poker.kind(2, self.ranks), self.ranks)
        else:
            return (0,self.ranks)


    def card_ranks(self, hand):
        self.ranks = [i for i in hand]
        self.ranks.sort(reverse=True)
        #print(self.ranks)
        return [5,4,3,2,1] if (max(self.ranks) - min(self.ranks) == 9 and len(set(self.ranks)) == 5 and str(max(self.ranks))[1] == 'A') else self.ranks
        #return self.ranks

    def straight(self, ranks):
        self.ranks = ranks
        "Return True if the case is true"
        return (max(self.ranks) - min(self.ranks) == 4) and len(set(self.ranks)) == 5

    def flush(self, hand):
        self.flushcount = 1
        for i in range(len(hand)):
            if i + 1 == 5:
                break

            if hand[i][:2] == hand[i+1][:2]:
                self.flushcount += 1



        return self.flushcount == 5


    def kind(self, n, rank):
        for r in rank:
            if rank.count(r) == n: return r
        return None

    def two_pairs(self, rank):
        self.rank = rank
        self.pair = self.kind(2,rank)
        self.lowpair = self.kind(2, list(reversed(self.rank)))
        if self.pair and self.lowpair != self.pair:
            return (self.pair, self.lowpair)
        else:
            return None


poker = Poker()


board = poker.board()
player1 = poker.dealcards()
player2 = poker.dealcards2()
bestforp1 = poker.best5(poker.p1cardswithboard(player1))
result1 = poker.hand_rank(bestforp1)
bestforp2 = poker.best5(poker.p2cardswithboard(player2))
result2 = poker.hand_rank(bestforp2)


