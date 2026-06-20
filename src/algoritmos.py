def bfs(graph, start_word):
    if not isinstance(graph, dict) or not graph:
        raise ValueError("O grafo fornecido é inválido ou está vazio.")
    
    if start_word not in graph:
        raise KeyError(f"A palavra '{start_word}' não existe no grafo.")

    visited = set()
    queue = [start_word]
    visited.add(start_word)
    result = []

    while queue:
        current_vertex = queue.pop(0)
        result.append(current_vertex)

        for neighbor in graph.get(current_vertex, {}):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result