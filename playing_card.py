# 'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠',
# 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥',
# 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦',
# 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣'
# playing card unicode: https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
import random


def playing_card():
    suit = ("\u2660", "\u2665", "\u2666", "\u2663")
    # print(suit)
    # rank = 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'
    # print(rank)
    rank = list("A123456789") + ["10"] + list("JQK")
    # print(rank)
    desk = []
    for s in suit:
        for r in rank:
            desk.append(r + s)
    return desk

d = playing_card()
print(d)
random.shuffle(d)
print(d)
p = random.sample(d, 1)
print(p)







playing_card()


