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
# UNION-FIND 
# Serve para detectar ciclos e unir componentes do grafo

def criar_union_find(vertices):
    """
    Cria a estrutura Union-Find para um conjunto de vértices.
    Cada vértice começa como seu próprio pai (componente isolado).
    """
    pai = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}
    return pai, rank


def encontrar(pai, vertice):
    """
    Encontra o representante (raiz) do componente de um vértice.
    Usa compressão de caminho para eficiência.
    """
    if pai[vertice] != vertice:
        pai[vertice] = encontrar(pai, pai[vertice])  # compressão de caminho
    return pai[vertice]


def unir(pai, rank, vertice_a, vertice_b):
    """
    Une os componentes de dois vértices.
    Retorna True se foram unidos, False se já estavam no mesmo componente (ciclo).
    """
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



# ALGORITMO DE KRUSKAL


def kruskal(grafo):
    """
    Executa o algoritmo de Kruskal para encontrar a Floresta Geradora Mínima.
    
    Como o grafo é DESCONEXO, o resultado será uma FLORESTA (várias árvores),
    uma para cada componente conectado do grafo.

    Parâmetros:
    -----------
    grafo : dict
        Dicionário de adjacência ponderado, gerado por criar_grafo() (grafos.py):
        {
            "palavra1": {"palavra2": peso, "palavra3": peso},
            "palavra2": {"palavra1": peso},
            ...
        }
        O peso de cada aresta é o produto das frequências das duas palavras
        no mesmo documento (ver grafos.py).

    Retorna:
    --------
    dict com:
        - "arestas": lista de tuplas (vertice_a, vertice_b, peso) da floresta geradora
        - "peso_total": soma dos pesos das arestas selecionadas
        - "num_componentes": número de componentes conectados encontrados
    """

    # --- 1. Extrair vértices e arestas do grafo ---
    vertices = list(grafo.keys())
    arestas = []

    for vertice_a, vizinhos in grafo.items():
        for vertice_b, peso in vizinhos.items():
            # Evita duplicatas (aresta A-B e B-A são a mesma)
            if vertice_a < vertice_b:
                arestas.append((peso, vertice_a, vertice_b))

    
    arestas.sort()

    
    pai, rank = criar_union_find(vertices)

   
    floresta = []
    peso_total = 0

    for peso, vertice_a, vertice_b in arestas:
        # Só adiciona a aresta se não formar ciclo
        if unir(pai, rank, vertice_a, vertice_b):
            floresta.append((vertice_a, vertice_b, peso))
            peso_total += peso

    
    componentes = len(set(encontrar(pai, v) for v in vertices))

    return {
        "arestas": floresta,
        "peso_total": peso_total,
        "num_componentes": componentes
    }



# EXECUÇÃO PARA TODAS AS ÉPOCAS

def kruskal_todas_epocas(grafos_por_epoca):
    """
    Roda o Kruskal para cada época do dicionário gerado em main.py.

    Parâmetros:
    -----------
    grafos_por_epoca : dict
        {
            "1980": {grafo da época},
            "1990": {grafo da época},
            ...
        }
        (formato gerado no main.py: grafos_por_epoca[period] = criar_grafo(documentos))

    Retorna:
    --------
    dict no formato:
        {
            "1980": {"arestas": [...], "peso_total": ..., "num_componentes": ...},
            "1990": {...},
            ...
        }
    """
    resultados = {}
    for epoca, grafo in grafos_por_epoca.items():
        resultados[epoca] = kruskal(grafo)
        print(f"Kruskal {epoca}: {len(resultados[epoca]['arestas'])} arestas, "
              f"{resultados[epoca]['num_componentes']} componente(s), "
              f"peso total {resultados[epoca]['peso_total']}")
    return resultados



# FUNÇÃO DE SAÍDA - Salva ou retorna o resultado


def salvar_resultado_kruskal(resultado, epoca, caminho="data/processed"):
    """
    Salva o resultado do Kruskal de UMA época em um arquivo .json ou .txt.
    Segue o mesmo padrão de pasta usado em main.py (data/processed/...).

    Parâmetros:
    -----------
    resultado : dict
        Retorno da função kruskal() para uma época específica
    epoca : str
        Nome/ano da época analisada (ex: "1980", "1990"...)
    caminho : str
        Pasta onde salvar o arquivo
    """
    import json
    import os

    os.makedirs(caminho, exist_ok=True)

    # Salva em JSON se o resultado for grande, txt se for pequeno
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
    """
    Salva o resultado do Kruskal de TODAS as épocas, um arquivo por época.

    Parâmetros:
    -----------
    resultados_por_epoca : dict
        Retorno da função kruskal_todas_epocas()
    caminho : str
        Pasta onde salvar os arquivos
    """
    for epoca, resultado in resultados_por_epoca.items():
        salvar_resultado_kruskal(resultado, epoca, caminho)