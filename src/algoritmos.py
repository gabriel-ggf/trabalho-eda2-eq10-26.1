def bfs(graph, start_word):
    if not isinstance(graph, dict) or not graph:
        raise ValueError("The provided graph is invalid or empty.")
    
    if start_word not in graph:
        raise KeyError(f"The word '{start_word}' does not exist in the graph.")

    visited = set()
    queue = [(start_word, 0)]
    visited.add(start_word)
    tree_levels = {}

    while queue:
        current_vertex, current_level = queue.pop(0)
        if current_level not in tree_levels:
            tree_levels[current_level] = []
        
        tree_levels[current_level].append(current_vertex)

        for neighbor in graph.get(current_vertex, {}):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, current_level + 1))

    return tree_levels