import os
import json

def export_as_txt(nome, conteudo, pasta_saida):
    os.makedirs(pasta_saida, exist_ok=True)
    path = os.path.join(pasta_saida, nome + ".txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(conteudo)

def export_as_json(dados, arquivo_saida="saida.json"):
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

def export_chunks(nome_base, chunks, pasta_chunks):
    os.makedirs(pasta_chunks, exist_ok=True)
    for i, chunk in enumerate(chunks):
        path = os.path.join(pasta_chunks, f"{nome_base}_chunk_{i+1}.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(chunk)
