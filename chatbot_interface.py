import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext
from tkinter import PhotoImage
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import speech_recognition as sr
from gtts import gTTS
import pygame
import tempfile
from PIL import Image, ImageTk, ImageOps

# Load the trained model
with open('chatbot_model_improved.pkl', 'rb') as file:
    model = pickle.load(file)

# Initialize the main window
root = tk.Tk()
root.title("Visar's Mental Health Chatbot")

# Set the colors
bg_color = "#f0f0f0"
text_color = "#333333"
entry_bg_color = "#ffffff"
button_bg_color = "#008CBA"

root.configure(bg=bg_color)

# Configure styles
style = ttk.Style()
style.configure("TEntry", relief="flat", padding=5)
style.configure("TButton", relief="flat", padding=5, background=button_bg_color, foreground=entry_bg_color, font=("Helvetica Neue", 12))

# Create chat window
chat_window = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD, width=60, height=20, bg=entry_bg_color, fg=text_color, font=("Helvetica Neue", 12), relief=tk.FLAT, bd=0, padx=10, pady=10)
chat_window.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Function to display the chat messages
def display_message(message, sender="You"):
    chat_window.configure(state=tk.NORMAL)
    chat_window.insert(tk.END, f"{sender}: {message}\n")
    chat_window.configure(state=tk.DISABLED)
    chat_window.see(tk.END)

# Function to get user input via text
def get_text_input():
    user_input = text_entry.get()
    display_message(user_input)
    text_entry.delete(0, tk.END)
    respond(user_input)

# Function to get user input via voice
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio_data = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio_data)
            text_entry.delete(0, tk.END)
            text_entry.insert(0, user_input)
        except sr.UnknownValueError:
            display_message("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            display_message(f"Could not request results from Google Speech Recognition service; {e}")

# Function to respond to user input
def respond(user_input):
    user_input = [user_input]
    response = model.predict(user_input)[0]
    display_message(response, sender="Bot")
    speak_text(response)

# Function to speak text
def speak_text(text):
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts.save(fp.name + ".mp3")
        pygame.mixer.init()
        pygame.mixer.music.load(fp.name + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

# Create text entry box
text_entry = ttk.Entry(root, width=40, style="TEntry")
text_entry.grid(row=1, column=0, padx=10, pady=10, ipadx=5, ipady=5)
text_entry.bind("<Return>", lambda event: get_text_input())  # Bind Enter key to send message
text_entry.focus()  # Set focus to the text entry widget

# Create Send button
send_button = ttk.Button(root, text="Send", command=get_text_input, style="TButton")
send_button.grid(row=1, column=1, padx=10, pady=10, ipadx=5, ipady=5)

# Load and invert the microphone icon image
mic_image = Image.open("microphone.png")
mic_image = mic_image.resize((24, 24), Image.LANCZOS)
microphone_icon = ImageTk.PhotoImage(mic_image)

# Create Voice Input button with microphone icon
voice_button = ttk.Button(root, image=microphone_icon, command=get_voice_input, style="TButton")
voice_button.grid(row=1, column=2, padx=10, pady=10, ipadx=5, ipady=5)

# Start the main loop
root.mainloop()
