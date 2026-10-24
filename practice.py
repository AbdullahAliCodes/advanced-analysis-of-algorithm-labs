from collections import deque

def get_legal_moves(blank_index):

    row = blank_index // 3 + 1
    col = blank_index % 3 + 1

    legal_moves = []

    if (row > 1):
        legal_moves.append("up")
    if (row < 3):
        legal_moves.append("down")
    if (col > 1):
        legal_moves.append("left")
    if (col < 3):
        legal_moves.append("right")

    return legal_moves

def make_move(boardStr, direction, blank_index):
    board = list(boardStr)

    match direction.lower():
        case "up":
            board[blank_index] = board[blank_index - 3]
            board[blank_index - 3] = "#"
        case "down":
            board[blank_index] = board[blank_index + 3]
            board[blank_index + 3] = "#"
        case "right":
            board[blank_index] = board[blank_index + 1]
            board[blank_index + 1] = "#"
        case "left":
            board[blank_index] = board[blank_index - 1]
            board[blank_index - 1] = "#"
    
    return "".join(board)

def bfs_shortest_path():
    # 1. get input for initial and goal state
    initial_state = input().strip()
    goal_state = input().strip()

    # 2. store initial into a queue
    queue = deque([(initial_state, 0)])

    # 3. intialise a set visited & add initial
    visited = set()
    visited.add(initial_state)

    # 4. start a while loop, while the queue exist
    while queue:
        # 5. destructure tuple current_state, score from popleft()
        current_state, cost = queue.popleft()
        # 6. check if current == goal, return cost
        if (current_state == goal_state):
            return cost

        # 7. if not, find blank, and call get_legal_moves
        blank_index = current_state.index("#")
        legal_moves = get_legal_moves(blank_index)

        # 8. iterate through legal_moves array
        for move in legal_moves:
            # 8.1. call make_move on each move, and assign to next_move
            next_move = make_move(current_state, move, blank_index)

            # 8.2. if next_move is not in visited
            if next_move not in visited:
                # 8.2.a. add next_move to visited
                visited.add(next_move)
                # 8.2.b. append next_move to queue
                queue.append((next_move, cost + 1))

    # 9. return -1 if goal state is not possible
    return -1

print(bfs_shortest_path())