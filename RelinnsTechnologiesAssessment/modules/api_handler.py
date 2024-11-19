from utils.imports import openai
from config.settings import OPENAI_API_KEY

# Set up the OpenAI API key
openai.api_key = OPENAI_API_KEY

def get_chatgpt_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=prompt,
            max_tokens=150,
            n=1,           
            stop=None,      
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error communicating with OpenAI API: {e}")
        return None
