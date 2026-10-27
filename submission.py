from collections import deque, defaultdict

# move_costs = {"up": 5, "down": 1, "left": 1, "right": 1}

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


def get_manhattan_distance(board, goal):
    total = 0
    for position in range(9):
        tile = board[position]
        if tile == "#":
            continue

        goal_position = goal.index(tile)
        row_distance = abs(position // 3 - goal_position // 3)
        col_distance = abs(position % 3 - goal_position % 3)
        total += row_distance + col_distance

    return total


def greedy_best_first_search(initial, goal):
    frontier = defaultdict(list)
    frontier[get_manhattan_distance(initial, goal)].append((initial, 0))
    visited = set()

    while frontier:
        smallest_heuristic = min(frontier)
        current_board, cost = min(frontier[smallest_heuristic])
        frontier[smallest_heuristic].remove((current_board, cost))

        if not frontier[smallest_heuristic]:
            del frontier[smallest_heuristic]

        if current_board in visited:
            continue
        visited.add(current_board)

        if current_board == goal:
            return cost

        legal_moves = get_legal_moves(current_board)
        for move in legal_moves:
            next_board = make_move(current_board, move)
            if next_board not in visited:
                heuristic = get_manhattan_distance(next_board, goal)
                frontier[heuristic].append((next_board, cost + 1))

    return -1

initial = input().strip()
goal = input().strip()
print(greedy_best_first_search(initial, goal))