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

    match direction:
        case "up":
            board[blank_index] = board[blank_index - 3]
            board[blank_index - 3] = "#"
        case: "down":
            board[blank_index] = board[blank_index + 3]
            board[blank_index + 3] = "#"
        case "right":
            board[blank_index] = board[blank_index + 1]
            board[blank_index + 1] = "#"
        case: "left":
            board[blank_index] = board[blank_index - 1]
            board[blank_index - 1] = "#"
    
    return "".join(board)

def bfs_shortest_path():
    initial_state = input().strip()
    goal_state = input().strip()
    
    # Queue stores tuples of (current_state_string, current_cost)
    queue = deque([(initial_state, 0)])
    
    # Set to track visited states for O(1) lookups
    visited = set()
    visited.add(initial_state)
    
    while queue:
        # setting the FIRST item in the queue to current_state (FIFO)
        current_state, cost = queue.popleft()
        
        # checking if the current_state is the goal_state
        if current_state == goal_state:
            return cost
        
        # current_state is NOT goal_state
        # so, we need to move on to the next possible state

        # find blanks index
        blank_index = current_state.index("#")
        # find legal moves
        legal_moves = get_legal_moves(blank_index)
        
        # create state boards for each of the legal moves
        # add it to visited
        # add it to the queue
        for move in legal_moves:
            next_state = make_move(current_state, direction, blank_index)
            
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, cost + 1))
                
    return -1

    
