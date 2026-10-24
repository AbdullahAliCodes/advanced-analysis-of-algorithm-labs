def Moves():
    board = input().strip()
    direction = input().strip().lower()
    boardArr = list(board)
    blankIndex = boardArr.index("#")
        
    newBoard = move(boardArr, direction, blankIndex)
    return newBoard

def move(boardArr, direction, blankIndex):
    match direction:
        case "up":
            boardArr[blankIndex] = boardArr[blankIndex-3]
            boardArr[blankIndex-3] = "#"
        case "left":
            boardArr[blankIndex] = boardArr[blankIndex-1]
            boardArr[blankIndex-1] = "#"
        case "right":
            boardArr[blankIndex] = boardArr[blankIndex+1]
            boardArr[blankIndex+1] = "#"
        case "down":
            boardArr[blankIndex] = boardArr[blankIndex+3]
            boardArr[blankIndex+3] = "#"
    return "".join(boardArr)


print(Moves())

# 1234#6789