# Import the OpenAI library, which provides an interface to the OpenAI API
import openai

# Set the OpenAI API key (REPLACE WITH YOUR OWN API KEY)
openai.api_key = 'your-api-key-here'

# Define a function to get a response from the ChatGPT model
def get_chatgpt_response(prompt, temperature=0.7):
    # Use the OpenAI API to generate a response to the given prompt
    # The 'text-davinci-003' engine is a specific model used for text generation
    # The'max_tokens' parameter limits the length of the response
    # The 'temperature' parameter controls the creativity of the response
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=150,
        temperature=temperature,  
    )
    # Return the text of the response, stripped of any leading or trailing whitespace
    return response.choices[0].text.strip()

# Define a function to run the chatbot
def chatbot():
    # Print a welcome message to the user
    print("Welcome to our customer support chatbot!")
    print("Please select a query or type your own question:")

    # Define a list of predefined prompts for the user to choose from
    prompts = [
        "What is your return policy?",
        "How do I track my order?",
        "Can I get a refund?"
    ]

    # Run the chatbot in a loop until the user chooses to quit
    while True:
        # Print the list of options to the user
        print("\nOptions:")
        for i, prompt in enumerate(prompts):
            print(f"{i+1}. {prompt}")
        print("4. Type your own question")
        print("5. Quit")

        # Get the user's choice
        choice = input("Enter your choice: ")

        # If the user chooses to type their own question
        if choice == "4":
            # Get the user's question
            user_prompt = input("Enter your question: ")
            # Get a response from the ChatGPT model
            response = get_chatgpt_response(user_prompt)
            # Print the response to the user
            print(f"ChatGPT Response:\n{response}")
        # If the user chooses to quit
        elif choice == "5":
            # Break out of the loop and end the chatbot
            break
        # If the user chooses a predefined prompt
        elif choice.isdigit() and 1 <= int(choice) <= len(prompts):
            # Get the chosen prompt
            prompt = prompts[int(choice) - 1]
            # Get a response from the ChatGPT model
            response = get_chatgpt_response(prompt)
            # Print the response to the user
            print(f"ChatGPT Response:\n{response}")
        # If the user enters an invalid choice
        else:
            # Print an error message and ask the user to try again
            print("Invalid choice. Please try again.")

# If this script is run directly (not imported as a module), run the chatbot
if __name__ == "__main__":
    chatbot()
