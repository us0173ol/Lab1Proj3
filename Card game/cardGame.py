import random

class Card(object):

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def show(self):
        print ("{} of {} ".format(self.rank, self.suit))

    def cardValue(self):
        return self.value

class Deck(object):

    def __init__(self):
        self.cards = []
        self.create()

    def create(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(1, 14):
                if value > 1 and value < 11:
                    rank = value
                if value == 1:
                    rank = "Ace"
                    value = 11
                if value == 11:
                    rank = "Jack"
                    value = 10
                if value == 12:
                    rank = "Queen"
                    value = 10
                if value == 13:
                    rank = "King"
                    value = 10

                self.cards.append(Card(suit, rank, value))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        #start at the end of the list of cards, go to zero, decrementing
        for i in range(len(self.cards)-1, 0, -1):
            #pick random element from the list to shuffle
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()

class Player (object):

    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()
            # print(self.name, "has: "+ str(card.show()))
    def getValue (self):
        self.playerHand = []
        for cards in self.hand:
            self.playerHand.append(int(cards.value))

        print(sum(self.playerHand))
        return sum(self.playerHand)

class Dealer (object):

    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw(self, deck):
        self.hand.append(deck.draw())
        return self

    def showHand(self):
        # self.dH = []
        for card in self.hand:
             card.show()
        #     self.dH.append(str(card.show))
        # print(self.dH[1])

    def getValue(self):
        self.dealerHand = []
        for cards in self.hand:
            self.dealerHand.append(int(cards.value))

        print(sum(self.dealerHand))
        return sum(self.dealerHand)

# name = input("What is your name? ")
# player = Player(str(name))
class Game():
    player = Player("Mike")
    dealer = Dealer("Dealer")
    deck = Deck()
    deck.shuffle()
    player.draw(deck)
    dealer.draw(deck)
    player.draw(deck)
    dealer.draw(deck)
    print(player.name, "has1: ")
    player.showHand()

    print(dealer.name, "shows2: ")
    dealer.showHand()

    print(player.name, "has3:  ")
    player.getValue()
    t = True
    while player.getValue() < int(21) and t == True:
        hit = str(input("Hit (h) or Stay (s)? " ))
        if hit == str("h"):
            player.draw(deck)
            print(player.name, "has4: ")
            player.showHand()

            print(player.name, "has5: ")
            player.getValue()

            if player.getValue() > int(21):
                print ("You went over, Dealer wins!!")
                break
            if player.getValue() == int(21):
                print("Blackjack!")
                t = False
        elif hit == str("s"):
            t = False
            print("You have decided to stay. ")
            while dealer.getValue() <= player.getValue():
                dealer.draw(deck)
                print(dealer.name, "has6: ")
                dealer.showHand()
                print(dealer.name, "has7: ")
                dealer.getValue()
                if dealer.getValue() == player.getValue():
                    print("Draw!")
                    break
                elif dealer.getValue() > player.getValue() and dealer.getValue() < int(22):
                    print("Dealer wins!!")
                    break
                elif dealer.getValue() < int(17):
                    dealer.draw(deck)
                    print(dealer.name, "has8: ")
                    dealer.showHand()
                    print(dealer.name, "has9: ")
                    dealer.getValue()
                else:
                    print("You win!")
                    break

game = Game()
