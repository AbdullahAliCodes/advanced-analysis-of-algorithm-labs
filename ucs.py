def get_legal_moves(blank_index):

    row = blank_index // 3 + 1
    col = blank_index % 3 + 1

    legal_moves = []

    if (row > 1): legal_moves.append("up")
    if (row < 3): legal_moves.append("down")
    if (col < 3): legal_moves.append("right")
    if (col > 1): legal_moves.append("left")

    return legal_moves

def make_move(board_str, direction, blank_index):
    board_list = list(board_str)

    match direction.lower():
        case "up": 
            board_list[blank_index] = board_list[blank_index - 3]
            board_list[blank_index - 3] = "#"
        case "down": 
            board_list[blank_index] = board_list[blank_index + 3]
            board_list[blank_index + 3] = "#"
        case "right": 
            board_list[blank_index] = board_list[blank_index + 1]
            board_list[blank_index + 1] = "#"
        case "left": 
            board_list[blank_index] = board_list[blank_index - 1]
            board_list[blank_index - 1] = "#"
    
    return "".join(board_list)

def uniform_cost_search() {
    initial_state = input().strip()
    goal_state = input().strip()

    # assign initial state into the priority queue with cost

    # While prio
    if (initial_state = goal_state):
        # append cost
    
    visited = set()
    visited.add(current_state)

    blank_index = initial_state.index("#")
    legal_moves = get_legal_moves(blank_index)

    for move in legal_moves:
        next_move = make_move(current_state, move, blank_index)

        # check if 
}
