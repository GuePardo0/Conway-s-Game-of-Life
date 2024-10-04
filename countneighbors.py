def countneighbors(collumn, row, collumnsize, rowsize, grid):
    number_of_neighbors = 0
    # Checking the X neighbor
    #  _____
    # |X|_|_|
    # |_|1|_|
    # |_|_|_|
    if collumn == 0:
        checkingcollumn = collumnsize-1
    else:
        checkingcollumn = collumn-1
    if row == 0:
        checkingrow = rowsize-1
    else:
        checkingrow = row-1
    if grid[checkingcollumn][checkingrow] == 1:
        number_of_neighbors+=1
    # Checking the X neighbor
    #  _____
    # |_|X|_|
    # |_|1|_|
    # |_|_|_|
    checkingcollumn = collumn
    if row == 0:
        checkingrow = rowsize-1
    else:
        checkingrow = row-1
    if grid[checkingcollumn][checkingrow] == 1:
        number_of_neighbors+=1
    # Checking the X neighbor
    #  _____
    # |_|_|X|
    # |_|1|_|
    # |_|_|_|
    if collumn == collumnsize-1:
        checkingcollumn = 0
    else:
        checkingcollumn = collumn+1
    if row == 0:
        checkingrow = rowsize-1
    else:
        checkingrow = row-1
    if grid[checkingcollumn][checkingrow] == 1:
        number_of_neighbors+=1
    # Checking the X neighbor
    #  _____
    # |_|_|_|
    # |X|1|_|
    # |_|_|_|
    if collumn == 0:
        checkingcollumn = collumnsize-1
    else:
        checkingcollumn = collumn-1
    checkingrow = row
    if grid[checkingcollumn][checkingrow] == 1:
        number_of_neighbors+=1
    # Checking the X neighbor
    #  _____
    # |_|_|_|
    # |_|1|X|
    # |_|_|_|
    if collumn == collumnsize-1:
        checkingcollumn = 0
    else:
        checkingcollumn = collumn+1
    checkingrow = row
    if grid[checkingcollumn][checkingrow] == 1:
        number_of_neighbors+=1
    # Checking the X neighbor
    #  _____
    # |_|_|_|
    # |_|1|_|
    # |X|_|_|
    if collumn == 0:
        checkingcollumn = collumnsize-1
    else:
        checkingcollumn = collumn-1
    if row == rowsize-1:
        checkingrow = 0
    else:
        checkingrow = row+1
    if grid[checkingcollumn][checkingrow] == 1:
        number_of_neighbors+=1
    # Checking the X neighbor
    #  _____
    # |_|_|_|
    # |_|1|_|
    # |_|X|_|
    checkingcollumn = collumn
    if row == rowsize-1:
        checkingrow = 0
    else:
        checkingrow = row+1
    if grid[checkingcollumn][checkingrow] == 1:
        number_of_neighbors+=1
    # Checking the X neighbor
    #  _____
    # |_|_|_|
    # |_|1|_|
    # |_|_|X|
    if collumn == collumnsize-1:
        checkingcollumn = 0
    else:
        checkingcollumn = collumn+1
    if row == rowsize-1:
        checkingrow = 0
    else:
        checkingrow = row+1
    if grid[checkingcollumn][checkingrow] == 1:
        number_of_neighbors+=1
    return number_of_neighbors
def countandlistneighbors(collumn, row, collumnsize, rowsize, grid):
    neighbors=[]
    number_of_neighbors = 0
    # Checking the X neighbor
    #  _____
    # |X|_|_|
    # |_|1|_|
    # |_|_|_|
    if collumn == 0:
        checkingcollumn = collumnsize-1
    else:
        checkingcollumn = collumn-1
    if row == 0:
        checkingrow = rowsize-1
    else:
        checkingrow = row-1
    if grid[checkingcollumn][checkingrow] == 1:
        number_of_neighbors+=1
    neighbors.append([checkingcollumn, checkingrow])
    # Checking the X neighbor
    #  _____
    # |_|X|_|
    # |_|1|_|
    # |_|_|_|
    checkingcollumn = collumn
    if row == 0:
        checkingrow = rowsize-1
    else:
        checkingrow = row-1
    if grid[checkingcollumn][checkingrow] == 1:
        number_of_neighbors+=1
    neighbors.append([checkingcollumn, checkingrow])
    # Checking the X neighbor
    #  _____
    # |_|_|X|
    # |_|1|_|
    # |_|_|_|
    if collumn == collumnsize-1:
        checkingcollumn = 0
    else:
        checkingcollumn = collumn+1
    if row == 0:
        checkingrow = rowsize-1
    else:
        checkingrow = row-1
    if grid[checkingcollumn][checkingrow] == 1:
        number_of_neighbors+=1
    neighbors.append([checkingcollumn, checkingrow])
    # Checking the X neighbor
    #  _____
    # |_|_|_|
    # |X|1|_|
    # |_|_|_|
    if collumn == 0:
        checkingcollumn = collumnsize-1
    else:
        checkingcollumn = collumn-1
    checkingrow = row
    if grid[checkingcollumn][checkingrow] == 1:
        number_of_neighbors+=1
    neighbors.append([checkingcollumn, checkingrow])
    # Checking the X neighbor
    #  _____
    # |_|_|_|
    # |_|1|X|
    # |_|_|_|
    if collumn == collumnsize-1:
        checkingcollumn = 0
    else:
        checkingcollumn = collumn+1
    checkingrow = row
    if grid[checkingcollumn][checkingrow] == 1:
        number_of_neighbors+=1
    neighbors.append([checkingcollumn, checkingrow])
    # Checking the X neighbor
    #  _____
    # |_|_|_|
    # |_|1|_|
    # |X|_|_|
    if collumn == 0:
        checkingcollumn = collumnsize-1
    else:
        checkingcollumn = collumn-1
    if row == rowsize-1:
        checkingrow = 0
    else:
        checkingrow = row+1
    if grid[checkingcollumn][checkingrow] == 1:
        number_of_neighbors+=1
    neighbors.append([checkingcollumn, checkingrow])
    # Checking the X neighbor
    #  _____
    # |_|_|_|
    # |_|1|_|
    # |_|X|_|
    checkingcollumn = collumn
    if row == rowsize-1:
        checkingrow = 0
    else:
        checkingrow = row+1
    if grid[checkingcollumn][checkingrow] == 1:
        number_of_neighbors+=1
    neighbors.append([checkingcollumn, checkingrow])
    # Checking the X neighbor
    #  _____
    # |_|_|_|
    # |_|1|_|
    # |_|_|X|
    if collumn == collumnsize-1:
        checkingcollumn = 0
    else:
        checkingcollumn = collumn+1
    if row == rowsize-1:
        checkingrow = 0
    else:
        checkingrow = row+1
    if grid[checkingcollumn][checkingrow] == 1:
        number_of_neighbors+=1
    neighbors.append([checkingcollumn, checkingrow])
    return number_of_neighbors, neighbors