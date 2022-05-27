import csv
import time

from timeit import default_timer as timer
from datetime import timedelta

import random

CSV_Base_Path = "./static/data/CSV/"

Poker_Hands_Data_Path = CSV_Base_Path + "Hand_Data.csv"

Keys = "Rank,Hand_Name,Cards_Bulk,Card_1,Card_2,Card_3,Card_4,Card_5".split(",")

def Name_To_Key( Name ):

    if ( Name == 'Rank' ):
        return 0
    elif ( Name == 'Hand_Name' ):
        return 1
    elif ( Name == 'Cards_Bulk' ):
        return 2
    elif ( Name == 'Card_1' ):
        return 3
    elif ( Name == 'Card_2' ):
        return 4
    elif ( Name == 'Card_3' ):
        return 4
    elif ( Name == 'Card_4' ):
        return 4
    elif ( Name == 'Card_5' ):
        return 4
    else:
        return -1

def Face_To_Num( Value ):
    if ( Value not in [ 'A', 'Q', 'K', 'J', 'T', '?' ] ):
        return int( Value )
    elif ( Value == 'A' ):
        return 14
    elif ( Value == 'K' ):
        return 13
    elif ( Value == 'Q' ):
        return 12
    elif ( Value == 'J' ):
        return 11
    elif ( Value == 'T' ):
        return 10
    elif ( Value == '?' ):
        return 15
    else:
        return 'Error'

def Num_To_Face( Value ):
    if ( Value == 15 ):
        return '?'
    elif ( Value == 14 ):
        return 'A'
    elif ( Value == 13 ):
        return 'K'
    elif ( Value == 12 ):
        return 'Q'
    elif ( Value == 11 ):
        return 'J'
    elif ( Value == 10 ):
        return 'T'
    elif ( Value == 9 ):
        return '9'
    elif ( Value == 8 ):
        return '8'
    elif ( Value == 7 ):
        return '7'
    elif ( Value == 6 ):
        return '6'
    elif ( Value == 5 ):
        return '5'
    elif ( Value == 4 ):
        return '4'
    elif ( Value == 3 ):
        return '3'
    elif ( Value == 2 ):
        return '2'
    else:
        return 'Error'

# Limits to a specific decimal point
def Places( Number, places ):
    if( places == 2 ):
        return float("{0:.2f}".format(Number)) # Better for printing
    elif( places == 4 ):
        return float("{0:.4f}".format(Number)) # Better for printing
    elif( places == 3 ):
        return float("{0:.3f}".format(Number)) # Better for printing
    else:
        return float("{0:.2f}".format(Number)) # Better for printing

def Open_CSV( filename ):

    CSV_File = []
    with open( filename, newline = '', encoding="utf-8" ) as f:
        reader = csv.reader( f )
        for row in reader:
            CSV_File.append( row )

    return CSV_File

def Save_CSV( filename, Data ):

    with open( filename, 'w', newline = '', encoding="utf-8" ) as f:
        write = csv.writer( f )
        write.writerows( Data )

    return "Saved!!!"

"""
def Search_UPC( UPC ):
    count = 0
    for row in UPC_Data:
        count = count + 1

        if( row[ 0 ] == UPC ):
            #print( row )
            return row

    print( "UPC Not Found!!!" )
"""

Cards  = [ "?", "A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2" ]
Values = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ]

# Ran at begining of the Application
def Initialize_OBJS(  ):
    #print( "Init Objs" )
    global Hand_Data
    Hand_Data = Open_CSV( Poker_Hands_Data_Path )
    #print( Hand_Data )
Initialize_OBJS(  )

def Deconstruct_Card( Card ):
    if( Card == '?' ):
        return '?', ''
    return Card[0], Card[1]

def Is_Flush( Suits ):
    Suit = Suits[0]
    for Item in Suits:
        if( Item != Suit ):
            return False
    return True

def Get_Ordered_Hand_Values( Hand_String ):
    Hand = Hand_String.split(" ")
    print( Hand )
    Value,Suit = Deconstruct_Card( Hand[0] )
    print( Value )

    Suits = [  ]
    Hand_Nums = [  ]

    for Card in Hand:
        Value,Suit = Deconstruct_Card( Card )
        print( Value )
        Value = Face_To_Num( Value )
        print( Value )
        if( Value != 15 ):
            Hand_Nums.append( Value )

            print( "HERE!!!: " + str( Value ) )
            Suits.append( Suit )

    Hand_Nums = sorted( Hand_Nums, reverse=True )
    print( Hand_Nums )

    Ordered_Hand = [  ]
    Hand_String = ""
    for Card_Num in Hand_Nums:
        Card_Value = Num_To_Face( Card_Num )
        Ordered_Hand.append( Card_Value )
        Hand_String += Card_Value + " "

    Hand_String = Hand_String.strip()
    print( Ordered_Hand )
    print( Hand_String )
    print( Suits )

    return Hand_String, Ordered_Hand, Is_Flush( Suits )

def Rank_Hand( Ordered_Hand_String, Is_Flush ):
    Ordered_Hand_String_List = Ordered_Hand_String.split(" ")
    print(  )
    print( Ordered_Hand_String )
    for row in Hand_Data:
        if( Ordered_Hand_String in row[ Name_To_Key( "Cards_Bulk" ) ] ):
            Rank = row[ Name_To_Key( "Rank" ) ]
            Hand_Name = row[ Name_To_Key( "Hand_Name" ) ]
            if( "flush" in Hand_Name.lower(  ) ):
                if( Is_Flush ):
                    print( row )
                    print( "|-> Flush <-|" )
                    return Rank, Hand_Name
            else:
                print( row )
                return Rank, Hand_Name

    return Rank, Hand_Name
    print(  )

def Eval_Hand( Hand_String ):
    print(  )
    print( "Start Eval_Hand(  )" )

    print()
    count = 0

    Ordered_Hand_String, Ordered_Hand, Is_Flush = Get_Ordered_Hand_Values( Hand_String )

    #Hand = Order_Hand( Hand )

    print( "Ordered_Hand: " + str( Ordered_Hand ) )
    print( "Is_Flush: " + str( Is_Flush ) )

    Rank, Hand_Name = Rank_Hand( Ordered_Hand_String, Is_Flush )

    print()

    print( "End Eval_Hand(  )" )
    print(  )

    return Rank, Hand_Name

def Fix_Data():
    Count = 0
    Place = Name_To_Key( "Cards_Bulk" )
    for row in Hand_Data:

        Hand_Nums = [  ]
        Hand_List = row[ Place ].split(" ")
        for Face in Hand_List:
            Value = Face_To_Num( Face )


            Hand_Nums.append( Value )


        Hand_Nums = sorted( Hand_Nums, reverse=True )
        Hand_Nums_String = ""

        for Card in Hand_Nums:
            Hand_Nums_String += str( Num_To_Face( Card ) ) + " "


        Hand_Nums_String = Hand_Nums_String.strip()
        print( Hand_Nums_String )
        #Hand_Data[ Count ][ Name_To_Key( "Hand_Name" ) ] =
        Hand_Data[ Count ][ Place ] = Hand_Nums_String
        Count += 1

    Save_CSV( "Ordered.csv", Hand_Data )
