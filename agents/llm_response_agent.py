import requests
import os
from dotenv import load_dotenv

load_dotenv()

class LLMResponseAgent:
    def __init__(self):
        self.api_key = os.getenv("TOGETHER_API_KEY")
        self.api_url = "https://api.together.xyz/v1/chat/completions"
        self.model = "mistralai/Mixtral-8x7B-Instruct-v0.1"

    def generate_answer(self, context, query, trace_id):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        messages = [
            {"role": "system", "content": "You are a helpful assistant that answers based on the given context."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
        ]

        data = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7
        }

        response = requests.post(self.api_url, headers=headers, json=data)
        if response.status_code != 200:
            raise Exception(f"Together API Error: {response.status_code} - {response.text}")

        return {
            "payload": {
                "response": response.json()["choices"][0]["message"]["content"]
            },
            "trace_id": trace_id
        }
