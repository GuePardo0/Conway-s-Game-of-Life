import time
import threading
import copy
from functions import *

# Main actions
def createnewgrid():
    # Read settings
    settingsfile = open("settings.txt", "r")
    settings = settingsfile.readlines()
    settingsfile.close()
    rowdefault = int(settings[0][12:-1])
    collumndefault = int(settings[1][16:-1])
    # Choosing the size of the grid
    clear(20)
    while True:
        # Choosing the number of collumns
        collumnsize = input("Choose the number of collumns your game will have.\n(Leave it empty for the default value)\n")
        if collumnsize == "":
            # If user left it empty
            collumnsize = collumndefault
        try:
            # If it's an integer
            collumnsize = int(collumnsize)
            if collumnsize > 0:
                break
            else:
                clear(20)
                print("Please, type a number greater than 0.\n")
        except:
            # If it's not an integer
            clear(20)
            print("Please, only type whole numbers.\n")
    clear(20)
    while True:
        # Choosing the number of rows
        rowsize = input("Choose the number of rows your game will have.\n(Leave it empty for the default value)\n")
        if rowsize == "":
            # If user left it empty
            rowsize = rowdefault
        try:
            # If it's an integer
            rowsize=int(rowsize)
            if rowsize > 0:
                break
            else:
                clear(20)
                print("Please, type a number greater than 0.\n")
        except:
            # If it's not an integer
            clear(20)
            print("Please, only type whole numbers.\n")
    printgrid(collumnsize, rowsize)
def settings():
    # Read settings
    settingsfile = open("settings.txt", "r")
    settings = settingsfile.readlines()
    settingsfile.close()
    rowdefault = int(settings[0][12:-1])
    collumndefault = int(settings[1][16:-1])
    tickspeed = int(settings[2][11:-1])
    clear(20)
    while True:
        print("Settings")
        print("")
        print("Default rows: %d" % rowdefault)
        print("Default collumns: %d" % collumndefault)
        print("Tickspeed: %d ticks per second" % tickspeed)
        print("")
        print("Which setting do you want to change?")
        print("Press the number that corresponds to the action that you want.")
        print("")
        print("(1) Row default value       (2) Collumn default value")
        print("(3) Tick speed              (4) Go back")
        userselection = input("")
        if userselection == "1":
            clear(20)
            while True:
                rowdefault = input("Type the new row default value:\n")
                try:
                    rowdefault = int(rowdefault)
                    if rowdefault > 0:
                        break
                    else:
                        clear(20)
                        print("Please, type a number greater than 0.\n")
                except:
                    clear(20)
                    print("Please, only type whole numbers.\n")
            settings[0] = "rowdefault: %d\n" % rowdefault

            # Rewrites the new settings in the file
            settingsfile = open("settings.txt", "w")
            for i in range(len(settings)):
                settingsfile.write(settings[i])
            settingsfile.close()
            clear(20)
        elif userselection == "2":
            clear(20)
            while True:
                collumndefault = input("Type the new row default value:\n")
                try:
                    collumndefault = int(collumndefault)
                    if collumndefault > 0:
                        break
                    else:
                        clear(20)
                        print("Please, type a number greater than 0.\n")
                except:
                    clear(20)
                    print("Please, only type whole numbers.\n")
            settings[1] = "collumndefault: %d\n" % collumndefault

            # Rewrites the new settings in the file
            settingsfile = open("settings.txt", "w")
            for i in range(len(settings)):
                settingsfile.write(settings[i])
            settingsfile.close()
            clear(20)
        elif userselection == "3":
            clear(20)
            while True:
                tickspeed = input("Type the new tickspeed:\n")
                try:
                    tickspeed = int(tickspeed)
                    if tickspeed > 0:
                        break
                    else:
                        clear(20)
                        print("Please, type a number greater than 0.\n")
                except:
                    clear(20)
                    print("Please, only type whole numbers.\n")
            settings[2] = "tickspeed: %d\n" % tickspeed

            # Rewrites the new settings in the file
            settingsfile = open("settings.txt", "w")
            for i in range(len(settings)):
                settingsfile.write(settings[i])
            settingsfile.close()
            clear(20)
        elif userselection == "4":
            break
        else:
            clear(20)
            print("That is not an option.\n")
def rungame():
    global game_is_running
    def rungamethread():
        # Read settings
        settingsfile = open("settings.txt", "r")
        settings = settingsfile.readlines()
        settingsfile.close()
        tickspeed = int(settings[2][11:-1])

        grid, collumnsize, rowsize = readgrid()

        # Running the game indefinitely
        nextstepgrid = copy.deepcopy(grid)
        while True:
            # Setting the new grid to be the last one
            grid = nextstepgrid

            # Taking a step
            nextstepgrid = step(collumnsize, rowsize, grid, method="neighbor")
            
            # Showing the next step on the gamescreen
            printgrid(collumnsize, rowsize, nextstepgrid)

            if game_is_running == False:
                break
            # Waiting
            time.sleep(1/tickspeed)
    game_is_running = True
    thread = threading.Thread(target=rungamethread)
    thread.start()
    clear(20)
    print("Press Enter to stop the game.")
    input()
    game_is_running = False
    print("Closing game...")
    time.sleep(1)

def visualizegrid():
    gamescreenfile = open("gamescreen.txt", "r")
    gamescreen = gamescreenfile.readlines()
    gamescreenfile.close()
    clear(20)
    for i in range(len(gamescreen)):
        print(gamescreen[i][:-1])
    print("")
    input("Press Enter to continue.\n")

# Main function
def conwaysgameoflife():
    clear(20)
    while True:
        print("Welcome to Conway's Game of Life!")
        print("Press the number that corresponds to the action that you want.")
        print("")
        print("(1) Create new grid       (2) Run game")
        print("(3) Visualize grid        (4) Settings")
        print("(5) Shut down")
        userselection = input("")
        if userselection == "1":
            createnewgrid()
            clear(20)
        elif userselection == "2":
            rungame()
            clear(20)
        elif userselection == "3":
            visualizegrid()
            clear(20)
        elif userselection == "4":
            settings()
            clear(20)
        elif userselection == "5":
            clear(20)
            print("System shut down.\n")
            break
        else:
            clear(20)
            print("That is not an option.\n")

# Call of the main function
conwaysgameoflife()