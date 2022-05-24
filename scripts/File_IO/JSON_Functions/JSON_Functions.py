import time

import json
#import os
#from os import walk

from random import randint

JSON_Base_Path = "./static/JSON/"

Pretty_Print = False

def Pprint( Override, String ):
    if( Pretty_Print or Override ):
        print( String )

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

# Open a JSON file
def Open_JSON( File_Name ):
    print( File_Name )

    File_Location = JSON_Base_Path + File_Name

    try:
        with open( File_Location, "r", encoding="utf-8" ) as JSON_RAW_INFO:
            JSON_DATA = json.load( JSON_RAW_INFO )
        return JSON_DATA
    except:
        return { "Error": "File Doesn't exist" }

# Save a JSON file using new data
def Save_JSON( JSON, filename, indent ):
    # open(filename, 'a', encoding="utf-8")
    File_Location = JSON_Base_Path + filename
    #Pprint( False,json.dump(
    #JSON))

    out_file = open( File_Location, "w", encoding="utf-8" )

    #Pprint( False, "Before Dump" )

    if( indent == None ):
        json.dump( JSON, out_file )
    if( indent == 4 ):
        json.dump( JSON, out_file, indent = 4 )

    #Pprint( False, "After Dump" )

    out_file.close()

    return "Success!!!"

def Sort_Array( ARR ):
    return sorted(ARR, key=lambda x : x['name'].lower())
# -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

def Paid_Toggle( Player_Name ):
    print( " ->" + str( Player_Name ) )

    Players = Open_JSON( "players.json" )

    Count = 0
    for Player in Players[ "Players" ]:
        print( Player[ "name" ].lower() )
        print( Player_Name.lower() )
        if( Player[ "name" ].lower() == Player_Name.lower() ):
            print(  )
            print( " - -- -- --- --- - - -- -- --- --- - - -- -- --- --- - - -- -- --- --- -" )
            print( Players[ "Players" ][Count][ "name" ] )
            print( Players[ "Players" ][Count][ "paid" ] )
            print( Players[ "Players" ][Count][ "hand" ] )
            print( " - -- -- --- --- - - -- -- --- --- - - -- -- --- --- - - -- -- --- --- -" )
            print(  )
            if( Players[ "Players" ][Count][ "paid" ] == True ):
                print( " True --> False " )
                Players[ "Players" ][Count][ "paid" ] = False
            else:
                print( " False --> True " )
                Players[ "Players" ][Count][ "paid" ] = True

            Save_JSON( Players, "players.json", 4 )
            return "Success"
        Count += 1


    # Remove from Leaderboards
    return "Player Doesn't Exist"

def Player_Exists( Player_Name, Players ):
    for Player in Players[ "Players" ]:
        if Player[ "name" ].lower() == Player_Name.lower():
            return True
    return False

def Add_Player( Player_Name, Paid ):

    NewJSON = {
        "name": Player_Name,
        "paid": Paid,
        "hand": ""
    }

    Players = Open_JSON( "players.json" )

    if( Player_Exists( Player_Name, Players ) ):
        return "Player_Exists!!!"


    Players[ "Players" ].append( NewJSON )

    Players[ "Players" ] = Sort_Array( Players[ "Players" ] )
    Save_JSON( Players, "players.json", 4 )

    return str( Player_Name ) + " Added"

def Remove_Player( Player_Name ):
    Players = Open_JSON( "players.json" )
    Count = 0
    for Player in Players[ "Players" ]:
        if Player[ "name" ].lower() == Player_Name.lower():
            Players[ "Players" ].pop( Count )
            Players[ "Players" ] = Sort_Array( Players[ "Players" ] )
            Save_JSON( Players, "players.json", 4 )
            return str( Player[ "name" ] ) + " Removed!! "
        Count += 1
    return "Player Not found"

card = { "suit": "D", "value": "A" }

def Get_Players(  ):

    return Open_JSON( "players.json" )

def Add_Hand( Player ): # Should be a hand of 5 cards! { { "" }, {  }, {  }, {  }, {  }  }
    #print( Hand )
    print( Player )
    print( determine_rank('TH TD TS TC 2H') )
    return "Hello World!!!"

# ========================================================================================================================================
# Poker Hand Analyser Library for Project Euler: Problem 54
from collections import namedtuple

suits = "HDCS".split()
faces = "2,3,4,5,6,7,8,9,T,J,Q,K,A"
face = faces.split(',')

class Card(namedtuple('Card', 'face, suit')):
	def __repr__(self):
		return ''.join(self)

