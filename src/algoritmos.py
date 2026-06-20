def bfs(grafo, palavra_inicial):
    if not isinstance(grafo, dict) or not grafo:
        raise ValueError("O grafo fornecido é inválido ou está vazio.")
    
    if palavra_inicial not in grafo:
        raise KeyError(f"A palavra '{palavra_inicial}' não existe no grafo.")

    visitados = set()
    fila = [palavra_inicial]
    visitados.add(palavra_inicial)
    resultado = []

    while fila:
        vertice_atual = fila.pop(0)
        resultado.append(vertice_atual)

        for vizinho in grafo.get(vertice_atual, {}):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

    return resultado