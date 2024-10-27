import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
from groq import Groq

API_KEY = "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"



# Initialize Groq API client
client = Groq(
    api_key=API_KEY,
)

# Function to get chat completion from Groq API
def get_ai_response(user_input):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_input}
            ],
            model="llama3-8b-8192",
            max_tokens=2048,
            top_p=1,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# Main loop for user input
# Function to handle sending messages
def send_message():
    user_input = user_entry.get()
    if user_input.strip() == "":
        return
    chat_history.insert(tk.END, user_input + "\n\n")
    user_entry.delete(0, tk.END)

    response = get_ai_response(user_input)
    chat_history.insert(tk.END, "AI: " + response + "\n")
    chat_history.yview(tk.END)  # Auto-scroll to the bottom


# Initialize tkinter window
root = tk.Tk()
root.title("Chat AI with Groq API")

# Set reasonable window size
window_width = 800
window_height = 600

root.geometry(f"{window_width}x{window_height}")

# Load and set background image
bg_image = Image.open("pic5.png")
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_photo)
background_label.image = bg_photo  # Keep a reference to the image
background_label.place(relwidth=1, relheight=1)

# Frame for chat history
chat_frame = tk.Frame(root, bg="#F7F7F7", bd=5)
chat_frame.place(relwidth=0.7, relheight=0.6, relx=0.15, rely=0.1)

# ScrolledText widget for chat history
chat_history = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, state='normal')
chat_history.pack(fill=tk.BOTH, expand=True)
chat_history.configure(state='normal')

# Entry widget for user input
user_entry = tk.Entry(root, font=("Arial", 14))
user_entry.place(relwidth=0.7, relheight=0.07, relx=0.15, rely=0.75)

# Send button
send_button = tk.Button(root, text="Send", font=("Arial", 14), command=send_message)
send_button.place(relwidth=0.2, relheight=0.07, relx=0.65, rely=0.85)

root.mainloop()