def royal_flush(hand):
	royalface = "TJQKA"
	# sort the cards based on the face rank of each card
	ordered = sorted(hand, key=lambda card: (faces.index(card.face), card.suit))

	first_card = ordered[0]
	other_cards = ordered[1:]

	# check if all are of the same suit
	if all(first_card.suit == card.suit for card in other_cards):
		# check if they are in sequential order
		# compare the ordered faces substring with the face list (which is converted to string)
		if ''.join(card.face for card in ordered) in royalface:
			return 'royal-flush', ordered[-1].face
	return False

def straight_flush(hand):
	# sort the cards based on the face rank of each card
	ordered = sorted(hand, key=lambda card: (faces.index(card.face), card.suit))

	first_card = ordered[0]
	other_cards = ordered[1:]

	# check if all are of the same suit
	if all(first_card.suit == card.suit for card in other_cards):
		# check if they are in sequential order
		# compare the ordered faces substring with the face list (which is converted to string)
		if ''.join(card.face for card in ordered) in ''.join(face):
			return 'straight-flush', ordered[-1].face
	return False

def four_of_a_kind(hand):
	allfaces = [f for f,s in hand]

	# create a unique set of ranks
	uniqueRanks = set(allfaces)

	# if there are more than 2 ranks, it's not four of a kind
	if len(uniqueRanks) != 2:
		return False

	for f in uniqueRanks:
		# if there are 4 faces, it is four of a kind
		if allfaces.count(f) == 4:
			uniqueRanks.remove(f)
			return "four-of-a-kind", f

	return False

def character_frequency(s):
	freq = {}
	for i in s:
		if i in freq:
			freq[i] += 1
		else:
			freq[i] = 1
	return freq

def full_house(hand):
	allfaces = [f for f,s in hand]

	rankFrequency = character_frequency(allfaces)

	# if there are 2 types of ranks and there's a card with 1 pair and 3 of a kind
	if len(rankFrequency) == 2 and (rankFrequency.values()[0] == 2 and rankFrequency.values()[1] == 3):
		return 'full-house'

	return False

def flush(hand):
	allfaces = [f for f,s in hand]

	first_card = hand[0]
	other_cards = hand[1:]

	if all(first_card.suit == card.suit for card in other_cards):
		return 'flush', sorted(allfaces, key=lambda f: face.index(f), reverse=True)

	return False

def straight(hand):
	ordered = sorted(hand, key=lambda card: (faces.index(card.face), card.suit))
	if ''.join(card.face for card in ordered) in ''.join(face):
		return 'straight', ordered[-1].face
	return False;

def three_of_a_kind(hand):
	allfaces = [f for f,s in hand]

	uniqueRanks = set(allfaces)

	if len(uniqueRanks) != 3:
		return False

	for f in uniqueRanks:
		if allfaces.count(f) == 3:
			uniqueRanks.remove(f)
			return "three-of-a-kind", f

	return False;

def two_pair(hand):
	allfaces = [f for f,s in hand]
	allftypes = set(allfaces)

	# collect pairs
	pairs = [f for f in allftypes if allfaces.count(f) == 2]

	# if there are more than two pairs
	if len(pairs) != 2:
		return False

	p1, p2 = pairs
	# get the difference using sets
	other_cards = [(allftypes - set(pairs)).pop()]
	return 'two-pair', pairs + other_cards if(face.index(p1) > face.index(p2)) else pairs[::-1] + other_cards

def one_pair(hand):
	allfaces = [f for f,s in hand]
	allftypes = set(allfaces)

	# collect pairs
	pairs = [f for f in allftypes if allfaces.count(f) == 2]

	# if there's more than one pair
	if len(pairs) != 1:
		return False

	allftypes.remove(pairs[0])
	return 'one-pair', pairs + sorted(allftypes, key=lambda f: face.index(f), reverse=True)

def high_card(hand):
	# collect all faces from each card
	allfaces = [f for f,s in hand]

	#sort the faces and show the highest card
	return "high_card", sorted(allfaces, key=lambda f: allfaces.index(f), reverse=True)[0]

def create_hand_tuple(cards = "5D 8C 9S JS AC"):
	hand = []

	for card in cards.split():
		face, suit = card[:-1], card[-1]
		hand.append(Card(face, suit))

	return hand;

# functions
handrankorder = (royal_flush,straight_flush,four_of_a_kind,full_house,
				flush,straight,three_of_a_kind,two_pair,
				one_pair,high_card)

def determine_rank(cards):
	hand = create_hand_tuple(cards)
	for ranker in handrankorder:
		rank = ranker(hand)

		if rank:
			break
	return rank
