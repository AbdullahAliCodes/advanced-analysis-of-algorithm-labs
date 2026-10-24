def legalMoves():
    board = input().strip()
    boardArr = list(board)
    blankIndex = boardArr.index("#")

    row = blankIndex // 3 + 1
    col = blankIndex % 3 + 1

    lastRow = (len(boardArr)-1) // 3 + 1
    lastCol = (len(boardArr)-1) % 3 + 1

    # print(f"row: {row}, col: {col}")
    # print(f"Last row: {lastRow}, col: {lastCol}")

    legalMoves = []

    if (row != 1):
        legalMoves.append("UP")
    if (row != lastRow):
        legalMoves.append("DOWN")
    if (col != 1):
        legalMoves.append("LEFT")
    if (col != lastCol):
        legalMoves.append("RIGHT")

    return "\n".join(legalMoves)

print(legalMoves())

# 1234#6789