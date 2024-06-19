import speech_recognition as sr
from chatGPT import askGPT
import pyaudio
import wave
import keyboard
from secret_key import AZURE_KEY
from google_calendar_integration import send_calendar_notification
from standup_analyzer import analyze_weekly_data
from languages import languages
# import assemblyai as aai
import openai
import os
from secret_key import API_KEY

MICROPHONE = 0 
AUDIOSTREAM = 2
FORMAT = pyaudio.paInt16  
CHANNELS = 2              
RATE = 44100             
CHUNK = 1024              
RECORD_SECONDS = 0        
WAVE_OUTPUT_FILENAME = "output.wav"
LANGUAGE_INPUT = "en-US"
# aai.settings.api_key = "8362156a30454b48864c00f54fe1a33c"
# transcriber = aai.Transcriber()

def speechToText(device):
    print("Listening... ")
    print("Press 'q' to stop.")
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK,input_device_index=device)
    frames = []

    print("Recording started...")
    while True:
        data = stream.read(CHUNK)
        frames.append(data)

        if keyboard.is_pressed("q"):
            print("done...")
            break
        if RECORD_SECONDS and len(frames) / (RATE / CHUNK) >= RECORD_SECONDS:
            break

    print("Recording stopped.")

    stream.stop_stream()
    stream.close()
    audio.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    print("Audio saved to", WAVE_OUTPUT_FILENAME)


# client = OpenAI(API_KEY)
openai.api_key = "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"

def audioToText(language):
    audio_file = open("./output.wav", "rb")
    if language != "en-US" and language != "en-IN":
        prompt = f"Translate the following {language} audio to English transcription"
    else:
        prompt = "Transcribe the following audio"
    response = openai.audio.translations.create(
        model="whisper-1",
        file=audio_file,
        prompt = prompt,
    )
    # print("API Response:", response)  # Debugging print
    text = response.text
    # print("Transcribed Text:", text)  # Debugging print
    return text


def main():
    while True: 
        print("Available Languages:")
        for index, language in enumerate(languages, start=1):
            print(f"{index}. {language}")

        selected_language = int(input("Enter the number corresponding to your preferred language: "))
        if selected_language < 1 or selected_language > len(languages):
            print("Invalid input! Please try again.")
        else:
            language_name = list(languages.keys())[selected_language - 1]
            language_code = languages[language_name]
            LANGUAGE_INPUT = language_code
            print(f"Selected language: {language_name}")
        
        final_text = ""
        print("""
            Welcome to DSM Handler : 
            Enter 1 to Record from your Microphone 
            Enter 2 to Record from Standard Audio Output 
            Enter 3 to Anaylze Weekly Data 
            Enter 4 to Exit
        """)


        choice = input("Your Choice: ")

        if choice == '1' : 
            print("Taking Audio from Microphone as an Input")
            speechToText(MICROPHONE)
 
        elif choice == '2' : 
            print("Taking Audio from Input Stream")
            speechToText(AUDIOSTREAM)
            
        elif choice == '3':
            print("Analyzing Weekly Data and Making Performance Evaluations")
            analyze_weekly_data()

        elif choice == '4':
            print("Exiting the program...")
            break

        else : 
            print("Invalid Choice. Please try again.")
            continue

        if choice in ['1', '2']:
            final_text = audioToText(LANGUAGE_INPUT)

        if final_text == "" or final_text is None:
            print("No Text to process")
        else: 
            print("Final Transcribed Text:", final_text)
            final_result = askGPT(f"This is the transcription of a daily meet of a team, you need to Extract summary, insights, and action items from the transcription in the same format and don't add redundent content: {final_text}")
            print(final_result)
            with open("output.json", "w") as f:
                f.write(final_result)
            send_calendar_notification(final_result)


if __name__ == "__main__":
    main()
