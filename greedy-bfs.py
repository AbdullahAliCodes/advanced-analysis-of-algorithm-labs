def greedy_bfs(initial, goal):
    frontier = defaultdict(list)
    frontier[get_manhattan_distance(initial, goal)].append((initial, 0))
    visited = set()

    while frontier:
        smallest_h = min(frontier)
        current_board, cost = min(frontier[smallest_h])
        frontier[smallest_h].remove((current_board, cost))
        
        if not frontier[smallest_h]:
            del frontier[smallest_h]
        
        if current_board not in visited:
            continue
        visited.add(current_board)

        if current_board == goal:
            return cost
        
        legal_moves = get_legal
        for move in legal_moves:
            next_board = 

            if next_board not in visited:
                heuristic = get_man((next_board, goal))
                frontier[heuristic].append((next_board, cost + 1))