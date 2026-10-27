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