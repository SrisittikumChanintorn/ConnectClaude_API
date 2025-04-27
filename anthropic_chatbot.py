def Normal_LLM(query, llm1, chat_history, model_name="", instruction="",max_tokens=1000):

    full_query = "\n".join([f"User: {q}\nAssistance: {a}" for q, a in chat_history])
    full_query += f"\nUser: {query}"

    chain1 = llm1.messages.create(
        model=model_name,
        max_tokens=max_tokens,
        system=instruction,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": full_query
                    }
                ]
            }
        ]
    )

    result = chain1.content[0].text

    return result



