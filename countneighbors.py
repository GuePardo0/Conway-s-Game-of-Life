def countneighbors(collumn, row, collumnsize, rowsize, grid):
    number_of_neighbors = 0
    # Checking the N neighbor
    #  _____
    # |N|_|_|
    # |_|X|_|
    # |_|_|_|
    if collumn == 0:
        checkingcollumn = collumnsize-1
    else:
        checkingcollumn = collumn-1
    if row == 0:
        checkingrow = rowsize-1
    else:
        checkingrow = row-1
    if grid[checkingcollumn][checkingrow] == "X":
        number_of_neighbors+=1
    # Checking the N neighbor
    #  _____
    # |_|N|_|
    # |_|X|_|
    # |_|_|_|
    checkingcollumn = collumn
    if row == 0:
        checkingrow = rowsize-1
    else:
        checkingrow = row-1
    if grid[checkingcollumn][checkingrow] == "X":
        number_of_neighbors+=1
    # Checking the N neighbor
    #  _____
    # |_|_|N|
    # |_|X|_|
    # |_|_|_|
    if collumn == collumnsize-1:
        checkingcollumn = 0
    else:
        checkingcollumn = collumn+1
    if row == 0:
        checkingrow = rowsize-1
    else:
        checkingrow = row-1
    if grid[checkingcollumn][checkingrow] == "X":
        number_of_neighbors+=1
    # Checking the N neighbor
    #  _____
    # |_|_|_|
    # |N|X|_|
    # |_|_|_|
    if collumn == 0:
        checkingcollumn = collumnsize-1
    else:
        checkingcollumn = collumn-1
    checkingrow = row
    if grid[checkingcollumn][checkingrow] == "X":
        number_of_neighbors+=1
    # Checking the N neighbor
    #  _____
    # |_|_|_|
    # |_|X|N|
    # |_|_|_|
    if collumn == collumnsize-1:
        checkingcollumn = 0
    else:
        checkingcollumn = collumn+1
    checkingrow = row
    if grid[checkingcollumn][checkingrow] == "X":
        number_of_neighbors+=1
    # Checking the N neighbor
    #  _____
    # |_|_|_|
    # |_|X|_|
    # |N|_|_|
    if collumn == 0:
        checkingcollumn = collumnsize-1
    else:
        checkingcollumn = collumn-1
    if row == rowsize-1:
        checkingrow = 0
    else:
        checkingrow = row+1
    if grid[checkingcollumn][checkingrow] == "X":
        number_of_neighbors+=1
    # Checking the N neighbor
    #  _____
    # |_|_|_|
    # |_|X|_|
    # |_|N|_|
    checkingcollumn = collumn
    if row == rowsize-1:
        checkingrow = 0
    else:
        checkingrow = row+1
    if grid[checkingcollumn][checkingrow] == "X":
        number_of_neighbors+=1
    # Checking the N neighbor
    #  _____
    # |_|_|_|
    # |_|X|_|
    # |_|_|N|
    if collumn == collumnsize-1:
        checkingcollumn = 0
    else:
        checkingcollumn = collumn+1
    if row == rowsize-1:
        checkingrow = 0
    else:
        checkingrow = row+1
    if grid[checkingcollumn][checkingrow] == "X":
        number_of_neighbors+=1
    return number_of_neighbors
def countandlistneighbors(collumn, row, collumnsize, rowsize, grid):
    neighbors=[]
    number_of_neighbors = 0
    # Checking the N neighbor
    #  _____
    # |N|_|_|
    # |_|X|_|
    # |_|_|_|
    if collumn == 0:
        checkingcollumn = collumnsize-1
    else:
        checkingcollumn = collumn-1
    if row == 0:
        checkingrow = rowsize-1
    else:
        checkingrow = row-1
    if grid[checkingcollumn][checkingrow] == "X":
        number_of_neighbors+=1
    neighbors.append([checkingcollumn, checkingrow])
    # Checking the N neighbor
    #  _____
    # |_|N|_|
    # |_|X|_|
    # |_|_|_|
    checkingcollumn = collumn
    if row == 0:
        checkingrow = rowsize-1
    else:
        checkingrow = row-1
    if grid[checkingcollumn][checkingrow] == "X":
        number_of_neighbors+=1
    neighbors.append([checkingcollumn, checkingrow])
    # Checking the N neighbor
    #  _____
    # |_|_|N|
    # |_|X|_|
    # |_|_|_|
    if collumn == collumnsize-1:
        checkingcollumn = 0
    else:
        checkingcollumn = collumn+1
    if row == 0:
        checkingrow = rowsize-1
    else:
        checkingrow = row-1
    if grid[checkingcollumn][checkingrow] == "X":
        number_of_neighbors+=1
    neighbors.append([checkingcollumn, checkingrow])
    # Checking the N neighbor
    #  _____
    # |_|_|_|
    # |N|X|_|
    # |_|_|_|
    if collumn == 0:
        checkingcollumn = collumnsize-1
    else:
        checkingcollumn = collumn-1
    checkingrow = row
    if grid[checkingcollumn][checkingrow] == "X":
        number_of_neighbors+=1
    neighbors.append([checkingcollumn, checkingrow])
    # Checking the N neighbor
    #  _____
    # |_|_|_|
    # |_|X|N|
    # |_|_|_|
    if collumn == collumnsize-1:
        checkingcollumn = 0
    else:
        checkingcollumn = collumn+1
    checkingrow = row
    if grid[checkingcollumn][checkingrow] == "X":
        number_of_neighbors+=1
    neighbors.append([checkingcollumn, checkingrow])
    # Checking the N neighbor
    #  _____
    # |_|_|_|
    # |_|X|_|
    # |N|_|_|
    if collumn == 0:
        checkingcollumn = collumnsize-1
    else:
        checkingcollumn = collumn-1
    if row == rowsize-1:
        checkingrow = 0
    else:
        checkingrow = row+1
    if grid[checkingcollumn][checkingrow] == "X":
        number_of_neighbors+=1
    neighbors.append([checkingcollumn, checkingrow])
    # Checking the N neighbor
    #  _____
    # |_|_|_|
    # |_|X|_|
    # |_|N|_|
    checkingcollumn = collumn
    if row == rowsize-1:
        checkingrow = 0
    else:
        checkingrow = row+1
    if grid[checkingcollumn][checkingrow] == "X":
        number_of_neighbors+=1
    neighbors.append([checkingcollumn, checkingrow])
    # Checking the N neighbor
    #  _____
    # |_|_|_|
    # |_|X|_|
    # |_|_|N|
    if collumn == collumnsize-1:
        checkingcollumn = 0
    else:
        checkingcollumn = collumn+1
    if row == rowsize-1:
        checkingrow = 0
    else:
        checkingrow = row+1
    if grid[checkingcollumn][checkingrow] == "X":
        number_of_neighbors+=1
    neighbors.append([checkingcollumn, checkingrow])
    return number_of_neighbors, neighbors