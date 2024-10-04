import threading
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
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
    # Reading settings
    settingsfile = open("settings.txt", "r")
    settings = settingsfile.readlines()
    settingsfile.close()
    tickspeed = int(settings[2][11:-1])

    # Reading the initial grid
    grid, collumnsize, rowsize = readgrid()

    # Running the game and showing it with matplotlib
    def update(frame):
        nonlocal grid
        grid = step(collumnsize, rowsize, grid, method="neighbor")
        mat.set_data(grid)
        return [mat]
    fig, ax = plt.subplots()
    cmap = ListedColormap(['#F4F4F4', 'black'])  # Adjust colors here as needed
    mat = ax.matshow(grid, cmap=cmap)
    plt.axis('off')
    animation = FuncAnimation(fig, update, frames=1, interval=1000/tickspeed, blit=True)
    
    # Waiting for user input to stop the game
    def stopgame():
        clear(20)
        input("Press Enter to stop the game.\n")
        print("Closing game...")
        plt.close(fig)
    thread = threading.Thread(target=stopgame)
    thread.start()

    plt.show()

def visualizegrid():
    grid, collumnsize, rowsize = readgrid()
    clear(20)
    row=""
    # First line
    row+=" _"
    for i in range(collumnsize-1):
        row+="__"
    print(row)
    # Rest of the lines
    for j in range(rowsize):
        row=""
        for i in range(collumnsize):
            row+="|%s" % grid[i][j]
        row+="|"
        print(row)
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