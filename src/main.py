import processamento_de_dados as pdd
import os
from grafos import criar_grafo
from algoritmos import bfs

words_list = {}
data_path = os.path.join('data', 'text')
savement_path = "data/processed/words_list.json"

for period in os.listdir(data_path):

    period_path = os.path.join(data_path, period)

    if os.path.isdir(data_path):

        words_list[period] = []
        for file in os.listdir(period_path):
            if file.endswith("txt"):

                file_path = os.path.join(period_path, file)
                words = pdd.load_words(file_path)
        
            frequency = {}
            for word in words:
                frequency[word] = frequency.get(word, 0) + 1

            words_list[period].append(frequency)

pdd.list_write(savement_path, words_list)

# cria um grafo para cada epoca
grafos_por_epoca = {}
for period, documentos in words_list.items():
    grafos_por_epoca[period] = criar_grafo(documentos)
    print(f"Grafo {period}: {len(grafos_por_epoca[period])} vértices")
    
target_word = "economia" # palavra chave do bfs
for target_period, target_graph in grafos_por_epoca.items():
    if target_word in target_graph:
        try:
            bfs_result = bfs(target_graph, target_word)
            total_words_found = sum(len(words) for words in bfs_result.values())
            
            save_data = {
                "periodo": target_period,
                "palavra_raiz": target_word,
                "profundidade_arvore": len(bfs_result) - 1, 
                "total_palavras": total_words_found,
                "arvore_bfs": bfs_result 
            }
            
            bfs_output_path = os.path.join("data", "processed", f"bfs_{target_period}_{target_word}.json")
            pdd.list_write(bfs_output_path, save_data)
            
        except Exception as e:
            print(f"Erro no periodo {target_period}: {e}")