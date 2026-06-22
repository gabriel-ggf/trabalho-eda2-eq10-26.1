## Trabalho de EDA2 2026.1 - Equipe 10 - UNB Campus Gama

# Análise Textual baseado em Épocas

Esse projeto se trata do uso prático dos conteúdos aprendidos no decorrer da disciplina Estrutura de Dados 2. O objetivo do nosso trabalho é utilizar grafos, além de outras estruturas de dados e algoritmos apresentados em sala de aula, para comparar o vocabulário e a coerência entre textos de diferentes épocas, analisando suas maiores diferenças e similaridades.

O código foi desenvolvido em Python, utilizando apenas bibliotecas de Processamento de Linguagem Natural (PLN) para carregar os dados. O programa funciona como uma simulação; portanto, iremos utilizar textos fictícios já selecionados e determinar os dados que queremos encontrar dentro do próprio programa.


### Integrantes do Grupo:

- Gabriel Guedes Fernandes - 232014656
- Daniel Fernandes Silva - 222008459
- Júlia Pêgo de Meneses - 231037745
- Vitor Guilherme Lustosa de Carvalho - 232014342
- Lara Souza Mota - 232021786

---

### Requerimentos

- Python 3.12+
- *Modulo Python*: spaCy 3.8.14+
- *Pipeline spaCy*: pt_core_news_sm (3.8.0)
- Git 2.54+

### Como Rodar Localmente

1. Certifique-se que Python está instalado na sua máquina.

```
python --version
```

2. Instale as dependencias. Utilize um ambiente virtual, caso necessário.

```
pip install spacy
python -m spacy download pt_core_news_sm
```

```
# Caso precise gerar um ambiente virtual, aplique esse código antes do anterior.
python -m venv venv
source venv/bin/activate #Linux/macOS
```

3. Clone o repositorio

```
git clone https://github.com/gabriel-ggf/trabalho-eda2-eq10-26.1.git
```

4. Entre no diretorio correto e rode a aplicação.

```
cd trabalho-eda2-eq10-26.1/src
python main.py
```