from agents.tools import open_notepad, open_chrome, create_file, search_web, get_time # <-- IMPORT NEW TOOL
from llm.ollama_client import query_llm_with_context 

# State variable to track the planned action
pending_action = None

def decide_and_act(user_input):
    global pending_action
    user_input_low = user_input.lower()

    # --- FAST PATH FOR TIME ---
    # We bypass the LLM entirely if you just want to know the time.
    if "time" in user_input_low and "what" in user_input_low:
        return get_time()

    # 1. Confirmation: Execute only if the user says "Yes" to a plan
    if pending_action and any(word in user_input_low for word in ["yes", "proceed", "go ahead", "do it"]):
        action = pending_action
        pending_action = None 
        
        if action == "notepad": return open_notepad()
        if action == "chrome": return open_chrome()
        if action == "create_file": return create_file()
        if "search" in action: 
            return search_web(action.replace("search", "").strip())
        
        return "Task complete, Boss."

    # 2. Planning: Let F.R.I.D.A.Y. explain what she wants to do
    response = query_llm_with_context(user_input)
    
    # 3. Intelligence: Stage the correct tool based on the context
    if "notepad" in user_input_low: pending_action = "notepad"
    elif "chrome" in user_input_low or "browser" in user_input_low: pending_action = "chrome"
    elif "file" in user_input_low: pending_action = "create_file"
    elif "search" in user_input_low: pending_action = f"search {user_input_low}"
    
    return response