from PyPDF2 import PdfReader

def extract_text_pdf(path):
    reader = PdfReader(path)
    return "\n".join([page.extract_text() or "" for page in reader.pages])
