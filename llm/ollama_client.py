import ollama

chat_history = []

def query_llm_with_context(user_input):
    # Add user message to history
    chat_history.append({'role': 'user', 'content': user_input})
    
    system_msg = {
        'role': 'system', 
        'content': (
            "You are F.R.I.D.A.Y., a highly advanced AI. Your tone is professional and efficient. "
            "Refer to the user as 'Boss' or 'Sir'. "
            "IMPORTANT: When given a task, outline the steps you will take and ask: 'Shall I proceed, Boss?'"
        )
    }

    try:
        response = ollama.chat(
            model='llama3',
            messages=[system_msg] + chat_history[-6:], # Send last 3 exchanges
        )
        
        assistant_reply = response['message']['content']
        chat_history.append({'role': 'assistant', 'content': assistant_reply})
        return assistant_reply
    except Exception as e:
        return f"Communication breakdown, Sir: {str(e)}"