import random
import time

global x

x = 0

global y

y = 0

def Player():

    PlayerTotal = 0

    for card in PlayerHand:

        PlayerTotal = PlayerTotal + card

    return PlayerTotal

def DealerCheck(PlayerTotal,DealerTotal):

    if PlayerTotal > DealerTotal:

        hit(DealerHand)

    elif PlayerTotal == DealerTotal:

        hit(DealerHand)

    else:
        print("Player Total: " + str(PlayerTotal) + "\nDealer Total: " + str(DealerTotal))
        print("Dealer won")

        exit()

def CheckTotal(Hand):

    PlayerTotal = 0

    DealerTotal = 0

    if Hand == PlayerHand:

        for x in Hand:

            PlayerTotal = PlayerTotal + x

        if PlayerTotal > 21:

            for card in Hand:

                if card == 11:

                    card = 1

                    CheckTotal(PlayerHand)

            print("Busted")

            exit()

        return PlayerTotal

    elif Hand == DealerHand:

        for x in Hand:

            DealerTotal = DealerTotal + x

        if DealerTotal > 21:

            for card in Hand:

                if card == 11:

                    card = 1

                    CheckTotal(DealerHand)

            PlayerTotal = Player()
            print("Player Total: " + str(PlayerTotal) + "\nDealer Total: " + str(DealerTotal))
            print("Player Won")
            exit()

        return DealerTotal

def hit(Hand):

    if Hand == PlayerHand:

        global x

        Hand.append(random.randrange(2, 11))
        print("Your Card: " + str(Hand[2 + x]))
        CheckTotal(Hand)
        x = x + 1
        Options()

    else:

        global y

        Hand.append(random.randrange(2, 11))
        y = y + 1
        Dealer()

def stand():

    hit(DealerHand)
    time.sleep(1)
    Dealer()

def Dealer():

    PlayerTotal = CheckTotal(PlayerHand)
    DealerTotal = CheckTotal(DealerHand)
    DealerCheck(PlayerTotal, DealerTotal)



def split():
    pass

PlayerHand = []

DealerHand = []

PlayerHand.append(random.randrange(2,11))
PlayerHand.append(random.randrange(2,11))

print("Your Card: " + str(PlayerHand[0]))
print("Your 2nd Card: " + str(PlayerHand[1]))

DealerHand.append(random.randrange(2,11))

print("Dealers Card: " + str(DealerHand[0]))


def Options():

    if PlayerHand[0] == PlayerHand[1]:

        Option = int(input("1 --> Hit\n2 --> Stand\n3 --> Split\nEnter: "))

        if Option == 1:

            hit(PlayerHand)

        elif Option == 2:

            stand()

        elif Option == 3:

            split()

        else:

            print("Invalid input")

    else:

        Option = int(input("1 --> Hit\n2 --> Stand\nEnter: "))

        if Option == 1:

            hit(PlayerHand)

        elif Option == 2:

            stand()

        else:

            print("Invalid input")

Options()