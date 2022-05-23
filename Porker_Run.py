#( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )
# /
#/
#
#------------------------------------------|
#    # Imported Libraries
#------------------------------------------|

# Added functionality to the Calculations. am close to having all variables needed to crunch numbers successfully just need CAse

from flask import Flask, render_template, request
import multiprocessing

#------------------------------------------|
#    # Import other python modules
#------------------------------------------|

#import scripts.Example.Example_Script as Example_Script
#<++| Import Hooks |++>

#
#\
# \
#( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )( )

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
# /
#/
#
#------------------------------------------|
#    # Flask: Porker_Run
#------------------------------------------|

app = Flask(__name__)

#
#\
# \
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

#===========================================
# /
#/        Global Variables
#
#------------------------------------------|
#    # Color Variables
#------------------------------------------|


Colors = {
    "Primary" : "g-white",
    "Secondary" : "g-black",
    "Background_Primary" : "g-gray",
    "Background_Secondary" : "g-lightgray",
    "Button_Primary": "g-blue",
    "Button_Secondary": "g-red"
}

#<++| Color Hooks |++>

#
#\
# \
#===========================================

#{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }
# /
#/
#
#------------------------------------------|
#    # Middleware WITHOUT Routes
#------------------------------------------|

"""
def Sample_Middleware_Function(  ):
    return "Sample_Middleware_Function Return"
"""

#<++| Middleware Hooks |++>

#
#\
# \
#{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }{ }

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# /
#/        # POST functions
#

#<++| API POST Hooks |++>

"""
@app.route("/Sample_Post", methods=['POST'])
def Sample_Post(  ):
    print( "---- Sample_Post( ) Start ----" )

    if request.method == "POST":
        JSON_Info = request.get_json()
        ARG_Info = request.args.to_dict()

        return JSON_Info

    return "Error"
"""

#
#\
# \
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
# /
#/        #    Routes for Flask: Porker_Run
#

#------------------------------------------|
#    # Landing Page: Porker_Run
#------------------------------------------|




#------------------------------------------|
#    # /Player_Input
#------------------------------------------|

# Player_Input GET API:
@app.route("/Player_Input")

def Player_Input(  ):

    title = "Player_Input"

    return render_template('Player_Input/Player_Input.html', title=title, Colors=Colors)



#------------------------------------------|
#    # /Add_Cards
#------------------------------------------|

# Add_Cards GET API:
@app.route("/Add_Cards")

def Add_Cards(  ):

    title = "Add_Cards"

    return render_template('Add_Cards/Add_Cards.html', title=title, Colors=Colors)



#------------------------------------------|
#    # /Results
#------------------------------------------|

# Results GET API:
@app.route("/Results")

def Results(  ):

    title = "Results"

    return render_template('Results/Results.html', title=title, Colors=Colors)



@app.route("/")
def Porker_Run():
    return render_template('Porker_Run.html', title="Porker_Run", Colors=Colors)

"""
#------------------------------------------|
#    # /Sample_Route
#------------------------------------------|

# Sample_Route:
@app.route("/Sample_Route/<Sample_Text>")

def Sample_Route( Sample_Text ):

    Title = "Sample Route"

    return render_template('Sample/Sample_Route.html', Title=Title, Sample_Text=Sample_Text, Colors=Colors)
"""

#\
# \
#[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
# /
#/        #    Boot up: Porker_Run ( Ran on start of script )
#

#------------------------------------------|
#    # Default namespace run
#------------------------------------------|

#<++| PROCESS Hooks |++>
def Start_Porker_Run( ip, port, Debug_Status ):
    app.run( host=ip, port=port, debug=Debug_Status )
    print("\nUp and Running!!!\n")

#\
# \
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

#++++++++++++++++++++++++++++++++++++++++++++++++++++
# /
#/        #    Boot up Porker_Run ( Ran on start of script )
#

if __name__ == "__main__":
    Porker_Run_JOBS = [  ]

    # Add Porker_Run to the Multiprocessor
    ip = 'localhost'
    port = 5000
    
    #Debug = False
    Debug = True

    # JOB: 1
    # Porker_Run
    Default_Porker_Run = multiprocessing.Process(target=Start_Porker_Run, args=( ip, port, Debug,))
    Porker_Run_JOBS.append( Default_Porker_Run )
    Default_Porker_Run.start()

#
#\
# \
#++++++++++++++++++++++++++++++++++++++++++++++++++++

#<++||++>##<++||++>##<++||++>##<++||++>##<++||++>##<++||++>##<++||++>##<++||++>##<++||++>##<++||++>##<++||++>##<++||++>##<++||++>##<++||++>#
#
#<++| All_Hooks |++>#

# Import Hooks      =   All_Pages_Have a .py file
# Color Hooks           =   ToDo: Think about it
# API GET Hooks    =   GET hook for each
# API POST Hooks   =   SINGLE post hook for project with triggers
# PROCESS Hooks         =   Default Process

# Project_Name     =   User_Input  =   From input

#
#<++||++>##<++||++>##<++||++>##<++||++>##<++||++>##<++||++>##<++||++>##<++||++>##<++||++>##<++||++>##<++||++>##<++||++>##<++||++>##<++||++>#
