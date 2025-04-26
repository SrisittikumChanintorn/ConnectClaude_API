import os
import anthropic
from anthropic_chatbot import Normal_LLM



# Initialize Necessary Parameters
instruction = "You are a world-class poet. Respond only with short poems."
model_name = "claude-3-5-sonnet-20240620"
max_tokens = 1000
api_key = 'YOUR_API_KEY'  # Replace with your actual OpenAI API key


# Initialize the Anthropic API client
llm1 = anthropic.Anthropic(api_key=api_key)


# Start the chat loop
chat_history = []
query = None  # Initialize query to avoid potential reference error

while True:
    if not query:
        query = input("User: ")
    if query in ['quit', 'q', 'exit']:
        break
    result = Normal_LLM(query, llm1, chat_history, model_name=model_name, instruction=instruction,max_tokens=max_tokens)
    print("Chatbot:", result)

    chat_history.append((query, result))
    query = None