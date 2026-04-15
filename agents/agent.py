from agents.tools import open_notepad, open_chrome, create_file, search_web
from llm.ollama_client import query_llm


def decide_and_act(user_input):
    user_input_lower = user_input.lower()

    if "notepad" in user_input_lower:
        return open_notepad()

    if "chrome" in user_input_lower:
        return open_chrome()

    if "create file" in user_input_lower:
        return create_file()

    if "search" in user_input_lower:
        query = user_input_lower.replace("search", "")
        return search_web(query)

    return query_llm(user_input)