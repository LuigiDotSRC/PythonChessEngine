pieces = {
    #position of all pieces
    "bPawn" : ["a7","b7","c7","d7","e7","f7","g7","h7"],
    "bRook" : ["a8","h8"],
    "bKnight" : ["b8","g8"],
    "bBishop" : ["c8","f8"],
    "bQueen" : ["d8"],
    "bKing" : ["e8"],

    "wPawn" : ["a2","b2","c2","d2","e2","f2","g2","h2"],
    "wRook" : ["a1","h1"],
    "wKnight" : ["b1","g1"],
    "wBishop" : ["c1","f1"],
    "wQueen" : ["d1"],
    "wKing" : ["e1"],
}

#testboard
pieces = {
    "bPawn" : ["f3","d3","e2","a6"],
    "wPawn" : ["b6"],
    "wRook" : ["a1","b1"],
    "wBishop" : ["a2"],
    "wKnight" : ["f5"],
    "wQueen" : ["a5"],
    "wKing" : ["a3"]
}

def getPos(allPos, position):
    record = allPos.items()
    for i in record:
        for j in i[1]:
            if(j == position):
                return i[0]

    return ""

def drawBoard(allPos):
    row = [1,2,3,4,5,6,7,8]
    colmn = ["a","b","c","d","e","f","g","h"]
    board = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []     
    ]
    for i in range(8):
        for j in range(8):
            target = board[i]
            searchRow = row[i]
            searchColmn = colmn[j]
            pos = searchColmn + str(searchRow)

            unit = getPos(allPos,pos)
            disp = ""
    
            if(unit == "wPawn"):
                disp = "♙"
            elif(unit == "wRook"):
                disp = "♖"
            elif(unit == "wKnight"):
                disp = "♘"
            elif(unit == "wBishop"):
                disp = "♗"
            elif(unit == "wQueen"):
                disp = "♕"
            elif(unit == "wKing"):
                disp = "♔"
                
            elif(unit == "bPawn"):
                disp = "♟︎"
            elif(unit == "bRook"):
                disp = "♜"
            elif(unit == "bKnight"):
                disp = "♞"
            elif(unit == "bBishop"):
                disp = "♝"
            elif(unit == "bQueen"):
                disp = "♛"
            elif(unit == "bKing"):
                disp = "♚"

            else:
                white = ["a2","a4","a6","a8","b1","b3","b5","b7","c2","c4","c6","c8",
                                 "d1","d3","d5","d7","e2","e4","e6","e8","f1","f3","f5","f7",
                                 "g2","g4","g6","g8","h1","h3","h5","h7"]

                '''
                black = ["a1","a3","a5","a7","b2","b4","b6","b8","c1","c3","c5","c7",
                                 "d2","d4","d6","d8","e1","e3","e5","e7","f2","f4","f6","f8",
                                 "g1","g3","g5","g7","h2","h4","h6","h8"]
                '''
            
                if(searchColmn+str(searchRow) in white):
                    disp = "□" #⬜
                else:
                    disp = "■" #⬛

            target.append(disp)

    for i in range(8):
        resultString = str(8-i) + " "
        for j in range(8):
            resultString += board[7-i][j] + " "
        print(resultString)
    print("  a b c d e f g h")

def vertical(allPos,initPos,paces):
    result = []
    blockedSpace = ""
    if(int(initPos[1:]) + paces > 8 or int(initPos[1:]) + paces < 1):
        return result 
    
    if(paces < 0):
        for i in range(paces * -1):
            rowCalculation = int(initPos[1:]) - i - 1
            position = initPos[:1] + str(rowCalculation)
    
            if(getPos(pieces,position) != ""):
                blockedSpace = position
                break
            result.append(position)

    else:
        for i in range(paces):
            rowCalculation = int(initPos[1:]) + i + 1
            position = initPos[:1] + str(rowCalculation)
    
            if(getPos(pieces,position) != ""):
                blockedSpace = position
                break
            result.append(position)
        
    return result,blockedSpace

