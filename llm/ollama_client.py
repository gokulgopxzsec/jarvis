import requests
import ollama

def query_llm(prompt):
    # Defining the persona and constraints for the local model
    system_instruction = "You are Jarvis, a helpful AI assistant. Keep responses concise and professional."
    full_prompt = f"{system_instruction}\n\nUser: {prompt}\nJarvis:"
    
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3", # Ensure this matches your local Ollama model name
                "prompt": full_prompt, # Use the combined prompt here
                "stream": False
            },
            timeout=60
        )

        if response.status_code != 200:
            return "LLM error"

        return response.json().get("response", "")

    except Exception as e:
        return f"Error contacting LLM: {str(e)}"
    
chat_history = []

def query_llm_with_context(user_input):
    # Add user message to history
    chat_history.append({'role': 'user', 'content': user_input})
    
    # System prompt for F.R.I.D.A.Y. persona
    system_msg = {
        'role': 'system', 
        'content': "You are F.R.I.D.A.Y., a highly advanced AI. Your tone is professional, efficient, and slightly witty. Refer to the user as 'Boss' or 'Sir'. Always analyze the context of the conversation before acting."
    }

    response = ollama.chat(
        model='llama3',
        messages=[system_msg] + chat_history[-5:], # Send last 5 exchanges
    )
    
    assistant_reply = response['message']['content']
    chat_history.append({'role': 'assistant', 'content': assistant_reply})
    return assistant_reply