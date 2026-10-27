from collections import defaultdict

def ucs(initial, goal):
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