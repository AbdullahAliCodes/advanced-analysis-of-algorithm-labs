def grid():
    board = "1857#3462"
    
    for i in range(0, 9, 3):
        row = board[i:i+3]
        print(" ".join(row))

grid()