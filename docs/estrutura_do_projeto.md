# Estrutura do Projeto

## Arquivos

- **main.py**: Este é o arquivo principal do programa. Ele inicializa os dados, criando a lista de ocorrências, e chama as funções do grafo e dos algoritmos.
- **algoritmos.py**: Neste arquivo, estão os algoritmos de grafos utilizados para a análise dos dados, como o BFS (Busca em Largura) e o algoritmo de Kruskal.
- **grafos.py**: Criação e manipulação dos gráfos e outras estruturas de dados.
- **processamento_de_dados.py**: Este módulo é responsável por abrir os arquivos de texto, realizar seu tratamento com a biblioteca de PLN e, além disso, efetuar o salvamento dos dados processados.

## Pasta do Dados (data)

### Pasta *text*

Esta pasta armazena os dados iniciais gerados para a análise. Os textos devem estar separados em suas respectivas pastas de acordo com cada época dentro deste repositório. Em nosso caso, são quatro pastas para cada época, com vinte textos em cada uma.

### Pasta *processed*

Esta pasta armazena os dados obtidos pelo programa, sendo atualizada toda vez que o sistema é iniciado. Os arquivos são salvos nos formatos *.json* ou *.txt*, dependendo do caso.

- **words_list.json**: Trata-se da lista de ocorrências de cada palavra em cada texto. O sistema salva os dados no formato ilustrado abaixo:

```
{
    "epoca1": [
        {
            "amor": 5,
            "tempo": 3,
            "vida": 2
        },
        {
            "guerra": 4,
            "soldado": 2,
            "terra": 1
        }
    ],
    "epoca2": [
        {
            "maquina": 8,
            "industria": 6
        }
    ]
}
```

- **krukal_{ano}.json**: Resultado do algoritmo de Kruskal salvo por época. O sistema salva os dados no formato ilustrado abaixo:

```
    {
        "1980": {
            "arestas": [
                [vertice1, vertice2, peso],
                [...]
            ], 
            "peso_total": ..., 
            "num_componentes": ...
        },
        "1990": {...},
        ...
    }
```

- **bfs_{ano}_economiajson**: Resultado do algoritmo BFS salvo por época. O sistema salva os dados no formato ilustrado abaixo:

```
    {
        periodo : 2000,
        "palavra_raiz": "economia",
        "profundidade_arvore": 3,
        "total_palavras": 500,
        "arvore_bfs": {
            "nivel0": [vertice1],
            "nivel1": [vertice1, vertice2, ...],
            "nivelx": [...]
        }
    }
```