import pandas as pd

def extract_text_xlsx(path):
    df = pd.read_excel(path)
    return df.to_string(index=False)
