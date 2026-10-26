
from collections import deque, defaultdict

move_costs = {"UP": 5, "DOWN": 1, "LEFT": 1, "RIGHT": 1}
def get_legal_moves(board):
    legal_moves = []
    blank_index = board.index("#")
    row = blank_index // 3 + 1
    col = blank_index % 3 + 1

    if row > 1: legal_moves.append("up")
    if row < 3: legal_moves.append("down")
    if col > 1: legal_moves.append("left")
    if col < 3: legal_moves.append("right")

    return legal_moves

def make_move(boardStr, move):
    board = list(boardStr)
    blank_index = board.index("#")
    
    match move:
        case "up":
            board[blank_index] = board[board_index - 3]
            board[blank_index - 3] = "#"
        case "down":
            board[blank_index] = board[board_index + 3]
            board[blank_index + 3] = "#"
        case "right":
            board[blank_index] = board[board_index + 1]
            board[blank_index + 1] = "#"
        case "left":
            board[blank_index] = board[board_index - 1]
            board[blank_index - 1] = "#"
    
    return "".join(board)



def ucs_shortest_path(initial, goal):
    # Part 1
    frontier = defaultdict(list)
    frontier[0].append(initial)
    visited = {initial: 0}
    current_min_cost = 0

    # Part 2
    while frontier:
        while current_min_cost not in frontier:
            current_min_cost += 1

        current_state = frontier[current_min_cost].pop()
        if not frontier[current_min_cost]:
            del frontier[current_min_cost]

        if current_state == goal:
            return current_min_cost

        # Part 3
        legal_moves = get_legal_moves(current_state)

        for move in legal_moves:
            next_board = make_move(current_state, move)
            new_cost = current_min_cost + move_costs[move]

            if next_board not in visited or new_cost < visited[next_board]:
                visited[next_board] = new_cost
                frontier[new_cost].append(next_board)

    return -1

initial = input().strip()
goal = input().strip()
print(ucs_shortest_path(initial, goal))