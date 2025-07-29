# 🤖 Agentic RAG Chatbot using Model Context Protocol (MCP)

A multi-agent Retrieval-Augmented Generation (RAG) chatbot that allows users to upload various document formats (PDF, DOCX, PPTX, TXT, Markdown, CSV) and ask questions based on their content. It features a modular architecture using four intelligent agents—`IngestionAgent`, `RetrievalAgent`, `LLMResponseAgent`, and `CoordinatorAgent`—communicating through a structured Model Context Protocol (MCP).



![alt text](<Screenshot (127).png>)

---

## ✅ Features

- 📄 Upload and parse multiple document formats: `PDF`, `DOCX`, `PPTX`, `CSV`, `TXT`, `MD`
- 🤖 Modular Agentic Design using:
  - **IngestionAgent** – parses and preprocesses uploaded documents
  - **RetrievalAgent** – generates embeddings and retrieves top-k context chunks
  - **LLMResponseAgent** – builds LLM queries and generates final responses
  - **CoordinatorAgent** – orchestrates the flow among other agents
- 🔌 Uses **Model Context Protocol (MCP)** for structured message passing
- 🧠 Embeddings via HuggingFace SentenceTransformers (`all-MiniLM-L6-v2`)
- 🗃️ Vector storage with **FAISS**
- 🗨️ LLM responses from **Together.ai** (`Mixtral` or `Mistral`)
- 💬 Streamlit UI for file uploads, multi-turn question answering, and source-based answers

---

## 📁 Folder Structure

```
agentic-rag-chatbot/
│
├── agents/
│   ├── ingestion_agent.py
│   ├── retrieval_agent.py
│   ├── llm_response_agent.py
│   └── coordinator_agent.py
│
├── mcp/
│   └── protocol.py  # MCP message format
│
├── vector_store/
│   └── store.py
│
├── ui/
│   └── app.py  # Streamlit app
│
├── data/
│   └── uploaded_files/
│
├── utils/
│   └── file_parsers.py
│
├── README.md
└── demo_ppt.pptx
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/agentic-rag-chatbot.git
cd agentic-rag-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add API Key for Together.ai

You can export it via terminal:

```bash
export TOGETHER_API_KEY="tgp_v1_XXXXXXXXXXXX"
```

Or create a `.env` file in the project root:

```ini
TOGETHER_API_KEY=tgp_v1_XXXXXXXXXXXX
```

### 4. Run the Streamlit UI

```bash
streamlit run ui/app.py
```

The UI will launch at [http://localhost:8501](http://localhost:8501).

---

## 💡 How It Works (Agentic Architecture)

### 🧠 Message Flow (Using MCP)

Each agent communicates using MCP messages structured like this:

```json
{
  "sender": "RetrievalAgent",
  "receiver": "LLMResponseAgent",
  "type": "CONTEXT_RESPONSE",
  "trace_id": "abc-123",
  "payload": {
    "top_chunks": ["doc1: KPIs include revenue", "slide3: growth by 12%"],
    "query": "What KPIs were tracked?"
  }
}
```

### ⚙️ Sample Workflow

User uploads: `sales_review.pdf`, `metrics.csv`

User asks: _"What KPIs were tracked in Q1?"_

Internally:

- `IngestionAgent` parses all documents and chunks content
- `RetrievalAgent` embeds chunks and retrieves top-k relevant ones
- `LLMResponseAgent` builds a prompt using retrieved chunks and queries the Together.ai LLM
- `CoordinatorAgent` coordinates flow among agents
- Response is shown in the UI with source references

---

## 🧠 Technologies Used

| Component           | Technology                      |
|--------------------|----------------------------------|
| Language Model      | Together.ai (Mixtral, Mistral)  |
| Embeddings          | SentenceTransformers (MiniLM)   |
| Vector DB           | FAISS                           |
| Frontend            | Streamlit                       |
| Document Parsing    | PyMuPDF, python-docx, pptx, pandas |
| Message Protocol    | Custom in-memory MCP            |

---

## 📦 Requirements

```
streamlit
python-dotenv
sentence-transformers
faiss-cpu
PyMuPDF
python-docx
python-pptx
pandas
together
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 📌 Challenges Faced

- Handling inconsistent document encoding and structure across formats
- Ensuring all agents consistently follow the MCP message schema
- Optimizing context chunking for large documents
- Integrating Together.ai within limited token budget

---


## 📄 License

MIT License. Feel free to use and modify with credit.

---

## 📬 Contact

For queries or feedback, open an issue or contact **Your Name**.
