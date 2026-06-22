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

def kruskal(grafo):
    """
    Executa o algoritmo de Kruskal para encontrar a Floresta Geradora Mínima. 
    Caso o grafo seja desconexo, o resultado será uma FLORESTA (várias árvores),
    uma para cada componente conectado do grafo.
    Em nosso caso, não há grafo desconexo, então essa exceção não se aplica aqui.
    """

    vertices = list(grafo.keys())
    arestas = []

    for vertice_a, vizinhos in grafo.items():
        for vertice_b, peso in vizinhos.items():
            if vertice_a < vertice_b:
                arestas.append((peso, vertice_a, vertice_b))

    arestas.sort(reverse=True)

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
    """
    Roda o Kruskal para cada época do dicionário gerado em main.py.
    """
    resultados = {}
    for epoca, grafo in grafos_por_epoca.items():
        resultados[epoca] = kruskal(grafo)
        print(f"Kruskal {epoca}: {len(resultados[epoca]['arestas'])} arestas, "
              f"{resultados[epoca]['num_componentes']} componente(s), "
              f"peso total {resultados[epoca]['peso_total']}")
    return resultados

def bfs(grafo, palavra_inicial):

    '''
    Função responsável pela aplicação do algoritmo do BFS.
    Recebe um grafo e uma palavra inicial.
    Cria uma FILA para calcular o BFS, e retorna o resultado.
    '''

    if not isinstance(grafo, dict) or not grafo:
        raise ValueError("Grafo inválido ou vazio.")
    
    if palavra_inicial not in grafo:
        raise KeyError(f"A palavra '{palavra_inicial}' não está presente no grafo.")

    visitado = {palavra_inicial}
    fila = [(palavra_inicial, 0)]
    pais = {palavra_inicial: None}
    ordem_visita = {}
    niveis = {palavra_inicial: 0}
    
    contador = 0
    while fila:
        vertice_atual, nivel_atual = fila.pop(0)
        ordem_visita[vertice_atual] = contador
        contador += 1

        for vizinho in grafo.get(vertice_atual, {}):
            if vizinho not in visitado:
                visitado.add(vizinho)
                pais[vizinho] = vertice_atual
                niveis[vizinho] = nivel_atual + 1
                fila.append((vizinho, nivel_atual + 1))
    
    resultado = {}
    for vertice in visitado:
        resultado[vertice] = {
            "pai": pais[vertice],
            "ordem_de_visita": ordem_visita[vertice],
            "nivel": niveis[vertice]
        }

    return resultado