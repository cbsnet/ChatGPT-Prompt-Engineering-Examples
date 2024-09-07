import openai

openai.api_key = ''

def get_chatgpt_response(prompt, temperature=0.7):
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=150,
        temperature=temperature,  
    )
    return response.choices[0].text.strip()

def chatbot():
    print("Welcome to our customer support chatbot!")
    print("Please select a query or type your own question:")

    prompts = [
        "What is your return policy?",
        "How do I track my order?",
        "Can I get a refund?"
    ]

    while True:
        print("\nOptions:")
        for i, prompt in enumerate(prompts):
            print(f"{i+1}. {prompt}")
        print("4. Type your own question")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "4":
            user_prompt = input("Enter your question: ")
            response = get_chatgpt_response(user_prompt)
            print(f"ChatGPT Response:\n{response}")
        elif choice == "5":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(prompts):
            prompt = prompts[int(choice) - 1]
            response = get_chatgpt_response(prompt)
            print(f"ChatGPT Response:\n{response}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    chatbot()
