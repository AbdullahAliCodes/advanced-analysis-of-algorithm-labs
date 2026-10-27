from collections import deque, defaultdict

move_costs = {"up": 5, "down": 1, "left": 1, "right": 1}

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

def breadth_first_search(initial, goal):
    queue = deque([(initial, 0)])
    visited = set()
    visited.add(initial)

    while queue:
        current_board, cost = queue.popleft()
        if current_board == goal:
            return cost

        legal_moves = get_legal_moves(current_board)
        for move in legal_moves:
            next_board = make_move(current_board, move)

            if next_board not in visited:
                visited.add(next_board)
                queue.append((next_board, cost + 1))

    return -1
    

def uniform_cost_search(initial, goal):
    frontier = defaultdict(list)
    frontier[0].append(initial)
    visited = {initial: 0}
    current_min_cost = 0

    while frontier:
        while current_min_cost not in frontier:
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

            if next_board not in visited or new_cost < visited[next_board]:
                visited[next_board] = new_cost
                frontier[new_cost].append(next_board)

    return -1


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


def a_star_search(initial, goal):
    frontier = defaultdict(list)
    frontier[manhattan_distance(initial, goal)].append((initial, 0))
    visited = set()
    current_min_priority = 0

    while frontier:
        while current_min_priority not in frontier:
            current_min_priority += 1

        current_board, cost = frontier[current_min_priority].pop()
        if not frontier[current_min_priority]:
            del frontier[current_min_priority]

        if current_board in visited:
            continue
        visited.add(current_board)

        if current_board == goal:
            return cost

        legal_moves = get_legal_moves(current_board)
        for move in legal_moves:
            next_board = make_move(current_board, move)
            if next_board not in visited:
                new_cost = cost + 1
                priority = new_cost + manhattan_distance(next_board, goal)
                frontier[priority].append((next_board, new_cost))

    return -1