def horizontal(allPos,initPos,paces):
    result = []
    blockedSpace = ""
    colmns = ["a","b","c","d","e","f","g","h"]
    targetcolmn = initPos[:1]

    index = colmns.index(targetcolmn)
    if(index + paces > 7 or index + paces < 0):
        return result

    if(paces < 0):
        for i in range(paces * -1):
            colmnCalculation = index - i - 1
            position = colmns[colmnCalculation] + initPos[1:]

            if(getPos(pieces,position) != ""):
                blockedSpace = position
                break
            result.append(position)

    else:
        for i in range(paces):
            colmnCalculation = index + i + 1
            position = colmns[colmnCalculation] + initPos[1:]
    
            if(getPos(pieces,position) != ""):
                blockedSpace = position
                break
            result.append(position)

    return result,blockedSpace

def diagonal(allPos,initPos,paces,dir):
    result = []
    blockedSpace = ""
    colmns = ["a","b","c","d","e","f","g","h"]
    targetcolmn = initPos[:1]
    targetrow = initPos[1:]
    WEST = "W"
    EAST = "E"
    index = colmns.index(targetcolmn)

    if(paces < 0):
        if(dir == WEST):
            for i in range(paces * -1):
                
                colmnCalculation = index - i - 1

                if(colmnCalculation < 0):
                    break
                    
                rowCalculation = int(targetrow) - i - 1

                if(rowCalculation < 1):
                    break
                    
                position = colmns[colmnCalculation] + str(rowCalculation)
                
                if(getPos(pieces,position) != ""):
                    blockedSpace = position
                    break
            
                result.append(position)
                
        elif(dir == EAST):
            for i in range(paces * -1):
                
                colmnCalculation = index + i + 1

                if(colmnCalculation > 7):
                    break
                    
                rowCalculation = int(targetrow) - i - 1

                if(rowCalculation < 1):
                    break
                    
                position = colmns[colmnCalculation] + str(rowCalculation)
                
                if(getPos(pieces,position) != ""):
                    blockedSpace = position
                    break
            
                result.append(position)
                
    else:
        if(dir == WEST):
            for i in range(paces):

                colmnCalculation = index - i - 1
                
                if(colmnCalculation < 0):
                    break
                    
                rowCalculation = int(targetrow) + i + 1

                if(rowCalculation > 8):
                    break
                    
                position = colmns[colmnCalculation] + str(rowCalculation)
                
                if(getPos(pieces,position) != ""):
                    blockedSpace = position
                    break
            
                result.append(position)

        elif(dir == EAST):
            for i in range(paces):
                
                colmnCalculation = index + i + 1

                if(colmnCalculation > 7):
                    break
                
                rowCalculation = int(targetrow) + i + 1

                if(rowCalculation > 8):
                    break
                    
                position = colmns[colmnCalculation] + str(rowCalculation)
                
                if(getPos(pieces,position) != ""):
                    blockedSpace = position
                    break
            
                result.append(position)
                
    return result,blockedSpace

def Lsearch(initpos):
    targets = []
    result = []
    alph = ["a","b","c","d","e","f","g","h"]
    currentRow = int(initpos[1:])
    currentCol = alph.index(initpos[:1])

    #top left 2 squares:
    targets.append([currentCol - 2, currentRow + 1])
    targets.append([currentCol - 1, currentRow + 2])

    #bot left 2 squares:
    targets.append([currentCol - 2, currentRow - 1])
    targets.append([currentCol - 1, currentRow - 2])

    #top right 2 squares:
    targets.append([currentCol + 2, currentRow + 1])
    targets.append([currentCol + 1, currentRow + 2])

    #bot right 2 squares:
    targets.append([currentCol + 2, currentRow - 1])
    targets.append([currentCol + 1, currentRow - 2])

    #append valid targets to result with proper syntax:
    for i in targets:
        if( (i[0] >= 0 and i[0] <= 7) and (i[1] >= 1 and i[1] <= 8) ):
            result.append(alph[i[0]] + str(i[1]))

    return result

def move(pos1,pos2):
    if(getPos(pieces,pos2) != ""):
        unitRemoved = getPos(pieces,pos2)
        pieces.get(unitRemoved).pop(pieces.get(unitRemoved).index(pos2))
    
    key = getPos(pieces,pos1)
    pieces.get(key).pop(pieces.get(key).index(pos1))
    pieces.get(key).append(pos2)

