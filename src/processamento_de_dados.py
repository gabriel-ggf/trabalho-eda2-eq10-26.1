import spacy
import json
import os

spc = spacy.load("pt_core_news_sm")

def carregar_palavras (caminho):

    '''
    A partir do caminho pré-definido dos arquivos das palavras,
    retorna uma lista de palavras filtradas utilizando a biblioteca spacy.
    '''

    with open(caminho, 'r', encoding='utf-8') as fl:
        
        texto = fl.read()
        doc = spc(texto)

    palavras = []

    for token in doc:
        lema = token.lemma_.lower()
        if not token.is_stop and not token.is_punct and not token.is_space and len(lema):
            palavras.append(lema)

    return palavras

def salvar_lista(caminho_de_salvamento, dados):

    '''
    Função simples de salvamento com arquivos ".json".
    Recebe os dados e o caminho de salvamento.
    '''

    with open(caminho_de_salvamento, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    print(f"Dados salvos em: {caminho_de_salvamento}")

def salvar_resultado_kruskal(resultado, epoca, caminho="data/processed"):
    """
    Salva o resultado do Kruskal de UMA época em um arquivo .json ou .txt.
    Segue o mesmo padrão de pasta usado em main.py (data/processed/...).
    """

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
    """
    for epoca, resultado in resultados_por_epoca.items():
        salvar_resultado_kruskal(resultado, epoca, caminho)

def coocorrencia(caminho_arquivo):
    '''
    Apenas retorna uma matriz com coocorrência de vértices entre os grafos.
    '''
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    
    nomes = list(dados.keys())
    conjuntos = [set(dados[nome].keys()) for nome in nomes]
    n = len(nomes)
    
    matriz = [[len(conjuntos[i].intersection(conjuntos[j])) for j in range(n)] for i in range(n)]
    
    print(f"{'':>10}" + "".join(f"{nome:>10}" for nome in nomes))
    print("-" * (10 + n * 10))
    for i, linha in enumerate(matriz):
        print(f"{nomes[i]:>10}" + "".join(f"{val:>10}" for val in linha))