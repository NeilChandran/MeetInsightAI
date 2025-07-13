"""
meeting_recorder.py

Records audio from your microphone and saves it as a WAV file.
"""

import sounddevice as sd
import numpy as np
import wave
import datetime
import os

SAMPLE_RATE = 44100  # Hertz
CHANNELS = 2
SAMPLE_WIDTH = 2  # bytes (16-bit)
DEFAULT_DURATION = 60  # seconds

def list_devices():
    print("Available audio input devices:")
    devices = sd.query_devices()
    for i, dev in enumerate(devices):
        if dev['max_input_channels'] > 0:
            print(f"{i}: {dev['name']}")

def record_audio(filename, duration, device=None):
    print(f"Recording for {duration} seconds...")
    try:
        if device is not None:
            sd.default.device = device
        audio = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=CHANNELS, dtype='int16')
        sd.wait()
        print("Recording finished. Saving file...")
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(SAMPLE_WIDTH)
            wf.setframerate(SAMPLE_RATE)
            wf.writeframes(audio.tobytes())
        print(f"Audio saved as {filename}")
    except Exception as e:
        print(f"Error during recording: {e}")

def get_filename():
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"meeting_{now}.wav"
    return filename

def main():
    print("Welcome to MeetInsightAI Meeting Recorder")
    list_devices()
    use_device = input("Enter device index for input (or press Enter for default): ").strip()
    device = int(use_device) if use_device else None
    duration_input = input(f"Enter recording duration in seconds (default {DEFAULT_DURATION}): ").strip()
    duration = int(duration_input) if duration_input.isdigit() else DEFAULT_DURATION
    filename = get_filename()
    record_audio(filename, duration, device)
    print("Done.")

if __name__ == "__main__":
    main()
