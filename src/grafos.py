# Esses dois imports são utilizados para gerar a lista de ocorrência.
# Eles NÃO são aplicados na função geradora dos grafos.
import os
from processamento_de_dados import carregar_palavras

def criar_lista(caminho):

    '''
    Gera e retorna a lista de ocorrência.
    Esta função utiliza o import "os" para encontrar o lugar de salvamento dos dados
    e o import "carregar_palavras" para filtrar as palavras com a biblioteca spacy.
    '''

    lista = {}
    
    for periodo in os.listdir(caminho):

        caminho_periodo = os.path.join(caminho, periodo)

        if os.path.isdir(caminho):

            lista [periodo] = []
            for arquivo in os.listdir(caminho_periodo):
                if arquivo.endswith("txt"):

                    caminho_do_arquivo = os.path.join(caminho_periodo, arquivo)
                    palavras = carregar_palavras(caminho_do_arquivo)
            
                frequencia = {}
                for word in palavras:
                    frequencia[word] = frequencia.get(word, 0) + 1

                lista[periodo].append(frequencia)
    
    return lista

def criar_grafo(documentos):
    
    """
    Constroi um grafo de coocorrência a partir dos documentos de uma época.
    Cada vértice representa uma palavra e cada aresta o peso da relação entre duas palavras,
    calculado pela multiplicação de suas frequências no mesmo documento.
    """
    grafo = {}
    
    for documento in documentos:
        palavras = list(documento.keys())
        
        # garante a criação de todos os vértices primeiro O(V)
        for palavra in palavras:
            if palavra not in grafo:
                grafo[palavra] = {}
                
        # cria ou incrementa as arestas com o peso multiplicativo O(E)
        for i in range(len(palavras)):
            for j in range(i + 1, len(palavras)):
                palavra_a = palavras[i]
                palavra_b = palavras[j]
                peso = documento[palavra_a] * documento[palavra_b]
                
                grafo[palavra_a][palavra_b] = grafo[palavra_a].get(palavra_b, 0) + peso
                grafo[palavra_b][palavra_a] = grafo[palavra_b].get(palavra_a, 0) + peso
                
    return grafo