def relativepos(pos,dir):

    if(dir == "vert"):
        workingpos = int(pos[1:])
        upperbound = 8-workingpos
        lowerbound = abs(1-workingpos)
        return upperbound,lowerbound
    
    elif(dir == "horiz"):
        #upper: right lower: left
        alph = ["a","b","c","d","e","f","g","h"]
        workingpos = alph.index(pos[:1]) + 1
        upperbound = 8-workingpos
        lowerbound = abs(1-workingpos)
        return upperbound,lowerbound
    
    elif(dir == "nwse"):

        alph = ["a","b","c","d","e","f","g","h"]
        workingpos = [ alph.index(pos[:1]) , int(pos[1:]) ]
        count = 0
        while(True):
            if(workingpos[0] >= 1 and workingpos[1] <= 7):
                count += 1
                workingpos[0] -= 1
                workingpos[1] += 1
            else:
                break
        
        nw = count

        workingpos = [ alph.index(pos[:1]) , int(pos[1:]) ]
        count = 0
        while(True):
            if(workingpos[0] <= 7 and workingpos[1] > 1):
                count += 1
                workingpos[0] += 1
                workingpos[1] -= 1
            else:
                break
        
        se = count
        return [nw,se]
    
    elif(dir == "nesw"):

        alph = ["a","b","c","d","e","f","g","h"]
        workingpos = [ alph.index(pos[:1]) , int(pos[1:]) ]
        count = 0
        while(True):
            if(workingpos[0] < 7 and workingpos[1] <= 7):
                count += 1
                workingpos[0] += 1
                workingpos[1] += 1
            else:
                break
        
        ne = count

        workingpos = [ alph.index(pos[:1]) , int(pos[1:]) ]
        count = 0
        while(True):
            if(workingpos[0] >= 1 and workingpos[1] > 1):
                count += 1
                workingpos[0] -= 1
                workingpos[1] -= 1
            else:
                break
        
        sw = count
        return [ne,sw]

def movegenPawn(pos):
    result = []
    speed = 1
    startingposW = ["a2","b2","c2","d2","e2","f2","g2","h2"]
    startingposB = ["a7","b7","c7","d7","e7","f7","g7","h7"]
        
    if(getPos(pieces,pos)[:1] == "w"):            
        if(pos in startingposW):
            speed = 2
            
        for i in vertical(pieces,pos,speed)[0]:
            result.append(i)

        if(len(diagonal(pieces,pos,speed,"W")[1]) != 0):
            for j in diagonal(pieces,pos,speed,"W")[1]:
                if(getPos(pieces,j)[:1 == "b"]):
                    result.append(diagonal(pieces,pos,speed,"W")[1])

        if(len(diagonal(pieces,pos,speed,"E")[1]) != 0):
            for j in diagonal(pieces,pos,speed,"E")[1]:
                if(getPos(pieces,j)[:1 == "b"]):
                    result.append(diagonal(pieces,pos,speed,"E")[1])

    else:
        speed = -1
        if(pos in startingposB):
            speed = -2
            
        for i in vertical(pieces,pos,speed)[0]:
            result.append(i)

        if(len(diagonal(pieces,pos,speed,"W")[1]) != 0):
            for j in diagonal(pieces,pos,speed,"W")[1]:
                if(getPos(pieces,j)[:1 == "w"]):
                    result.append(diagonal(pieces,pos,speed,"W")[1])

        if(len(diagonal(pieces,pos,speed,"E")[1]) != 0):
            for j in diagonal(pieces,pos,speed,"E")[1]:
                if(getPos(pieces,j)[:1 == "w"]):
                    result.append(diagonal(pieces,pos,speed,"E")[1])
    
    return result

