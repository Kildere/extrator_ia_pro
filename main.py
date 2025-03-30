
import os
import json
from extratores.pdf_extrator import extract_text_pdf
from extratores.docx_extrator import extract_text_docx
from extratores.xlsx_extrator import extract_text_xlsx
from extratores.generic_extrator import extract_text_generic
from utils.export_utils import export_as_txt, export_as_json, export_chunks
from analise.otimizador_texto import limpar_texto, remover_duplicatas, limpar_texto_avancado, chunk_texto, gerar_relatorio

def extrair_arquivo(path):
    if path.endswith('.pdf'):
        return extract_text_pdf(path)
    elif path.endswith('.docx'):
        return extract_text_docx(path)
    elif path.endswith('.xlsx') or path.endswith('.xls'):
        return extract_text_xlsx(path)
    else:
        return extract_text_generic(path)

def processar_pasta(pasta_entrada, pasta_saida):
    resultados = {}
    os.makedirs(pasta_saida, exist_ok=True)
    os.makedirs("relatorios", exist_ok=True)
    os.makedirs("chunks", exist_ok=True)

    for arquivo in os.listdir(pasta_entrada):
        caminho = os.path.join(pasta_entrada, arquivo)
        if os.path.isfile(caminho):
            print(f"📄 Processando {arquivo}...")
            conteudo = extrair_arquivo(caminho)
            conteudo = limpar_texto(conteudo)
            conteudo = remover_duplicatas(conteudo)
            conteudo = limpar_texto_avancado(conteudo)
            chunks = chunk_texto(conteudo)
            nome_base = os.path.splitext(arquivo)[0]
            export_as_txt(nome_base, conteudo, pasta_saida)
            export_chunks(nome_base, chunks, "chunks")
            resultados[arquivo] = conteudo
            relatorio = gerar_relatorio(arquivo, conteudo, chunks)
            with open(f"relatorios/{nome_base}_relatorio.json", "w", encoding="utf-8") as f:
                json.dump(relatorio, f, indent=2, ensure_ascii=False)

    export_as_json(resultados, os.path.join(pasta_saida, "saida.json"))
    print("✅ Processamento finalizado com sucesso!")

if __name__ == "__main__":
    entrada = "entrada"
    saida = "saida"
    os.makedirs(entrada, exist_ok=True)
    os.makedirs(saida, exist_ok=True)
    processar_pasta(entrada, saida)
