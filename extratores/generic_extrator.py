import textract

def extract_text_generic(path):
    try:
        return textract.process(path).decode('utf-8')
    except Exception as e:
        return f"Erro ao extrair conteúdo: {e}"
