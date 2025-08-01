Tour-Talker AI Voice Assistant ✈️🎙️
Tour-Talker is an interactive, multi-lingual AI-powered travel assistant. Built with Python and Streamlit, it leverages the power of Google's Gemini Pro model to provide real-time, voice-based answers to all your travel queries. Just select your language, ask a question with your voice, and get an instant, spoken response.

✨ Live Demo Link ✨
(Replace the link above with your actual Streamlit Cloud URL after deployment)

🚀 Features
Voice-to-Voice Interaction: Ask questions using your microphone and receive audible responses.

Multi-Lingual Support: Communicate in various languages, including English, Spanish, French, Hindi, Marathi, and more.

Powered by Google Gemini: Utilizes the state-of-the-art Gemini Pro model for intelligent, context-aware, and accurate answers.

Intuitive Web Interface: A clean and user-friendly interface built with Streamlit.

Conversation History: Keeps track of your current conversation with the assistant.

Ready for Deployment: Designed to be easily deployed on Streamlit Cloud.

📸 Application Preview
(It is highly recommended to add a screenshot or a GIF of your application here. You can drag and drop the image into your GitHub README editor.)

🛠️ Technologies Used
Backend: Python

Web Framework: Streamlit

AI/LLM: Google Gemini Pro API (google-generativeai)

Speech-to-Text: Google Speech Recognition API (SpeechRecognition)

Text-to-Speech: Google Text-to-Speech (gTTS)

Audio Handling: PyDub, Pyglet, PyAudio

⚙️ Setup and Local Installation
To run this project on your local machine, follow these steps:

1. Clone the Repository

git clone https://github.com/your-username/tour-talker.git
cd tour-talker

2. Create a Virtual Environment
It's recommended to create a virtual environment to manage project dependencies.

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
Install all the required packages from the requirements.txt file.

pip install -r requirements.txt

4. Set Up Your API Key
The application uses Streamlit's secrets management for the deployed version. For local development, create a file named .streamlit/secrets.toml and add your API key to it:

# .streamlit/secrets.toml
GEMINI_API_KEY = "YOUR_API_KEY_HERE"

Replace YOUR_API_KEY_HERE with your actual Gemini API key.

5. Run the Application
Launch the Streamlit app from your terminal:

streamlit run app.py

The application should now be running in your web browser!

☁️ Deployment
This application is ready to be deployed on Streamlit Cloud.

Push your code to a public GitHub repository.

Follow the instructions in the Streamlit Cloud dashboard to deploy from the repository.

Add your GEMINI_API_KEY to the app's secrets in the Streamlit Cloud settings, as described in the application instructions.

👤 Author
Shailesh Bothe

GitHub

LinkedIn