def ucs_shortest_path(initial, goal):
    # A dictionary mapping cumulative cost to a list of states (Bucket Queue)
    # This acts as an efficient priority queue using only the collections library.
    frontier = defaultdict(list)
    frontier[0].append(initial)
    
    # Dictionary to track the minimum cost to reach each state
    visited = {initial: 0} # dictionary
    
    current_min_cost = 0
    
    while frontier:
        # Advance the current_min_cost to the next non-empty bucket
        while current_min_cost not in frontier or not frontier[current_min_cost]:
            current_min_cost += 1
            # Failsafe if queue is theoretically empty
            if current_min_cost > max(frontier.keys(), default=current_min_cost):
                return -1
                
        # Pop a state from the current lowest-cost bucket
        current_state = frontier[current_min_cost].pop()
        
        # Check if we've reached the goal
        if current_state == goal:
            return current_min_cost
            
        # If we previously found a cheaper path to this state while it was waiting, skip it
        if visited.get(current_state, float('inf')) < current_min_cost:
            continue

        blank_index = current_state.index("#")
        legal_moves = get_legal_moves(blank_index)
        
        for move in legal_moves:
            next_state = make_move(current_state, move, blank_index)
            new_cost = current_min_cost + move_costs[move]
            
            # If this path to next_state is cheaper than any previously found, update and queue
            if new_cost < visited.get(next_state, float('inf')):
                visited[next_state] = new_cost
                frontier[new_cost].append(next_state)
                
    return -1