from agents.tools import open_notepad, open_chrome, create_file, search_web
from llm.ollama_client import query_llm

def decide_and_act(user_input):
    # 1. Define the System Prompt to guide the LLM's decision
    prompt = f"""
    You are the brain of an AI assistant named Jarvis. 
    Your job is to look at the user's request and pick the best tool from this list:
    - notepad: Use when the user wants to open a text editor or write notes.
    - chrome: Use when the user wants to open a browser or go to Google.
    - create_file: Use when the user wants to create, save, or make a new file.
    - search: Use when the user wants to look something up on the internet.
    - none: Use for general conversation or questions that don't need a tool.

    User request: "{user_input}"
    
    Respond with ONLY the name of the tool.
    """
    
    # 2. Get the decision from your local Ollama model
    decision = query_llm(prompt).lower()

    # 3. Route to the correct tool based on the LLM's choice
    if "notepad" in decision:
        return open_notepad()
    
    elif "chrome" in decision:
        return open_chrome()
    
    elif "create_file" in decision:
        return create_file()
    
    elif "search" in decision:
        # For search, we still need the original input to know what to search for
        return search_web(user_input)
    
    else:
        # Default to standard conversation if no tool matches
        return query_llm(user_input)