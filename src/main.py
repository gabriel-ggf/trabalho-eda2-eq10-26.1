import os
from processamento_de_dados import salvar_lista, salvar_todos_resultados
from grafos import criar_grafo, criar_lista
from algoritmos import kruskal_todas_epocas
from algoritmos import bfs

# Caminho de entrada pala gerar a lista de ocorrência.
caminho_de_entrada = os.path.join('data', 'text')
caminho_de_salvamento = "data/processed/words_list.json"

# Primeira etapa do programa.
# Gera uma lista de ocorrência com as palavras filtradas pela biblioteca Spacy
print(f"Gerando Lista de Ocorrência...")
lista_ocorrencia = criar_lista(caminho_de_entrada)
salvar_lista(caminho_de_salvamento, lista_ocorrencia)

print(f"\n------------------------------------------\n")

# Segunda etapa do programa.
# Gera os grafos de cada época utilizando a lista de ocorrência.
print(f"Gerando Grafos por Épocas...")
grafos_por_epoca = {}
for period, documentos in lista_ocorrencia.items():
    grafos_por_epoca[period] = criar_grafo(documentos)
    print(f"Grafo {period}: {len(grafos_por_epoca[period])} vértices")

print(f"\n------------------------------------------\n")

# Terceira etapa do programa.
# Aplica o algoritmo de Kruskal para cada grafo e salva na pasta '/data/processed/'
print(f"Aplicando algoritmo de Kruskal por Época...")
resultados_kruskal = kruskal_todas_epocas(grafos_por_epoca)
salvar_todos_resultados(resultados_kruskal)

print(f"\n------------------------------------------\n")

# Quarta etapa do programa.
# Aplica o algoritmo BFS para cada grafo e salva na pasta '/data/processed/'
print(f"Aplicando algoritmo BFS por Época...")
palavra_alvo = "economia"
for periodo_alvo, grafo_alvo in grafos_por_epoca.items():
    if palavra_alvo in grafo_alvo:
        try:
            resultado_bfs = bfs(grafo_alvo, palavra_alvo)
            palavras_encontradas = sum(len(palavras) for palavras in resultado_bfs.values())
            
            dados_de_salvamento = {
                "periodo": periodo_alvo,
                "palavra_raiz": palavra_alvo,
                "profundidade_arvore": len(resultado_bfs) - 1, 
                "total_palavras": palavras_encontradas,
                "arvore_bfs": resultado_bfs 
            }
            
            caminho_bfs = os.path.join("data", "processed", f"bfs_{periodo_alvo}_{palavra_alvo}.json")
            salvar_lista(caminho_bfs, dados_de_salvamento)
            
        except Exception as e:
            print(f"Erro no periodo {periodo_alvo}: {e}")

print(f"\n------------------------------------------\n")