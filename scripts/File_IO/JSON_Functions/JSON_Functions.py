import time

import json
#import os
#from os import walk

from random import randint

JSON_Base_Path = "./static/data/JSON/"

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

def Sort_Array( ARR, key ):
    if( key == 'rank' ):
        return sorted(ARR, key=lambda x : int( x[ key ]))
    return sorted(ARR, key=lambda x : x[ key ].lower())
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
        "hand": "",
        "rank": "",
        "hand_name": ""
    }

    Players = Open_JSON( "players.json" )

    if( Player_Exists( Player_Name, Players ) ):
        return "Player_Exists!!!"


    Players[ "Players" ].append( NewJSON )

    Players[ "Players" ] = Sort_Array( Players[ "Players" ], 'name' )
    Save_JSON( Players, "players.json", 4 )

    return str( Player_Name ) + " Added"

def Remove_Player( Player_Name ):
    Players = Open_JSON( "players.json" )
    Count = 0
    for Player in Players[ "Players" ]:
        if Player[ "name" ].lower() == Player_Name.lower():
            Players[ "Players" ].pop( Count )
            Players[ "Players" ] = Sort_Array( Players[ "Players" ], 'name' )
            Save_JSON( Players, "players.json", 4 )
            return str( Player[ "name" ] ) + " Removed!! "
        Count += 1
    return "Player Not found"

card = { "suit": "D", "value": "A" }

def Get_Players(  ):

    return Open_JSON( "players.json" )


def Get_Leaders(  ):

    Temp_Players = {
        "Players": [ ]
    }

    Players = Get_Players(  )
    Count = 0
    for Player in Players[ "Players" ]:

        print( )
        print( Count )
        print( )
        print( Player[ "hand" ] )
        print( Player[ "paid" ] )

        if( Player[ "paid" ] == True ):
            if(  Player[ "hand" ] != "" ):
                print( "Adding: " + str( Player ) )
                Temp_Players["Players"].append( Player )
            else:
                pass

        else:
            pass

        print( )
        print( )

        Count = Count + 1

    #print( Players )
    Temp_Players["Players"] = Sort_Array( Temp_Players["Players"], 'rank' )

    #print( Players )
    return Temp_Players

def Update_Player( Player_Name, Hand, Rank, Hand_Name ):
    Players = Open_JSON( "players.json" )
    Count = 0

    for Player in Players[ "Players" ]:
        if Player[ "name" ].lower() == Player_Name.lower():
            Players[ "Players" ][Count][ "rank" ] = int( Rank )
            Players[ "Players" ][Count][ "hand_name" ] = Hand_Name
            Players[ "Players" ][Count][ "hand" ] = Hand
            Save_JSON( Players, "players.json", 4 )

        Count += 1
    return
