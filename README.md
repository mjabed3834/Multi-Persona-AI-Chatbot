Multi-Persona AI Chatbot with Google Gemini 1.5

Overview:
This project is a multi-persona AI chatbot that leverages Google's Gemini 1.5 Flash-8B model. Users can interact with three unique personas, each offering a distinct conversational style:

- Viper (Angry GPT): Sarcastic and aggressive tone.
- Seraphina: Balanced and humorous responses.
- Elysia: Seductive and alluring tone.

The chatbot is built using Flask for the backend and utilizes HTML, CSS, and JavaScript for the frontend.

---

Features:
- Three distinct personas for a unique chatbot experience.
- Integration with Google Gemini 1.5 API for advanced natural language processing.
- Real-time interaction with asynchronous responses.
- User-friendly interface with persona selection.
- Customizable prompts for accurate persona-based responses.

---

Technologies Used:
- Python (Backend)
- Flask (Web Framework)
- Google Gemini 1.5 API (AI Model)
- HTML, CSS (Frontend)
- JavaScript, jQuery (AJAX for real-time communication)

---

Installation & Setup:

Prerequisites:
- Python 3.7+ installed
- pip (Python Package Installer)

Steps:
1. Clone the repository:
   git clone https://github.com/mjabed3834/multi-persona-ai-chatbot.git
   cd multi-persona-ai-chatbot

2. Create a virtual environment:
   python -m venv venv

3. Activate the virtual environment:
   - Windows:
     venv\Scripts\activate
   - macOS/Linux:
     source venv/bin/activate

4. Install dependencies:
   pip install -r requirements.txt

5. Set up the Gemini API key:
   - Obtain the API key from Google Cloud Console.
   - Set the API key as an environment variable:
     - Windows:
       set GEMINI_API_KEY=your_api_key
     - macOS/Linux:
       export GEMINI_API_KEY=your_api_key

6. Run the application:
   python app.py

7. Open a browser and go to:
   http://127.0.0.1:5000/

---

How It Works:
- Select a persona: Viper, Seraphina, or Elysia.
- Enter a message and send it.
- Receive a response based on the selected persona’s style.

---

Example Questions:

Viper (Angry GPT):
- "Why is technology so overrated?"
- "Tell me something annoying."
- "What’s your opinion on AI?"

Seraphina:
- "What's a good joke?"
- "How do you see the future of tech?"
- "What's your take on machine learning?"

Elysia:
- "Do you believe in love?"
- "What's the most romantic thing you've heard?"
- "Tell me your secrets."

---

License:
This project is open-source and licensed under the MIT License.

---

Contact:
For inquiries or issues, reach out via:
- GitHub: https://github.com/mjabed3834
- Email:jabedhosen.cse@gmail.com

Enjoy chatting with the AI personas!
