import openai

# Set the OpenAI API key (REPLACE WITH YOUR OWN API KEY)
openai.api_key = 'your-api-key-here'

# Define a function to get a response from the ChatGPT model
def get_chatgpt_response(prompt, temperature=0.7):
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=150,
        temperature=temperature,  
    )
    return response.choices[0].text.strip()

# Define a function to run the chatbot
def financial_chatbot():
    print("Welcome to our financial services chatbot!")
    print("Please select a topic or type your own question:")

    topics = [
        "Investment advice",
        "Retirement planning",
        "Credit score management",
        "Mortgage options"
    ]

    while True:
        print("\nOptions:")
        for i, topic in enumerate(topics):
            print(f"{i+1}. {topic}")
        print("5. Type your own question")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "5":
            user_prompt = input("Enter your question: ")
            response = get_chatgpt_response(user_prompt)
            print(f"ChatGPT Response:\n{response}")
        elif choice == "6":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(topics):
            topic = topics[int(choice) - 1]
            if topic == "Investment advice":
                investment_prompt = "What are some general investment strategies for a long-term portfolio?"
                response = get_chatgpt_response(investment_prompt)
                print(f"ChatGPT Response:\n{response}")
            elif topic == "Retirement planning":
                retirement_prompt = "What are some key factors to consider when planning for retirement?"
                response = get_chatgpt_response(retirement_prompt)
                print(f"ChatGPT Response:\n{response}")
            elif topic == "Credit score management":
                credit_prompt = "What are some ways to improve my credit score?"
                response = get_chatgpt_response(credit_prompt)
                print(f"ChatGPT Response:\n{response}")
            elif topic == "Mortgage options":
                mortgage_prompt = "What are some common types of mortgages and their benefits?"
                response = get_chatgpt_response(mortgage_prompt)
                print(f"ChatGPT Response:\n{response}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    financial_chatbot()
