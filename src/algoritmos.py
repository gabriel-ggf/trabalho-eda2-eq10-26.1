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


def criar_union_find(vertices):
    pai = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}
    return pai, rank


def encontrar(pai, vertice):
    if pai[vertice] != vertice:
        pai[vertice] = encontrar(pai, pai[vertice])
    return pai[vertice]


def unir(pai, rank, vertice_a, vertice_b):
    raiz_a = encontrar(pai, vertice_a)
    raiz_b = encontrar(pai, vertice_b)

    if raiz_a == raiz_b:
        return False  

    if rank[raiz_a] < rank[raiz_b]:
        pai[raiz_a] = raiz_b
    elif rank[raiz_a] > rank[raiz_b]:
        pai[raiz_b] = raiz_a
    else:
        pai[raiz_b] = raiz_a
        rank[raiz_a] += 1

    return True


def kruskal(grafo):
    vertices = list(grafo.keys())
    arestas = []

    for vertice_a, vizinhos in grafo.items():
        for vertice_b, peso in vizinhos.items():
            if vertice_a < vertice_b:
                arestas.append((peso, vertice_a, vertice_b))

    arestas.sort()

    pai, rank = criar_union_find(vertices)
    floresta = []
    peso_total = 0

    for peso, vertice_a, vertice_b in arestas:
        if unir(pai, rank, vertice_a, vertice_b):
            floresta.append((vertice_a, vertice_b, peso))
            peso_total += peso

    componentes = len(set(encontrar(pai, v) for v in vertices))

    return {
        "arestas": floresta,
        "peso_total": peso_total,
        "num_componentes": componentes
    }


def kruskal_todas_epocas(grafos_por_epoca):
    resultados = {}
    for epoca, grafo in grafos_por_epoca.items():
        resultados[epoca] = kruskal(grafo)
        print(f"Kruskal {epoca}: {len(resultados[epoca]['arestas'])} arestas, "
              f"{resultados[epoca]['num_componentes']} componente(s), "
              f"peso total {resultados[epoca]['peso_total']}")
    return resultados


def salvar_resultado_kruskal(resultado, epoca, caminho="data/processed"):
    import json
    import os

    os.makedirs(caminho, exist_ok=True)

    if len(resultado["arestas"]) > 50:
        nome_arquivo = f"{caminho}/kruskal_{epoca}.json"
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            json.dump(resultado, f, ensure_ascii=False, indent=4)
    else:
        nome_arquivo = f"{caminho}/kruskal_{epoca}.txt"
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write(f"=== Floresta Geradora Mínima - Época {epoca} ===\n\n")
            f.write(f"Componentes conectados: {resultado['num_componentes']}\n")
            f.write(f"Peso total: {resultado['peso_total']}\n\n")
            f.write("Arestas da floresta:\n")
            for a, b, peso in resultado["arestas"]:
                f.write(f"  {a} -- {b}  (peso: {peso})\n")

    print(f"Resultado salvo em: {nome_arquivo}")
    return nome_arquivo


def salvar_todos_resultados(resultados_por_epoca, caminho="data/processed"):
    for epoca, resultado in resultados_por_epoca.items():
        salvar_resultado_kruskal(resultado, epoca, caminho)