from collections import deque, defaultdict

def get_legal_moves(boardStr):
    blank_index = boardStr.index("#")

    row = blank_index // 3 + 1
    col = blank_index % 3 + 1
    legal_moves = []

    if (row > 1): legal_moves.append("up")
    if (row < 3): legal_moves.append("down")
    if (col > 1): legal_moves.append("left")
    if (col < 3): legal_moves.append("right")

    return legal_moves

def make_move(boardStr, move):
    board = list(boardStr)
    blank_index = board.index("#")

    match move:
        case "up":
            board[blank_index] = board[blank_index - 3]
            board[blank_index - 3] = "#"
        case "down":
            board[blank_index] = board[blank_index + 3]
            board[blank_index + 3] = "#"
        case "left":
            board[blank_index] = board[blank_index - 1]
            board[blank_index - 1] = "#"
        case "right":
            board[blank_index] = board[blank_index + 1]
            board[blank_index + 1] = "#"            

    return "".join(board)

def uniform_cost_search(initial, goal):
    frontier = defaultdict(list)
    frontier[0].append(initial)
    visited = {initial: 0}
    current_min_cost = 0

    while frontier:
        if current_min_cost not in frontier:
            current_min_cost += 1
        
        current_board = frontier[current_min_cost].pop()
        if not frontier[current_min_cost]:
            del frontier[current_min_cost]
        
        if current_board == goal:
            return current_min_cost
        
        legal_moves = get_legal_moves(current_board)
        for move in legal_moves:
            next_board = make_move(current_board, move)
            new_cost = 