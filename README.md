# Multi-Persona AI Chatbot with Google Gemini 1.5

## Overview

This project is a **multi-persona AI chatbot** that leverages the power of **Google's Gemini 1.5 Flash-8B model**. It offers users the ability to interact with three unique personas, each providing a distinct tone and style of responses:

- **Viper** (Angry GPT): Sarcastic and aggressive tone.
- **Seraphina**: Balanced and humorous responses.
- **Elysia**: Seductive and alluring tone.

The chatbot is built with **Flask** as the backend and utilizes **HTML**, **CSS**, and **JavaScript** for a simple yet interactive frontend.

---

## Features

- **Three distinct personas** for a unique conversational experience.
- **Gemini 1.5 API** integration for state-of-the-art natural language processing.
- **Real-time communication** with asynchronous responses.
- **Easy-to-use interface** with persona selection and text input.
- **Customizable prompts** for each persona, ensuring accurate tone and response style.

---

## Technologies Used

- **Python** (Backend)
- **Flask** (Web Framework)
- **Google Gemini 1.5 API** (AI Model)
- **HTML** & **CSS** (Frontend)
- **JavaScript** (AJAX for real-time interaction)
- **JQuery** (For AJAX requests)

---

## Installation & Setup

### Prerequisites

Before getting started, ensure you have the following:

- **Python 3.7+** installed.
- **pip** (Python Package Installer).

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/multi-persona-ai-chatbot.git
    cd multi-persona-ai-chatbot
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set up the **Gemini API key** from Google:
    - Visit the [Google Cloud Console](https://console.cloud.google.com/), create a project, and enable the Gemini API.
    - Set the API key as an environment variable:
      - On Windows:
        ```bash
        set GEMINI_API_KEY=your_api_key
        ```
      - On macOS/Linux:
        ```bash
        export GEMINI_API_KEY=your_api_key
        ```

6. Run the Flask application:
    ```bash
    python app.py
    ```

7. Open a web browser and go to `http://127.0.0.1:5000/` to interact with the chatbot.

---

## How It Works

- **Choose a Persona**: Select from one of the three personas available: **Viper**, **Seraphina**, or **Elysia**.
- **Enter a Message**: Type a message and press the "Send" button to communicate with the selected persona.
- **Get a Response**: The chatbot will respond in real-time, with each persona using a unique conversational tone.

---

## Example Questions

- **Viper (Angry GPT)**:
  - "Why is technology so overrated?"
  - "Tell me something annoying."
  - "What’s your opinion on AI?"

- **Seraphina**:
  - "What's a good joke?"
  - "How do you see the future of tech?"
  - "What's your take on machine learning?"

- **Elysia**:
  - "Do you believe in love?"
  - "What's the most romantic thing you've heard?"
  - "Tell me your secrets."

---

## License

This project is open-source and licensed under the [MIT License](LICENSE).

---

## Contact

For any inquiries or issues, feel free to reach out to me through GitHub or via email at [your_email@example.com].

---

Enjoy chatting with the AI personas and have fun exploring this project!
