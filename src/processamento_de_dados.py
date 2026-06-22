import spacy
import json
import os

spc = spacy.load("pt_core_news_sm")

def load_words (path):

    with open(path, 'r', encoding='utf-8') as fl:
        
        text = fl.read()
        doc = spc(text)

    words = []

    for token in doc:
        lemma = token.lemma_.lower()
        if not token.is_stop and not token.is_punct and not token.is_space and len(lemma):
            words.append(lemma)

    return words

def list_write(savement_path, data):
    os.makedirs(os.path.dirname(savement_path), exist_ok=True)

    with open(savement_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Dados salvos em: {os.path.abspath(savement_path)}")
