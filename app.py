from flask import Flask, render_template, request, jsonify
from groq import Groq
from utils import * 
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Đảm bảo thư mục tồn tại
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def receive_message():
    data = request.get_json()
    user_input = data.get('message')
    if user_input:
        bot_response = send_prompt(client, user_input)
        return jsonify({"response": bot_response})
    return jsonify({"response": "Error: Message not provided"}), 400


@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'response': 'No image part'}), 400
    file = request.files['image']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)


# @app.route('/add_urls', methods=['POST'])  # New route for multiple URLs
# def add_urls():
#     path = r'D:\tfolder\codingFile\AIlearning\projects\CHatbot\data'
#     urls = []
#     data = request.get_json()
#     new_urls = data.get('urls')
#     if new_urls:
#         urls.extend(new_urls)  # Append new URLs to the existing list
#         with open(os.path.join(path, 'urls.txt'), 'w') as file:
#             for u in urls:
#                 file.write(u + '\n')  # Write each URL on a new line
#         return jsonify({'response': 'URLs added successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
