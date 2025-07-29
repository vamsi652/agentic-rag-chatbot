from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent

class CoordinatorAgent:
    def __init__(self):
        self.ingestion = IngestionAgent()
        self.retrieval = RetrievalAgent()
        self.llm = LLMResponseAgent()

    def run_pipeline(self, file_paths, query, trace_id):
        all_docs = []
        for path in file_paths:
            ingest_msg = self.ingestion.ingest(path, trace_id)
            all_docs.append(ingest_msg["payload"]["content"])
        
        retrieval_msg = self.retrieval.retrieve(query, all_docs, trace_id)
        llm_msg = self.llm.generate_answer(retrieval_msg["payload"]["retrieved_context"], query, trace_id)
        return llm_msg
