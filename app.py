# app.py
# Import necessary libraries
import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import speech_recognition as sr
import io

# --- App Configuration ---
st.set_page_config(
    page_title="Tour-Talker AI Voice Assistant",
    page_icon="✈️",
    layout="centered",
)

# --- App Title and Description ---
st.title("Tour-Talker AI Voice Assistant ✈️")
st.markdown("Your friendly AI travel guide. Press 'Start' to begin a continuous conversation.")

# --- Session State Initialization ---
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'language' not in st.session_state:
    st.session_state.language = 'en'
if 'talking' not in st.session_state:
    st.session_state.talking = False # Controls the conversation loop

# --- Language Selection ---
languages = {
    'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de',
    'Italian': 'it', 'Hindi': 'hi', 'Marathi': 'mr', 'Japanese': 'ja', 'Korean': 'ko',
}
selected_language_name = st.selectbox("Select Language:", list(languages.keys()))
st.session_state.language = languages[selected_language_name]

# --- API Key Configuration ---
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
    api_key_configured = True
except (KeyError, Exception):
    st.error("🚨 Gemini API Key not found. Please add it to your Streamlit secrets.")
    api_key_configured = False

# --- Core Functions ---
def listen_and_transcribe(r, source, language='en-US'):
    """Captures and transcribes audio. Re-uses recognizer and source."""
    st.info("Listening...")
    try:
        audio = r.listen(source, timeout=5, phrase_time_limit=15)
        st.success("Audio captured!")
        text = r.recognize_google(audio, language=language)
        st.write(f"You said: {text}")
        return text
    except sr.WaitTimeoutError:
        st.warning("Listening timed out. Say something or press 'Stop'.")
        return None
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        st.error(f"Speech recognition request failed; {e}")
        st.session_state.talking = False
        return None

def get_gemini_response(query, language):
    """Gets a response from the Gemini API."""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        prompt = f"You are a helpful and friendly travel assistant named Tour-Talker. Provide a concise and informative response to the following query, in {selected_language_name}: '{query}'"
        
        st.session_state.messages.append({"role": "user", "parts": [prompt]})
        response = model.generate_content(st.session_state.messages)
        st.session_state.messages.append({"role": "model", "parts": [response.text]})
        
        return response.text
    except Exception as e:
        st.error(f"An error occurred with the Gemini API: {e}")
        st.session_state.talking = False
        return None

def text_to_speech_bytes(text, lang='en'):
    """Converts text to speech and returns the audio data as bytes."""
    if not text:
        return None
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        return audio_fp
    except Exception as e:
        st.error(f"An error occurred during text-to-speech: {e}")
        st.session_state.talking = False
        return None

# --- Main App Logic ---
col1, col2 = st.columns(2)

with col1:
    if st.button("Start Conversation 🎙️"):
        if api_key_configured:
            st.session_state.talking = True
        else:
            st.warning("Please configure your API key first.")

with col2:
    if st.button("Stop Conversation ⏹️"):
        st.session_state.talking = False
        st.rerun()

if st.session_state.talking:
    st.info("Conversation in progress... Press 'Stop' to end.")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        while st.session_state.talking:
            lang_code = f"{st.session_state.language}-IN" if st.session_state.language in ['hi', 'mr'] else f"{st.session_state.language}-US"
            user_query = listen_and_transcribe(r, source, language=lang_code)
            
            if user_query:
                with st.spinner("Tour-Talker is thinking..."):
                    gemini_response = get_gemini_response(user_query, st.session_state.language)
                
                if gemini_response:
                    st.write(f"Tour-Talker says: {gemini_response}")
                    audio_bytes = text_to_speech_bytes(gemini_response, lang=st.session_state.language)
                    if audio_bytes:
                        st.audio(audio_bytes, format='audio/mp3', start_time=0)

# --- Display Chat History ---
st.subheader("Conversation History")
if not st.session_state.messages:
    st.info("Your conversation will appear here.")
else:
    for msg in st.session_state.messages:
        if msg['role'] == 'user':
            try:
                original_query = msg['parts'][0].split("'")[1]
                st.chat_message("user").write(f"You: {original_query}")
            except IndexError:
                pass
        elif msg['role'] == 'model':
            st.chat_message("assistant").write(f"Tour-Talker: {msg['parts'][0]}")
