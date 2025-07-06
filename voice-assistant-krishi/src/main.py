"""
Voice Assistant Krishi
---------------------
A virtual voice assistant for Windows that supports:
- Wake word detection ("Hey Krishi")
- Speech recognition and text input
- Task execution: play music, open apps, search the web, tell time/date, control system volume, and more
- Grok-like Q&A: Ask general questions and get answers using OpenAI's GPT
- Text-to-speech responses
- Extensible and easy to customize

To use: Just speak or type your command. The assistant will respond and perform the requested action.
"""

import pyttsx3
import speech_recognition as sr
import threading
import time
import os
import webbrowser
import subprocess
import psutil
import pyautogui
from datetime import datetime
import requests
import openai
from dotenv import load_dotenv

class VoiceAssistantKrishi:
    def __init__(self):
        """Initialize the Voice Assistant"""
        self.tts_engine = pyttsx3.init()
        self.wake_word = "hey krishi"
        self.is_active = False
        
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Configure microphone
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
        
        # Configure Text-to-Speech
        self.configure_tts()
        
        # Supported commands
        self.commands = {
            "music": ["play music", "play song", "open music", "spotify"],
            "call": ["call", "phone", "dial"],
            "apps": ["open", "launch", "start"],
            "time": ["time", "what time"],
            "date": ["date", "what date", "today"],
            "weather": ["weather", "temperature"],
            "search": ["search", "google", "find"],
            "system": ["shutdown", "restart", "volume"],
            "help": ["help", "commands", "what can you do"],
            "exit": ["goodbye", "exit", "quit", "stop", "bye"]
        }
        
        # Load environment variables
        load_dotenv()
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        if self.openai_api_key:
            openai.api_key = self.openai_api_key
        
    def configure_tts(self):
        """Configure Text-to-Speech settings"""
        try:
            # Set speech rate (words per minute)
            self.tts_engine.setProperty('rate', 150)
            
            # Set volume (0.0 to 1.0)
            self.tts_engine.setProperty('volume', 0.9)
            
            # Try to set voice (female voice if available)
            voices = self.tts_engine.getProperty('voices')
            if voices:
                # Use second voice if available (usually female)
                if len(voices) > 1:
                    self.tts_engine.setProperty('voice', voices[1].id)
                else:
                    self.tts_engine.setProperty('voice', voices[0].id)
                    
        except Exception as e:
            print(f"TTS configuration warning: {e}")
        
    def speak(self, text):
        """Convert text to speech"""
        print(f"🤖 Krishi: {text}")
        try:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            print(f"Speech error: {e}")
        
    def get_user_input(self):
        """Get text input from user"""
        return input("👤 You (Type): ").lower().strip()
    
    def listen_for_speech(self):
        """Listen for speech input from user"""
        try:
            print("🎤 Listening... (Speak now)")
            with self.microphone as source:
                # Listen for audio with timeout
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
            
            print("🔄 Processing your speech...")
            # Use Google's speech recognition
            text = self.recognizer.recognize_google(audio).lower()
            print(f"👤 You said: {text}")
            return text
            
        except sr.WaitTimeoutError:
            print("⏰ No speech detected, timeout reached")
            return ""
        except sr.UnknownValueError:
            print("❓ Sorry, I couldn't understand what you said")
            return ""
        except sr.RequestError as e:
            print(f"🌐 Speech recognition service error: {e}")
            return ""
        except Exception as e:
            print(f"🔴 Speech recognition error: {e}")
            return ""
    
    def play_music(self):
        """Open music applications"""
        try:
            # Try to open Spotify
            self.speak("Opening Spotify for you")
            webbrowser.open("https://open.spotify.com")
        except Exception as e:
            self.speak("I couldn't open music. Let me try YouTube Music")
            webbrowser.open("https://music.youtube.com")
    
    def make_call(self, command):
        """Handle call requests"""
        self.speak("I can't make actual calls yet, but I can help you open calling apps")
        try:
            # Try to open default calling app
            if "whatsapp" in command:
                webbrowser.open("https://web.whatsapp.com")
                self.speak("Opening WhatsApp Web")
            elif "skype" in command:
                webbrowser.open("https://web.skype.com")
                self.speak("Opening Skype")
            else:
                self.speak("You can try saying 'open WhatsApp' or 'open Skype'")
        except Exception as e:
            self.speak("I couldn't open the calling app")
    
    def open_application(self, command):
        """Open various applications"""
        try:
            if "browser" in command or "chrome" in command:
                self.speak("Opening Chrome browser")
                webbrowser.open("https://www.google.com")
                
            elif "notepad" in command:
                self.speak("Opening Notepad")
                subprocess.Popen(["notepad"])
                
            elif "calculator" in command:
                self.speak("Opening Calculator")
                subprocess.Popen(["calc"])
                
            elif "file manager" in command or "explorer" in command:
                self.speak("Opening File Explorer")
                subprocess.Popen(["explorer"])
                
            elif "paint" in command:
                self.speak("Opening Paint")
                subprocess.Popen(["mspaint"])
                
            elif "word" in command:
                self.speak("Opening Microsoft Word")
                subprocess.Popen(["winword"])
                
            elif "excel" in command:
                self.speak("Opening Microsoft Excel")
                subprocess.Popen(["excel"])
                
            elif "powerpoint" in command:
                self.speak("Opening PowerPoint")
                subprocess.Popen(["powerpnt"])
                
            elif "youtube" in command:
                self.speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")
                
            elif "facebook" in command:
                self.speak("Opening Facebook")
                webbrowser.open("https://www.facebook.com")
                
            elif "instagram" in command:
                self.speak("Opening Instagram")
                webbrowser.open("https://www.instagram.com")
                
            elif "gmail" in command or "email" in command:
                self.speak("Opening Gmail")
                webbrowser.open("https://mail.google.com")
                
            else:
                self.speak("I'm not sure which app you want to open. Try being more specific.")
                
        except Exception as e:
            self.speak(f"I couldn't open that application. Error: {str(e)}")
    
    def get_time(self):
        """Get current time"""
        current_time = datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {current_time}")
    
    def get_date(self):
        """Get current date"""
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        self.speak(f"Today is {current_date}")
    
    def get_weather(self):
        """Get weather information"""
        self.speak("I don't have weather integration yet, but let me open a weather website for you")
        webbrowser.open("https://weather.com")
    
    def search_web(self, command):
        """Search the web"""
        search_term = command.replace("search", "").replace("google", "").replace("find", "").strip()
        
        if search_term:
            self.speak(f"Searching for {search_term}")
            search_url = f"https://www.google.com/search?q={search_term.replace(' ', '+')}"
            webbrowser.open(search_url)
        else:
            search_term = input("What would you like me to search for? ")
            if search_term:
                self.speak(f"Searching for {search_term}")
                search_url = f"https://www.google.com/search?q={search_term.replace(' ', '+')}"
                webbrowser.open(search_url)
    
    def system_control(self, command):
        """Handle system control commands"""
        if "volume up" in command:
            self.speak("Increasing volume")
            for i in range(5):
                pyautogui.press('volumeup')
                
        elif "volume down" in command:
            self.speak("Decreasing volume")
            for i in range(5):
                pyautogui.press('volumedown')
                
        elif "mute" in command:
            self.speak("Muting volume")
            pyautogui.press('volumemute')
            
        elif "shutdown" in command:
            self.speak("I can't shutdown the system for security reasons")
            
        elif "restart" in command:
            self.speak("I can't restart the system for security reasons")
            
        else:
            self.speak("I'm not sure what system command you want me to execute")
    
    def show_help(self):
        """Show available commands"""
        help_text = """
        
        💡 Tips:
        - Speak clearly and at normal pace
        - Wait for the listening prompt before speaking
        - Use the wake word "Hey Krishi" for attention
        """
        
        self.speak("Here are my available commands and features")
        print(help_text)
    
    def classify_command(self, command):
        """Classify user command into categories"""
        for category, keywords in self.commands.items():
            for keyword in keywords:
                if keyword in command:
                    return category
        return "unknown"
    
    def is_question(self, command):
        question_starts = [
            'what is', 'who is', 'explain', 'define', 'how do', 'how to', 'why', 'when', 'where', 'tell me about', 'give me details about', 'describe'
        ]
        return any(command.strip().lower().startswith(q) for q in question_starts)

    def ask_grok(self, question):
        if not self.openai_api_key:
            self.speak("Sorry, the AI Q&A feature is not configured. Please set your API key in the .env file.")
            return
        self.speak("Let me find the answer for you.")
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}],
                max_tokens=256,
                temperature=0.7
            )
            answer = response.choices[0].message['content'].strip()
            print(f"🤖 Grok: {answer}")
            self.speak(answer)
        except Exception as e:
            self.speak(f"Sorry, I couldn't get an answer. {e}")

    def process_command(self, command):
        """Process user commands"""
        if not command:
            return True
            
        command_type = self.classify_command(command)
        
        try:
            if self.is_question(command):
                self.ask_grok(command)
            elif command_type == "music":
                self.play_music()
                
            elif command_type == "call":
                self.make_call(command)
                
            elif command_type == "apps":
                self.open_application(command)
                
            elif command_type == "time":
                self.get_time()
                
            elif command_type == "date":
                self.get_date()
                
            elif command_type == "weather":
                self.get_weather()
                
            elif command_type == "search":
                self.search_web(command)
                
            elif command_type == "system":
                self.system_control(command)
                
            elif command_type == "help":
                self.show_help()
                
            elif command_type == "exit":
                self.speak("Goodbye! Have a wonderful day!")
                return False
                
            else:
                self.speak("I'm not sure how to help with that. Try saying 'help' to see what I can do.")
                
        except Exception as e:
            self.speak(f"Sorry, I encountered an error: {str(e)}")
            
        return True
    
    def start_assistant(self):
        """Main assistant loop"""
        print("🚀 Starting Voice Assistant Krishi...")
        print("="*60)
        
        self.speak("Hello! I'm Krishi, your personal voice assistant. Speak to me, or type if you prefer.")
        self.speak("Say 'Hey Krishi' to wake me up.")
        
        while True:
            try:
                print("\n" + "="*60)
                print("💬 Listening for your voice... (or type and press Enter)")
                
                # Start a thread to listen for speech
                speech_result = {'text': ''}
                def listen_thread():
                    speech_result['text'] = self.listen_for_speech()
                t = threading.Thread(target=listen_thread)
                t.start()
                
                # Wait for either speech or text input
                user_input = ''
                while t.is_alive():
                    if os.name == 'nt':
                        import msvcrt
                        if msvcrt.kbhit():
                            user_input = input("👤 You (Type): ").lower().strip()
                            break
                    else:
                        import sys, select
                        print("(Press Enter to type instead of speaking)")
                        i, o, e = select.select([sys.stdin], [], [], 0.1)
                        if i:
                            user_input = sys.stdin.readline().strip().lower()
                            break
                    time.sleep(0.1)
                t.join(timeout=0.1)
                if not user_input:
                    user_input = speech_result['text']
                
                # Process wake word
                if user_input and self.wake_word in user_input:
                    self.speak("Yes, I'm listening. How can I help you?")
                    user_input = user_input.replace(self.wake_word, "").strip()
                    if not user_input:
                        self.speak("Please say your command.")
                        user_input = self.listen_for_speech()
                
                # Process command
                if user_input:
                    if not self.process_command(user_input):
                        break
                
            except KeyboardInterrupt:
                print("\n\n🛑 Assistant stopped by user")
                self.speak("Goodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
                self.speak("Sorry, I encountered an error. Please try again.")

def main():
    """Main function to start the assistant"""
    try:
        assistant = VoiceAssistantKrishi()
        assistant.start_assistant()
    except Exception as e:
        print(f"Failed to start assistant: {e}")

if __name__ == "__main__":
    main()