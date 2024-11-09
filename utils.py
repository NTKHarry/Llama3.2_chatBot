from groq import Groq
from datetime import datetime
import json
import markdown2  # To convert Markdown to HTML
import base64
import os
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

# Lấy API key từ biến môi trường
api_key = os.getenv("API_KEY")

# Initialize the Groq client with your API key
client = Groq(api_key=api_key)

class ChatHistory:
    def __init__(self):
        self.messages = []
    def init(self):
        self.messages.append({"role": "system", "content": "You are a helpful assistant."})
    def add_message(self, role, content):
        # Get the current time in ISO format (for logging or saving)
        current_time = datetime.now().isoformat()
        self.messages.append({"role": role, "content": content})  # Add time for internal use only
    
    def get_history(self):
        # Return the complete history including all fields
        return self.messages 
    

chat_history = ChatHistory()
chat_history.init()


def send_prompt(client, prompt):
    if(prompt == ""):
        prompt = "No message"
    #tạo list content gồm các loại dữ liệu prompt, image
    chat_history.add_message("user", prompt)
    # Gửi prompt đến LLM
    completion = client.chat.completions.create(
        model="llama-3.2-90b-vision-preview",
        messages=chat_history.get_history(), # Get the filtered history
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    ai_response = completion.choices[0].message.content
    chat_history.add_message("assistant", ai_response)
    
    filename = "history.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(chat_history.messages, f, ensure_ascii=False, indent=4)  # Save the full history including timestamps
    
    # Convert Markdown to HTML with code highlighting
    ai_response_html = markdown2.markdown(ai_response, extras=["fenced-code-blocks", "highlightjs-lang"])
    return ai_response_html
