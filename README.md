# LLaMA 3.2 ChatBot with Flask

A chatbot application leveraging the **LLaMA 3.2** language model through the **Groq API**. This project sets up a local web application using **Flask** for the backend and **HTML, CSS** for the frontend.

## Features

- Connects and interacts with the LLaMA 3.2 language model via the Groq API.
- Provides a simple, user-friendly web interface for chat interactions.
- Designed to be extendable and customizable for various use cases.

## Requirements

- **Python 3.x** is required for running this application.
- **Groq API Key** is necessary for accessing the LLaMA 3.2 model through Groq. Obtain an API key by registering on the Groq platform.

## Installation and Setup

To set up the project locally, follow these steps:

1. **Clone the Repository**

   Clone this repository to a local machine:
   ```bash
   git clone https://github.com/NTKHarry/Llama3.2_chatBot.git
   cd llama3.2-chatbot
    ```

2. **Install Dependencies**

   Install the required libraries by running the following command:
   ```bash
   pip install -r requirements.txt
    ```

3. **Configure the API Key**

    Create a `.env` file in the root directory
    
    In the `.env` file, add your Groq API key:
     ```plaintext
     API_KEY=your_groq_api_key_here
     ```
    Replace `your_groq_api_key_here` with your actual API key obtained from Groq.

    This `.env` file will be used to securely store the API key, and it will be loaded by the application at runtime.

4. **Run the Application**

   To start the Flask application, run the following command:
   ```bash
   python app.py
