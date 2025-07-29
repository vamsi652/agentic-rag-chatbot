from utils.file_parsers import parse_file
from mcp.protocol import create_mcp_message

class IngestionAgent:
    def ingest(self, file_path, trace_id):
        content = parse_file(file_path)
        return create_mcp_message("IngestionAgent", "RetrievalAgent", "INGESTED_CONTENT", trace_id, {
            "content": content,
            "filename": file_path
        })