def movegenRook(pos):
    result = []
    if(getPos(pieces,pos)[:1] == "w"):   
        relativeV = relativepos(pos,"vert")         
        moves = vertical(pieces,pos,-1*relativeV[1])

        for i in moves[0]:
            result.append(i)
                
        if(len(moves[1]) != 0):
            if(getPos(pieces,moves[1])[:1] == "b"):
                result.append(moves[1])

        moves = vertical(pieces,pos,relativeV[0])

        for i in moves[0]:
            result.append(i)
                
        if(len(moves[1]) != 0):
            if(getPos(pieces,moves[1])[:1] == "b"):
                result.append(moves[1])

        #--------------------------

        relativeH = relativepos(pos,"horiz")         
        moves = horizontal(pieces,pos,-1*relativeH[1])

        for i in moves[0]:
            result.append(i)
                
        if(len(moves[1]) != 0):
            if(getPos(pieces,moves[1])[:1] == "b"):
                result.append(moves[1])

        moves = horizontal(pieces,pos,relativeH[0])

        for i in moves[0]:
            result.append(i)
                
        if(len(moves[1]) != 0):
            if(getPos(pieces,moves[1])[:1] == "b"):
                result.append(moves[1])

    else:
        relativeV = relativepos(pos,"vert")         
        moves = vertical(pieces,pos,-1*relativeV[1])

        for i in moves[0]:
            result.append(i)
                
        if(len(moves[1]) != 0):
            if(getPos(pieces,moves[1])[:1] == "w"):
                result.append(moves[1])

        moves = vertical(pieces,pos,relativeV[0])

        for i in moves[0]:
            result.append(i)
                
        if(len(moves[1]) != 0):
            if(getPos(pieces,moves[1])[:1] == "w"):
                result.append(moves[1])

        #--------------------------

        relativeH = relativepos(pos,"horiz")         
        moves = horizontal(pieces,pos,-1*relativeH[1])

        for i in moves[0]:
            result.append(i)
                
        if(len(moves[1]) != 0):
            if(getPos(pieces,moves[1])[:1] == "w"):
                result.append(moves[1])

        moves = horizontal(pieces,pos,relativeH[0])

        for i in moves[0]:
            result.append(i)
                
        if(len(moves[1]) != 0):
            if(getPos(pieces,moves[1])[:1] == "w"):
                result.append(moves[1])
    return result

def movegenBishop(pos):
    result = []
    if(getPos(pieces,pos)[:1] == "w"):     
        relativeD = relativepos(pos,"nwse")         
        moves = diagonal(pieces,pos,relativeD[0],"W")
        
        for i in moves[0]:
            result.append(i)

        if(len(moves[1]) != 0):
            if(getPos(pieces,moves[1])[:1] == "b"):
                result.append(moves[1])

        moves = diagonal(pieces,pos,-1*relativeD[1],"E")
        
        for i in moves[0]:
            result.append(i)

        if(len(moves[1]) != 0):
            if(getPos(pieces,moves[1])[:1] == "b"):
                result.append(moves[1])

        #--------

        relativeD = relativepos(pos,"nesw")         
        moves = diagonal(pieces,pos,relativeD[0],"E")
        
        for i in moves[0]:
            result.append(i)

        if(len(moves[1]) != 0):
            if(getPos(pieces,moves[1])[:1] == "b"):
                result.append(moves[1])

        moves = diagonal(pieces,pos,-1*relativeD[1],"W")
            
        for i in moves[0]:
            result.append(i)

        if(len(moves[1]) != 0):
            if(getPos(pieces,moves[1])[:1] == "b"):
                result.append(moves[1])
    else:
        relativeD = relativepos(pos,"nwse")         
        moves = diagonal(pieces,pos,relativeD[0],"W")
        
        for i in moves[0]:
            result.append(i)

        if(len(moves[1]) != 0):
            if(getPos(pieces,moves[1])[:1] == "w"):
                result.append(moves[1])

        moves = diagonal(pieces,pos,-1*relativeD[1],"E")
        
        for i in moves[0]:
            result.append(i)

        if(len(moves[1]) != 0):
            if(getPos(pieces,moves[1])[:1] == "w"):
                result.append(moves[1])

        #--------

        relativeD = relativepos(pos,"nesw")         
        moves = diagonal(pieces,pos,relativeD[0],"E")
        
        for i in moves[0]:
            result.append(i)

        if(len(moves[1]) != 0):
            if(getPos(pieces,moves[1])[:1] == "w"):
                result.append(moves[1])

        moves = diagonal(pieces,pos,-1*relativeD[1],"W")
        
        for i in moves[0]:
            result.append(i)

        if(len(moves[1]) != 0):
            if(getPos(pieces,moves[1])[:1] == "w"):
                result.append(moves[1])

    return result

