# 🧠 extrator_ia_pro

Sistema de extração inteligente de conteúdo textual a partir de arquivos `.pdf`, `.docx`, `.xlsx` e outros — com limpeza avançada e preparação para agentes de IA (RAG, embeddings, chatbot, etc.).

---

## 🚀 Funcionalidades

- 📄 Suporte a múltiplos formatos de entrada:
  - PDF (`.pdf`)
  - Word (`.docx`)
  - Excel (`.xlsx`, `.xls`)
  - Texto (`.txt`)
- 🧼 Pipeline de limpeza inteligente:
  - Remoção de duplicatas
  - Correção de palavras quebradas
  - Padronização de espaçamento e pontuação
- 🧱 Divisão automática em chunks (blocos prontos para IA)
- 📊 Geração de relatórios JSON com estatísticas de cada documento
- ✅ Pronto para ser integrado com IA via embeddings ou RAG

---

## 📁 Estrutura do Projeto

```
extrator_ia_pro/
├── main.py
├── requirements.txt
├── entrada/          ← Coloque seus arquivos aqui
├── saida/            ← Resultados em .txt + saida.json
├── chunks/           ← Blocos para IA (ideal p/ embeddings)
├── relatorios/       ← Análises por arquivo (.json)
├── analise/
│   └── otimizador_texto.py
├── extratores/
│   ├── pdf_extrator.py
│   ├── docx_extrator.py
│   ├── xlsx_extrator.py
│   └── generic_extrator.py
└── utils/
    └── export_utils.py
```

---

## ⚙️ Como usar

### 1. Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/extrator_ia_pro.git
cd extrator_ia_pro
```

### 2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Baixe o recurso do NLTK (somente uma vez):

```python
import nltk
nltk.download('punkt')
```

### 5. Coloque os arquivos em `entrada/` e execute:

```bash
python main.py
```

---

## 🧪 Exemplo de saída

- `saida/arquivo.txt`: texto limpo e unificado
- `chunks/arquivo_chunk_1.txt`: blocos de 500 tokens
- `relatorios/arquivo_relatorio.json`: análise automática
- `saida/saida.json`: todos os textos agrupados em JSON

---

## 💡 Próximas evoluções

- 🌐 API local com FastAPI
- 💬 Chat com base nos arquivos (RAG)
- 🧠 Integração com OpenAI, HuggingFace ou LlamaIndex
- 🔍 Busca semântica com FAISS ou Qdrant

---

## 👨‍💻 Autor & Colaboração

Construído por Kildere Sobral Irineu com apoio técnico do seu 'Agente de IA Dev' do ChatGPT.  
Este projeto foi desenvolvido de forma iterativa, com foco prático e escalabilidade para uso com Inteligência Artificial.

www.linkedin.com/in/kilderesobralirineu 

---

## 📄 Licença

MIT
