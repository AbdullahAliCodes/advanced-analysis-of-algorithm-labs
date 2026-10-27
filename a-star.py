def a_star(initial, goal):
    frontier = defaultdict(list)
    frontier[getmaxdist(initial, goal)].append((initial, 0))
    visited = set()