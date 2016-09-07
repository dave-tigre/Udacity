#!/usr/bin/env python

# Udacity's Design of Computer Programs
# Creating a Poker Game

import random
import itertools

import itertools

def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand."
    print max(itertools.combinations(hand,5), key = hand_rank)
    return max(itertools.combinations(hand,5), key = hand_rank)

def deal(numhands, n = 5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
	random.shuffle(deck)
	return [deck[n*i:n*(i+1)] for i in range(numhands)]

def poker(hand):
	"Return the best hand(s): poker([hand,...]) => [hand,...]"
	return allmax(hand, key = hand_rank)

def allmax(iterable, key=None):
	"Return a list of all items equal to the max"
	m = max(iterable, key=hand_rank)
	max_hands = []
	for n in iterable:
		if(hand_rank(n) == hand_rank(m)):
			max_hands.append(n)
	return max_hands

def straight(ranks):
	"Return True if the ordered ranks form a 5-card straight"
	return (max(ranks) - min(ranks) == 4) and (len(set(ranks)) == 5)

def flush(hand):
	"Return True if all the cards have the same suit"
	suits = [s for r, s in hand]
	return len(set(suits)) == 1

def kind(n, ranks):
	"""Return the first rank that this hand has exactly n of.
	Return None if the there is no n-of-a kind in the hand."""
	for r in ranks:
		if ranks.count(r) == n: return r
	return None

def two_pair(ranks):
	"""If there are two pair, return the two ranks as a tuple:
	(highest, lowest); otherwise return None."""
	pair = kind(2, ranks)
	lowpair = kind(2, list(reversed(ranks)))
	if pair and lowpair != pair:
		return (pair, lowpair)
	else:
		return None

def hand_rank(hand):
	"Return the ranking of the given hands in the form of a tuple"
	ranks = card_ranks(hand)
	if straight(ranks) and flush(hand):
		return (8, max(ranks))
	elif kind(4, ranks):
		return (7, kind(4, ranks), kind(1, ranks))
	elif kind(3, ranks) and kind(2,ranks):
		return (6, kind(3, ranks), kind(2, ranks))
	elif flush(hand):
		return (5, ranks)
	elif straight(ranks):
		return (4, max(ranks))
	elif kind(3, ranks):
		return (3, kind(3, ranks), kind(1, ranks))
	elif two_pair(ranks):
		return (2, two_pair(ranks), ranks)
	elif kind(2, ranks):
		return (1, kind(2, ranks), ranks)
	else:
		return (0, ranks)

	
def card_ranks(cards):
	"Return a list of the ranks, sorted"
	ranks = ['--23456789TJQKA'.index(r)  for r, s in cards]
	ranks.sort(reverse=True)
	return [5,4,3,2,1] if (ranks == [14,4,3,2,1]) else ranks

def test():
	"Test cases for the functions in poker programs"
	sf = "6C 7C 8C 9C TC".split() #straight flush
	fk = "9D 9H 9S 9C 7D".split() # four of a kind
	fh = "TD TC TH 7C 7D".split() # full house
	tp = "5S 5D 9H 9C 6S".split() # two pair
	fkranks = card_ranks(fk)
	tpranks = card_ranks(tp)
	assert kind(4, fkranks) == 9
	assert kind(3, fkranks) == None
	assert kind(2, fkranks) == None
	assert kind(1, fkranks) == 7
	assert two_pair(fkranks) == None
	assert two_pair(tpranks) == (9, 5) 
	assert straight([9,8,7,6,5]) == True
	assert straight([9,8,8,6,5]) == False
	assert flush(sf) == True
	assert flush(fk) == False
	assert poker([sf, fk, fh]) == [sf]
	assert poker([fk, fh]) == [fk]
	assert poker([fh, fh]) == [fh, fh]
	# special case testing
	assert poker([sf]) == [sf] # testing a single hand
	assert poker([sf]+99*[fk]) == [sf] # testing one hundred hands
	return "tests pass"
def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'

print test_best_hand()
