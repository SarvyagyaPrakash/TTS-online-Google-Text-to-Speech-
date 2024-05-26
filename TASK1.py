# To run TTS offline, the system must have required available offline voices and language.
# By default, only "English" Translation will work when system is offline.
# Online TTS work for every language. 
# Around 11 languages are supported in online TTS system

from gtts import gTTS
import pyttsx3

def tts_google(text, lang='en', rate=1.0):
    try:
        tts = gTTS(text=text, lang=lang, slow=(rate < 1.0))
        tts.save("answer.mp3")
        print("Audio saved as answer.mp3 using Google TTS")
    except Exception as e:
        print(f"Error using Google TTS: {e}")
    # To customize the speech synthesis according to the user.
def tts_offline(text, lang='en', rate=200, volume=1.0, voice_id=None):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)
        voices = engine.getProperty('voices')

        # Mapping language to corresponding voice keyword
        lang_to_voice_keyword = {
            'en': 'english',
            'es': 'spanish',
            'hi': 'hindi',
            'fr': 'french',
            'de': 'german',
            'zh': 'chinese',
            'ja': 'japanese',
            'it': 'italian',
            'pt': 'portuguese',
            'ru': 'russian',
            'ko': 'korean'
        }

        selected_voice = None

        if lang in lang_to_voice_keyword:
            for voice in voices:
                if lang_to_voice_keyword[lang] in voice.name.lower():
                    selected_voice = voice.id
                    break
        # Prompt to choose voice
        if selected_voice:
            engine.setProperty('voice', selected_voice)
        elif voice_id:
            engine.setProperty('voice', voice_id)
        else:
            print(f"No default voice found for language '{lang}', using system default voice.")
        # Saving audio file
        engine.save_to_file(text, "answer.wav")
        engine.runAndWait()
        print("Audio saved as answer.wav using offline TTS")
    except Exception as e:
        print(f"Error using offline TTS: {e}")

def list_offline_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for idx, voice in enumerate(voices):
        print(f"Voice {idx}: {voice.name}, ID: {voice.id}, Language: {voice.languages}")
        # To Choose TTS type
if __name__ == "__main__":
    print("Select TTS Type:")
    print("1. Online TTS (By Google)")
    print("2. Offline TTS")
    choice = input("Enter choice (1/2): ")

    text = input("Enter text to convert to speech: ")
    # Final prompt and display
    if choice == '1':
        print("Supported Languages for Online TTS:")
        print("English (en), Spanish (es), Hindi (hi), French (fr), German (de), Chinese (zh), Japanese (ja), Italian (it), Portuguese (pt), Russian (ru), Korean (ko)")
        lang = input("Enter language code (e.g., 'en' for English, 'es' for Spanish, 'hi' for Hindi, etc.): ")
        rate = float(input("Enter speaking rate (default is 1.0, lower is slower, higher is faster): "))
        tts_google(text, lang, rate)
    elif choice == '2':
        print("Available offline voices:")
        list_offline_voices()
        lang = input("Enter language code (e.g., 'en' for English, 'es' for Spanish, 'hi' for Hindi, 'fr' for French, 'de' for German, 'zh' for Chinese, 'ja' for Japanese, 'it' for Italian, 'pt' for Portuguese, 'ru' for Russian, 'ko' for Korean): ")
        rate = int(input("Enter speaking rate (default is 200 words per minute): "))
        volume = float(input("Enter volume (0.0 to 1.0, default is 1.0): "))
        voice_id = input("Enter voice ID (leave blank for default): ")
        tts_offline(text, lang, rate, volume, voice_id if voice_id else None)
    else:
        print("Invalid choice")

