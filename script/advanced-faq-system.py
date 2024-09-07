import openai
import re

# Set the OpenAI API key (REPLACE WITH YOUR OWN API KEY)
openai.api_key = 'your-api-key-here'

# Define a function to get a response from the ChatGPT model
def get_chatgpt_response(prompt, temperature=0.7):
    # Use the OpenAI API to generate a response to the given prompt
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=150,
        temperature=temperature,  
    )
    # Return the text of the response, stripped of any leading or trailing whitespace
    return response.choices[0].text.strip()

# Define a dictionary to store FAQs and their corresponding answers
faqs = {
    "What is the company's mission?": "Our mission is to provide innovative solutions to our customers.",
    "How do I contact customer support?": "You can contact us at support@example.com or call us at 1-800-EXAMPLE.",
    "What are the company's hours of operation?": "We are open Monday through Friday, 9am to 5pm EST."
}

# Define a function to handle user input and provide a response
def handle_user_input(user_input):
    # Check if the user input matches any of the FAQs
    for question, answer in faqs.items():
        # Use regular expressions to match the user input to the FAQ question
        if re.search(question, user_input, re.IGNORECASE):
            # Return the answer to the FAQ
            return answer
    
    # If the user input doesn't match any of the FAQs, use the ChatGPT model to generate a response
    chatgpt_prompt = f"User asked: {user_input}. Provide a helpful response."
    response = get_chatgpt_response(chatgpt_prompt)
    return response

# Define a function to run the FAQ system
def faq_system():
    print("Welcome to our FAQ system!")
    while True:
        # Get user input
        user_input = input("Enter your question: ")
        
        # Handle the user input and provide a response
        response = handle_user_input(user_input)
        print(f"Response: {response}")
        
        # Ask the user if they have another question
        another_question = input("Do you have another question? (yes/no): ")
        if another_question.lower()!= "yes":
            break

if __name__ == "__main__":
    faq_system()
