from vector_store.store import build_vector_store, get_relevant_chunks
from mcp.protocol import create_mcp_message

class RetrievalAgent:
    def retrieve(self, query, docs, trace_id):
        build_vector_store(docs)
        top_chunks = get_relevant_chunks(query)
        return create_mcp_message("RetrievalAgent", "LLMResponseAgent", "RETRIEVAL_RESULT", trace_id, {
            "retrieved_context": top_chunks,
            "query": query
        })
