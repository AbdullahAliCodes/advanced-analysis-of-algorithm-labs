from collections import deque

def bfs(initial, goal):
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