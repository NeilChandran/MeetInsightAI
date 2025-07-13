"""
transcriber.py

Transcribes audio files to text using the SpeechRecognition library and Google Web Speech API.
"""

import speech_recognition as sr
import os
import sys

def transcribe_audio(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        print(f"Transcribing {filename}...")
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        print("Transcription successful.")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"API error: {e}")
        return ""

def save_transcript(text, transcript_file):
    with open(transcript_file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Transcript saved to {transcript_file}")

def batch_transcribe(directory):
    for file in os.listdir(directory):
        if file.endswith(".wav"):
            transcript_file = os.path.join(directory, file.replace('.wav', '.txt'))
            if os.path.exists(transcript_file):
                print(f"Transcript already exists for {file}, skipping.")
                continue
            transcript = transcribe_audio(os.path.join(directory, file))
            if transcript:
                save_transcript(transcript, transcript_file)

def main():
    print("Welcome to MeetInsightAI Transcriber")
    mode = input("Transcribe single file or batch? (single/batch): ").strip().lower()
    if mode == "batch":
        directory = input("Enter directory path: ").strip()
        if not os.path.isdir(directory):
            print("Invalid directory.")
            return
        batch_transcribe(directory)
    else:
        audio_file = input("Enter audio filename to transcribe: ").strip()
        if not os.path.exists(audio_file):
            print("File not found.")
            return
        transcript = transcribe_audio(audio_file)
        if transcript:
            transcript_file = audio_file.replace('.wav', '.txt')
            save_transcript(transcript, transcript_file)
        else:
            print("No transcript generated.")

if __name__ == "__main__":
    main()

