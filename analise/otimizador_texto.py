import re

def limpar_texto(texto):
    texto = re.sub(r'\n{2,}', '\n', texto)
    texto = re.sub(r' +', ' ', texto)
    return texto.strip()

def remover_duplicatas(texto):
    linhas = texto.splitlines()
    unicas = []
    for linha in linhas:
        if linha.strip() and linha not in unicas:
            unicas.append(linha)
    return "\n".join(unicas)

def limpar_texto_avancado(texto: str) -> str:
    linhas = list(dict.fromkeys(texto.splitlines()))
    texto = "\n".join(linhas)
    texto = re.sub(r'(\w{2,})\s+(\w{2,})', lambda m: (
        m.group(1) + m.group(2)
        if m.group(1).islower() and m.group(2).islower()
        else m.group(1) + ' ' + m.group(2)
    ), texto)
    texto = re.sub(r'(\d+)\.(\w)', r'\1. \2', texto)
    texto = re.sub(r'\n{2,}', '\n', texto)
    texto = re.sub(r' {2,}', ' ', texto)
    return texto.strip()

def chunk_texto(texto, max_tokens=500):
    linhas = texto.splitlines()
    chunks = []
    atual = []
    count = 0
    for linha in linhas:
        if not linha.strip():
            continue
        atual.append(linha.strip())
        count += len(linha.split())
        if count >= max_tokens:
            chunks.append(" ".join(atual))
            atual = []
            count = 0
    if atual:
        chunks.append(" ".join(atual))
    return chunks

def gerar_relatorio(nome_arquivo, texto, chunks):
    return {
        "arquivo": nome_arquivo,
        "tamanho_texto": len(texto),
        "qtd_linhas": len(texto.splitlines()),
        "qtd_chunks": len(chunks),
        "recomendacoes": [
            "Verificar duplicatas",
            "Remover cabeçalhos repetidos",
            "Segmentar por seções com títulos"
        ]
    }
