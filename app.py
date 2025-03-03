import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

# Load API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("API key is missing! Set GEMINI_API_KEY environment variable.")

# Configure the API
genai.configure(api_key=GEMINI_API_KEY)

# Set up model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Define unique prompt styles for each persona
persona_prompts = {
    "viper": "Respond in a sarcastic, aggressive, and condescending tone. Be rude and short.",
    "seraphina": "Respond in a balanced and humorous tone. Use wit and light humor in your answers.",
    "elysia": "Respond in a seductive and alluring tone. Be charming and enticing in your responses."
}

# Initialize models for different personas with unique prompts
personas = {
    "viper": genai.GenerativeModel(model_name="gemini-1.5-flash-8b", generation_config=generation_config),
    "seraphina": genai.GenerativeModel(model_name="gemini-1.5-flash-8b", generation_config=generation_config),
    "elysia": genai.GenerativeModel(model_name="gemini-1.5-flash-8b", generation_config=generation_config)
}

# Start chat sessions for each persona
chat_sessions = {persona: model.start_chat(history=[]) for persona, model in personas.items()}

# Start Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    persona = request.form['persona']  # Get selected persona from user
    
    if not user_input:
        return jsonify({"response": "Please enter a message."})
    
    if persona not in chat_sessions:
        return jsonify({"response": "Invalid persona selected."})

    # Modify user input based on persona
    persona_prompt = persona_prompts[persona]
    prompt_input = f"{persona_prompt}\nUser: {user_input}\nAI:"

    # Get AI response based on the modified prompt
    response = chat_sessions[persona].send_message(prompt_input)
    
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(debug=True)
