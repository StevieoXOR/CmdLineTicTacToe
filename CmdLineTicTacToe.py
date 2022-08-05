TTTBoard = [
    ['`','`','`','`'],
    ['`','`','`','`'],
    ['`','`','`','`'],
    ['`','`','`','`']
]

print('INFO: Upper left is row0,col0. Bottom right is ', end='')
print('row' + str(len(TTTBoard)-1) + ',col' + str(len(TTTBoard[0])-1) + '.')

winnerExists = False
isPlayerOnesTurn = False
while not winnerExists: #while nobodyHasWonTheGameYet
    isPlayerOnesTurn = not isPlayerOnesTurn #Switch players
    if isPlayerOnesTurn:
        print('Player 1 (X)')
    else:
        print('Player 2 (O)')

    #Get input coordinate and modify the board
    coords = input('Enter the 2D coordinates of the square you would like to mark as yours (e.g. row2,col1): ')
    while not (len(coords)>2
               and coords[0].isdigit() and coords[1]==',' and coords[2].isdigit()   #stringIsInFormat: digit,digit
               and int(coords[0])<len(TTTBoard)      # xCoord<numRows    DO NOT USE .count() BECAUSE IT FINDS MATCHES, NOT LENGTH
               and int(coords[2])<len(TTTBoard[0])   # yCoord<numColumns
               and TTTBoard[int(coords[0])][int(coords[2])] == '`'):    #TTTBoard[x][y]=='`'  spotHasNotBeenClaimed
        #Specific error messages
        if not (coords[0].isdigit() and coords[1]==',' and coords[2].isdigit()):
            print('Coordinate must be formatted like 2,2 or 0,5')
        elif int(coords[0])>=len(TTTBoard):                  #elif instead of if because of invalid coordinates crashing the program
            print('Invalid number of rows')
        elif int(coords[2])>=len(TTTBoard[0]):               #elif instead of if because of invalid coordinates crashing the program
            print('Invalid number of columns')
        elif TTTBoard[int(coords[0])][int(coords[2])] != '`':#elif instead of if because of invalid coordinates crashing the program
            print('Spot has already been claimed')
        coords = input('Invalid Coordinate, enter a 2D coordinate: ')    #coords is a string because input always yields a string
    x = int(coords[0])
    y = int(coords[2])
    if isPlayerOnesTurn:
        TTTBoard[x][y] = 'X'
    else:
        TTTBoard[x][y] = 'O'
    
    #Draw game board
    rowNum = colNum = 0
    print('r\\c ',end='')
    for colElement in TTTBoard[0]:
        print(str(colNum)+' ',end='')
        colNum += 1
    print()
    for row in TTTBoard:
        print( str(rowNum)+' | ', end='' )
        for colElement in row:
            print( str(colElement)+' ', end='' )
        print('|')
        rowNum += 1
    print()


    #Check for winner
    #Check each row to see if entire row is all Xs or all Os
    for row in TTTBoard:    #row is a list, not an index number
        #Check each row to see if entire row is all Xs or all Os
        if row.count('X')==len(row):    #if thereAreAsManyXsAsSpotsInTheRow
            winnerExists = True
            print('Player 1 (X) wins!')
        elif row.count('O')==len(row):    #if thereAreAsManyOsAsSpotsInTheRow
            winnerExists = True
            print('Player 2 (O) wins!')
    
    #Check each column to see if entire column is all Xs or all Os
    #Check 1 specific column from each row. E.g. row0col0, row1col0, row2,col0, row3col0
    isAllXsInAtLeastOneColumn = False
    isAllOsInAtLeastOneColumn = False
    numCol = 0
    while numCol < len( TTTBoard[0] ):  #For each column in row0
        isAllXsInCurrColumn = True
        isAllOsInCurrColumn = True
        numRow = 0  #Reset numRows back to 0 after inner loop finishes
        while numRow < len(TTTBoard):   #While rowNum < numRows
            if TTTBoard[numRow][numCol]!='X':
                isAllXsInCurrColumn = False
            if TTTBoard[numRow][numCol]!='O':
                isAllOsInCurrColumn = False
            #print('row',numRow,' col',numCol,' ', end='')
            #print('isAllXsInCurrColumn',isAllXsInCurrColumn,' ', end='')
            #print('isAllOsInCurrColumn',isAllOsInCurrColumn)
            numRow += 1
        if isAllXsInCurrColumn:
            isAllXsInAtLeastOneColumn = True
            print('Player 1 (X) wins!')
            exit(0) #Quit program
        elif isAllOsInCurrColumn:
            isAllOsInAtLeastOneColumn = True
            print('Player 2 (O) wins!')
            exit(0) #Quit program
        #print('isAllXsInAtLeastOneColumn',isAllXsInAtLeastOneColumn,' ', end='')
        #print('isAllOsInAtLeastOneColumn',isAllOsInAtLeastOneColumn)
        numCol += 1
    
    #Check each diagonal to see if entire diagonal is all Xs or all Os
    if len( TTTBoard[0] ) != len( TTTBoard ):   # numCols != numRows
        print('Number of columns does not equal number of rows. Cannot check for diagonal winners.')
        exit(0)
    spotID = 0
    isAllXsInMainDiagonal = isAllOsInMainDiagonal = True
    while spotID < len( TTTBoard ):  #For each square in col0. Doesn't matter if I use cols or rows because #cols=#rows
        if TTTBoard[spotID][spotID]!='X':
            isAllXsInMainDiagonal = False
        if TTTBoard[spotID][spotID]!='O':
            isAllOsInMainDiagonal = False
        #print('row',spotID,' col',spotID,' ', end='')
        #print('isAllXsInMainDiagonal',isAllXsInMainDiagonal,' ', end='')
        #print('isAllOsInMainDiagonal',isAllOsInMainDiagonal)
        spotID += 1
    if isAllXsInMainDiagonal:
        print('Player 1 (X) wins!')
        exit(0) #Quit program
    elif isAllOsInMainDiagonal:
        print('Player 2 (O) wins!')
        exit(0) #Quit program
    
    rowNum = 0
    colNum = len( TTTBoard[0] )-1  #Index of the last column in the list
    isAllXsInMinorDiagonal = isAllOsInMinorDiagonal = True
    while colNum >= 0:  #For each square in col0. Doesn't matter if I use cols or rows because #cols=#rows
        if TTTBoard[rowNum][colNum]!='X':
            isAllXsInMinorDiagonal = False
        if TTTBoard[rowNum][colNum]!='O':
            isAllOsInMinorDiagonal = False
        #print('row',rowNum,' col',colNum,' ', end='')
        #print('isAllXsInMinorDiagonal',isAllXsInMinorDiagonal,' ', end='')
        #print('isAllOsInMinorDiagonal',isAllOsInMinorDiagonal)
        rowNum += 1
        colNum -= 1
    if isAllXsInMinorDiagonal:
        print('Player 1 (X) wins!')
        exit(0) #Quit program
    elif isAllOsInMinorDiagonal:
        print('Player 2 (O) wins!')
        exit(0) #Quit program