def movegenKnight(pos):
    result = []
    if(getPos(pieces,pos)[:1] == "w"):
        Lmove = Lsearch(pos)
        for i in Lmove:
            if(getPos(pieces,i)[:1] != "w"):
                result.append(i)
    else:
        Lmove = Lsearch(pos)
        for i in Lmove:
            if(getPos(pieces,i)[:1] != "b"):
                result.append(i)
    return result

def movegenKing(pos):
    moves = []
    result = []
    alph = ["a","b","c","d","e","f","g","h"]
    currentRow = pos[1:]
    currentCol = pos[:1]

    moves.append(vertical(pieces,pos,1))
    moves.append(vertical(pieces,pos,-1))
    moves.append(horizontal(pieces,pos,1))
    moves.append(horizontal(pieces,pos,-1))
    moves.append(diagonal(pieces,pos,1,"W"))
    moves.append(diagonal(pieces,pos,-1,"W"))
    moves.append(diagonal(pieces,pos,1,"E"))
    moves.append(diagonal(pieces,pos,-1,"E"))

    for i in moves: 
        if(len(i) != 0):
            result.append(i[0][0])

        if(getPos(pieces,pos)[:1] == "w"):
            if(len(i[1]) != 0):
                if(getPos(pieces,i[1])[:1] == "b"):
                    result.append(i[1])

        elif(getPos(pieces,pos)[:1] == "b"):
            if(len(i[1]) != 0):
                if(getPos(pieces,i[1])[:1] == "w"):
                    result.append(i[1])

    return result

def behavior(allPos,pos):
    targetunit = getPos(allPos,pos)[1:]
    
    if(targetunit == "Pawn"):
        return movegenPawn(pos)

    if(targetunit == "Rook"):
        return movegenRook(pos)

    if(targetunit == "Bishop"):
        return movegenBishop(pos)

    if(targetunit == "Knight"):
        return movegenKnight(pos)

    if(targetunit == "Queen"):
        result = []
        for i in movegenBishop(pos):
            result.append(i)
        for i in movegenRook(pos):
            result.append(i)

        return result

    if(targetunit == "King"):
        return movegenKing(pos)
            
def WplayerMove(allPos):
    moveComplete = False
    validResponse = ["Pawn","Rook","Knight","Bishop","Queen","King"]
    targetPiece = ""
    drawBoard(pieces)

    while(True):
        print("\nWHITE MOVE:")
        print("{ Pawn: ♙, Rook: ♖, Knight: ♘, Bishop: ♗, Queen: ♕, King: ♔ }")

        while(True):
            targetPiece = input("WHITE: Enter Target Piece > ")
            if(targetPiece not in validResponse):
                print("Enter a valid response")
            else:
                break
        
        validPos = pieces.get("w" + targetPiece)
        
        if(validPos != None):
            print(validPos)

            while(True):
                targetPos = input("WHITE: Enter Target Position > ")
                if(targetPos not in validPos):
                    print("Enter a valid response")
                else:
                    validMoves = behavior(pieces,targetPos)
                    break
            
            if(len(validMoves) > 0):
                print(validMoves)

                while(True):
                    targetMove = input("WHITE: Enter Move > ")
                    if(targetMove not in validMoves):
                        print("Enter a valid response")
                    else:
                        moveComplete = True
                        break
            else:
                print("This piece has no valid moves")
        
        else:
            print("You don't have any remaining units of this type")
        
        if(moveComplete):
            print("WHITE: MOVE " + targetPiece + " at " + targetPos + " to: " + targetMove)
            move(targetPos,targetMove)
            break
        
    
if __name__ == "__main__":
    #drawBoard(pieces)

    game = True
    if(game):
        for i in range(4):
            WplayerMove(pieces)

    