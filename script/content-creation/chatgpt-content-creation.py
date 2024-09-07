import openai
import json
import os
from typing import List, Dict

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog_ideas(topic: str, num_ideas: int = 5) -> List[str]:
    prompt = f"Generate {num_ideas} blog post ideas about {topic}. Provide only the titles."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative content strategist."},
            {"role": "user", "content": prompt}
        ]
    )
    ideas = response.choices[0].message.content.strip().split("\n")
    return [idea.lstrip("1234567890-. ") for idea in ideas]

def create_outline(title: str) -> List[str]:
    prompt = f"Create a detailed outline for a blog post titled '{title}'. Include main sections and subsections."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an experienced blog post outliner."},
            {"role": "user", "content": prompt}
        ]
    )
    outline = response.choices[0].message.content.strip().split("\n")
    return [item.strip() for item in outline if item.strip()]

def write_introduction(title: str, outline: List[str]) -> str:
    prompt = f"Write an engaging introduction for a blog post titled '{title}'. Use the following outline as context: {json.dumps(outline)}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a skilled blog post writer."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def automate_content_creation(topic: str) -> Dict[str, Dict[str, str]]:
    result = {}
    
    # Generate blog post ideas
    ideas = generate_blog_ideas(topic)
    
    for idea in ideas:
        # Create outline for each idea
        outline = create_outline(idea)
        
        # Write introduction for each idea
        introduction = write_introduction(idea, outline)
        
        result[idea] = {
            "outline": outline,
            "introduction": introduction
        }
    
    return result

def main():
    topic = input("Enter a topic for blog post ideas: ")
    content = automate_content_creation(topic)
    
    # Save the results to a JSON file
    with open("automated_content.json", "w") as f:
        json.dump(content, f, indent=2)
    
    print(f"Content creation automated for topic: {topic}")
    print(f"Results saved to automated_content.json")

if __name__ == "__main__":
    main()
