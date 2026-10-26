# AAA lab test template: 8-puzzle labs 1 and 2
# Only collections is imported (numpy and collections are the only allowed libraries).

from collections import deque, defaultdict

move_costs = {"UP": 5, "DOWN": 1, "LEFT": 1, "RIGHT": 1}   # UCS only. Set UP to 1 for uniform costs


def show(board):
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


# ---------- Helpers (Lab 1, Submissions 1 and 2) ----------

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


def manhattan(board, goal):
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


# ---------- Lab 1, Submission 3: BFS ----------

def bfs(initial, goal):
    queue = deque([(initial, 0)])
    visited = set()
    visited.add(initial)

    while queue:
        current, cost = queue.popleft()
        if current_state == goal_state:
            return cost

        legal_moves = get_legal_moves(current)

        for move in legal_moves:
            next_board = make_move(current, move)

            if next_board not in visited:
                visited.add(next_board)
                queue.append((next_board, cost + 1))
    
    return -1
            


# ---------- Lab 2, Submission 1: UCS ----------

def ucs_shortest_path(initial, goal):
    frontier = defaultdict(list)
    fronter[0].append(initial)
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
            new_cost = current_min_cost + move_costs[move]
    


# ---------- Lab 2, Submission 2: Greedy (priority = guess only) ----------

def greedy(start, goal):
    buckets = defaultdict(list)
    buckets[manhattan(start, goal)].append((start, 0))
    visited = set()

    while buckets:
        smallest = min(buckets)
        item = min(buckets[smallest])          # ties: alphabetically smallest board
        buckets[smallest].remove(item)
        if not buckets[smallest]:
            del buckets[smallest]
        board, cost = item

        if board in visited:
            continue
        visited.add(board)

        if board == goal:
            return cost

        for a in actions(board):
            next_board = move(board, a)
            if next_board not in visited:
                guess = manhattan(next_board, goal)
                buckets[guess].append((next_board, cost + 1))


# ---------- Lab 2, Submission 3: A* (priority = cost so far + guess) ----------

def astar(start, goal):
    buckets = defaultdict(deque)
    buckets[manhattan(start, goal)].append((start, 0))
    visited = set()

    while buckets:
        smallest = min(buckets)
        board, cost = buckets[smallest].popleft()
        if not buckets[smallest]:
            del buckets[smallest]

        if board in visited:
            continue
        visited.add(board)

        if board == goal:
            return cost

        for a in actions(board):
            next_board = move(board, a)
            if next_board not in visited:
                new_cost = cost + 1
                priority = new_cost + manhattan(next_board, goal)
                buckets[priority].append((next_board, new_cost))


# ---------- Main: uncomment the ONE block the question asks for ----------

# Lab 1, Submission 1: apply a move
# board = input().strip()
# action = input().strip()
# print(move(board, action))

# Lab 1, Submission 2: legal moves
# board = input().strip()
# for a in actions(board):
#     print(a)

# Board printer
# board = input().strip()
# show(board)

# Lab 1, Submission 3: BFS
# start = input().strip()
# goal = input().strip()
# print(bfs(start, goal))

# Lab 2, Submission 1: UCS
# start = input().strip()
# goal = input().strip()
# print(ucs(start, goal))

# Lab 2, Submission 2: Greedy
# start = input().strip()
# goal = input().strip()
# print(greedy(start, goal))

# Lab 2, Submission 3: A*
# start = input().strip()
# goal = input().strip()
# print(astar(start, goal))