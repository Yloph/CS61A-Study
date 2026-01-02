### Iterators


## iter and next
"""
iter(iterable) -> return an iterator over the elements of an iterable value
next(iterator) -> return the next element in an iterator
"""
s = [[1, 2], 3, 4, 5]
t = iter(s)


## Dictionary Iteration
"""
An iterable value is any value that can be passed to iter to produce iterator
An iterator is returned from iter and can be passed to next
All iterators are mutable

Cannot change dictionary size during iteration
"""


## For Statement
r = range(3, 6)

for i in r:
    print(i)

for i in r:
    print(i) # same as above

ri = iter(r)
for i in ri:
    next(i) # 3 4 5

for i in ri:
    next(i) # nothing will be printed



## Built-in Iterator Functions
# map(func, iterable) -> iterate func(x) for x in iterable
bcd = ['b', 'c', 'd']
m_bcd = map(lambda x: x.upper(), bcd)
list(m_bcd) # same as [x.upper() for x in bcd]

def double(x):
    print('**', x, '=>', 2 * x, '**')
    return 2 * x
m = map(double, [2, 3, 4, 5]) # double applied lazily
next(m) # double will be applied

# filter(func, iterable) -> iterate x in iterable if func(x)
m = map(double, range(3, 7))
f = lambda y: y >= 10
t = filter(f, m)

next(t)
next(t)

list(filter(f, map(double, range(3, 7))))
# zip(first_iter, second_iter) -> iterate over co-indexed (x, y) pairs
list(zip([1, 2], [3, 4]))
# if an iterable is longer, zip only iterates over matched and skip extra
list(zip([1, 2], [3, 4, 5]))
# more than two iterables can be passed to zip
list(zip([1, 2], [3, 4, 5], [6, 7]))

def palindrome(s):
    """
    Return whether s is the same backward and forward
    """
    # return all([a == b for a, b in zip(s, reversed(s))])
    return list(s) == list(reversed(s))

# reversed(sequence) -> iterate over x in a sequence in reverse order
# sorted(iterable) -> create a sorted list containing x in iterable


## Blackjack
import random

points = {'J': 11, 'Q': 12, 'K': 13, 'A': 1}

def hand_score(hand):
    """
    hand: a list of cards in hand

    Compute total score in hand
    """
    tot = sum([points.get(card, card) for card in hand])
    if tot <= 11 and 'A' in hand:
        return tot + 10
    
    return tot

def shuffle_cards():
    deck = (['J', 'Q', 'K', 'A'] + list(range(2, 11))) * 4
    random.shuffle(deck)
    return iter(deck)

def player_turn(up_card, cards, strategy, deck):
    while hand_score(cards) <= 21 and strategy(up_card, cards):
        cards.append(next(deck))

def dealer_turn(cards, deck):
    while hand_score(cards) <= 17:
        cards.append(next(deck))

def blackjack(strategy, announce = print):
    deck = shuffle_cards()

    player_cards = [next(deck)]
    up_card = next(deck)
    player_cards.append(next(deck))
    hole_card = next(deck)

    player_turn(up_card, player_cards, strategy, deck)
    if hand_score(player_cards) > 21:
        announce('Player goes bust with', player_cards, 'againist a', up_card)

        return -1
    
    dealer_cards = [up_card, hole_card]
    dealer_turn(dealer_cards, deck)
    if hand_score(dealer_cards) > 21:
        announce('Dealer busts with', dealer_cards)

        return 1
    else:
        announce('Player has', hand_score(player_cards))
        announce('Dealer has', hand_score(dealer_cards))
        diff = hand_score(player_cards) - hand_score(dealer_cards)
        return max(-1, min(1, diff))

def basic_strategy(up_card, cards):
    if hand_score(cards) <= 11:
        return True
    if up_card in [2, 3, 4, 5, 6]:
        return False
    
    return hand_score(cards) < 17

def shh(*args):
    """
    Don't print or do anything
    """

def gamble(strategy, hand = 1000):
    return sum([blackjack(strategy, shh) for _ in range(hand)])