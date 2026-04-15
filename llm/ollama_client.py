import requests


def query_llm(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        if response.status_code != 200:
            return "LLM error"

        return response.json().get("response", "")

    except Exception as e:
        return f"Error contacting LLM: {str(e)}"
