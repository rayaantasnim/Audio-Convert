import asyncio
import os
import sys
import time
from pathlib import Path
import edge_tts
import pyttsx3

# Supported high-quality online voices
ONLINE_VOICES = {
    "1": {"name": "Microsoft Christopher (Male)", "id": "en-US-ChristopherNeural", "gender": "male"},
    "2": {"name": "Microsoft Ava (Female)", "id": "en-US-AvaNeural", "gender": "female"},
    "3": {"name": "Microsoft Brian (Male - UK)", "id": "en-GB-BrianNeural", "gender": "male"}
}

def dynamic_print(text: str, delay: float = 0.02):
    """Prints text with a smooth, stylized typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_unique_filename(base_name: str = "speech", extension: str = "mp3") -> str:
    """Generates a non-conflicting sequential filename to prevent overwrites."""
    counter = 1
    while True:
        filename = f"{base_name}_{counter:03d}.{extension}"
        if not Path(filename).exists():
            return filename
        counter += 1

def fallback_offline_tts(text: str, output_file: str, target_gender: str):
    """Advanced localized backup that matches voice gender seamlessly."""
    dynamic_print("\n[!] Internet connection/API failure detected.")
    dynamic_print("-> Switching instantly to 100% offline local backup engine...")
    
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        selected_voice = voices[0]  # Default fallback
        
        # Smart matching: Try to find a local voice matching the requested gender
        for voice in voices:
            if target_gender in voice.name.lower() or (hasattr(voice, 'gender') and voice.gender == target_gender):
                selected_voice = voice
                break
                
        engine.setProperty('voice', selected_voice.id)
        engine.setProperty('rate', 165)  # Optimally balanced natural human speed
        
        # Save audio locally
        engine.save_to_file(text, output_file)
        engine.runAndWait()
        dynamic_print(f"✨ Successfully saved local backup audio to: '{output_file}'")
    except Exception as e:
        print(f"Critical Error: Local text-to-speech architecture failed. Details: {e}")

async def generate_speech():
    print("=" * 60)
    print("         PREMIUM HYBRID TEXT-TO-SPEECH GENERATOR        ")
    print("=" * 60)
    
    # 1. Capture and validate text input
    text_input = input("📝 Enter the text you want to convert into speech:\n> ").strip()
    if not text_input:
        print("❌ Error: Input text cannot be completely empty.")
        return

    # 2. Present voice configuration menu
    print("\nAvailable Premium Online Voices:")
    for key, voice_info in ONLINE_VOICES.items():
        print(f" [{key}] {voice_info['name']}")
    
    choice = input("\nSelect a voice number (Default is 1): ").strip()
    selected_voice = ONLINE_VOICES.get(choice, ONLINE_VOICES["1"])
    
    # 3. Calculate smart output file route
    output_filename = get_unique_filename()
    
    # 4. Attempt Primary Premium Generation (Online)
    try:
        dynamic_print(f"\n📡 Connecting to cloud matrix for '{selected_voice['name']}'...")
        communicate = edge_tts.Communicate(text_input, selected_voice["id"])
        await communicate.save(output_filename)
        dynamic_print(f"✨ Success! High-fidelity studio voice saved to: '{output_filename}'")
        
    except Exception as e:
        # 5. Trigger automated offline emergency system on network fail
        fallback_offline_tts(text_input, output_filename, selected_voice["gender"])

if __name__ == "__main__":
    try:
        asyncio.run(generate_speech())
    except KeyboardInterrupt:
        print("\n\nProcess terminated cleanly by user.")
