import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key-here'

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # or another model like "gpt-3.5-turbo"
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,  # Controls creativity; higher is more random
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    # Example prompt
    example_prompt = """
    You are a customer support agent. A customer asks for details about your return policy. Provide a concise and friendly response.
    """

    # Get the response from ChatGPT
    result = get_chatgpt_response(example_prompt)
    print(f"ChatGPT Response:\n{result}")

