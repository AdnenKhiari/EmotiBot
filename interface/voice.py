import speech_recognition as sr
import pyttsx3


def text_to_speech(text: str, rate: int = 150, volume: float = 0.9):
    """Reads the given text aloud using TTS."""
    tts_engine = pyttsx3.init()
    tts_engine.setProperty('rate', rate)  # Set speaking rate
    tts_engine.setProperty('volume', volume)  # Set volume
    tts_engine.say(text)
    tts_engine.runAndWait()

def get_user_input_voice() -> str:
    """Gets user input through voice recognition."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            query = recognizer.recognize_google(audio)  # Recognize speech using Google API
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you please repeat?")
            return get_user_input_voice()  # Retry on failure
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""