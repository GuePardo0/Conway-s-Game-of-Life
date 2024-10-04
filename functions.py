from countneighbors import *

# Function declarations
def clear(n):
    for i in range(n):
        print("\n")
def readgrid():
    gamescreenfile = open("gamescreen.txt", "r")
    gamescreen = gamescreenfile.readlines()
    gamescreenfile.close()
    collumnsize = int((len(gamescreen[1])-2)/2)
    rowsize = len(gamescreen)-1
    grid = []
    for i in range(collumnsize):
        collumn = []
        for j in range(rowsize):
            collumn.append(gamescreen[j+1][i*2+1])
        grid.append(collumn)
    return grid, collumnsize, rowsize
def printgrid(collumnsize, rowsize, grid=""):
    """ Currently having a problem with optimizing the printing of the grid.
    Printing it in a file is slow, but still haven't found a better method """

    # If the grid is not given, make an empty grid
    if grid == "":
        grid = []
        for i in range(collumnsize):
            emptycollumn = []
            for j in range(rowsize):
                emptycollumn.append("_")
            grid.append(emptycollumn)

    gamescreenfile = open("gamescreen.txt", "w")

    # Printing each line
    if rowsize != 0 and collumnsize != 0:
        # First line
        gamescreenfile.write(" _")
        for i in range(collumnsize-1):
            gamescreenfile.write("__")
        gamescreenfile.write("\n")
        # Rest of the lines
        for j in range(rowsize):
            for i in range(collumnsize):
                gamescreenfile.write("|%s" % grid[i][j])
            gamescreenfile.write("|\n")

    gamescreenfile.close()
def step(collumnsize, rowsize, grid, method="neighbor"):
    # Create new empty grid
    nextstepgrid = []
    for i in range(collumnsize):
        emptycollumn = []
        for j in range(rowsize):
            emptycollumn.append("_")
        nextstepgrid.append(emptycollumn)

    """ This method calculates the number of neighbors of the alive tiles
    and then for the their neighboring tiles
    (It is faster for games with big grids and few alive cells) """
    if method == "neighbor":
        # Calculating the next state of each alive tile and putting its neighbors into a list
        # Going through all tiles
        neighbors = []
        for collumn in range(collumnsize):
            for row in range(rowsize):
                # Checking only alive cells
                if grid[collumn][row] == "X":
                    # Cell is alive
                    # Counting the number of alive neighbors
                    number_of_neighbors, current_neighbors = countandlistneighbors(collumn, row, collumnsize, rowsize, grid)

                    # Putting all neighbors into the neighbors list
                    for i in range(8):
                        if not current_neighbors[i] in neighbors:
                            neighbors.append(current_neighbors[i])
                    
                    # If it has two or three alive neighbors, it lives
                    # Else, it dies
                    if number_of_neighbors >= 2 and number_of_neighbors <= 3:
                        nextstepgrid[collumn][row] = "X"

        # Calculating the next state of each tile neighboring an alive tile
        # Going through all neighboring tiles
        for i in range(len(neighbors)):
            # Counting the number of alive neighbors
            number_of_neighbors = countneighbors(neighbors[i][0], neighbors[i][1], collumnsize, rowsize, grid)

            # Creating the next step
            if grid[neighbors[i][0]][neighbors[i][1]] == "X":
                # Cell is alive
                # If it has two or three alive neighbors, it lives
                # Else, it dies
                if number_of_neighbors >= 2 and number_of_neighbors <= 3:
                    nextstepgrid[neighbors[i][0]][neighbors[i][1]] = "X"
            else:
                # Cell is dead
                # If it has three alive neighbors, it lives
                # Else, it dies
                if number_of_neighbors == 3:
                    nextstepgrid[neighbors[i][0]][neighbors[i][1]] = "X"
    
    """ This method calculates the number of neighbors of each tile
    (It is faster for games with grids full of alive cells) """
    if method == "all":
        # Calculating the next state of each tile
        # Going through all tiles
        for collumn in range(collumnsize):
            for row in range(rowsize):
                # Counting the number of alive neighbors
                number_of_neighbors = countneighbors(collumn, row, collumnsize, rowsize, grid)[0]

                # Creating the next step
                if grid[collumn][row] == "X":
                    # Cell is alive
                    # If it has two or three alive neighbors, it lives
                    # Else, it dies
                    if number_of_neighbors >= 2 and number_of_neighbors <= 3:
                        nextstepgrid[collumn][row] = "X"
                else:
                    # Cell is dead
                    # If it has three alive neighbors, it lives
                    # Else, it dies
                    if number_of_neighbors == 3:
                        nextstepgrid[collumn][row] = "X"
    return nextstepgrid