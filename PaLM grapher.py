import tkinter as tk
from tkinter import filedialog
import google.generativeai as genai

# AI setup
genai.configure(api_key="Your_API_Key")
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]
model = genai.GenerativeModel(
    model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings
)

# UI setup
window = tk.Tk()
window.geometry("720x480")
window.resizable(True, True)
window.title("Mind Mapper")
window.config(bg="#454545")

# vars
window_bg = tk.PhotoImage(file="Background.png")

# commands
def send_gen():
    prompt_message = prompt.get()
    response = model.generate_content([prompt_message])
    text_widget.insert(tk.END, response.text + "\n")
    # Optionally, you can clear the entry field after sending the message
    prompt.delete(0, tk.END)

# (Window design)#

# title
title_logo = tk.PhotoImage(file="titlelogo.png")
title_label = tk.Label(window, image=title_logo, font=(14), height=20, width=115)
title_label.place(x=620, y=0)

# text prompt
prompt = tk.Entry(window, width=143, font=(14))
prompt.place(x=5, y=710)

# send button
send_logo = tk.PhotoImage(file="sendbutton.png")
send_button = tk.Button(window, image=send_logo, width=35, height=15, command=send_gen)
send_button.place(x=1300, y=710)

# screen with scroll bar
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_widget = tk.Text(window, wrap=tk.WORD, width=120, height=30, fg="white", font=("Helvetica", 14), yscrollcommand=scrollbar.set)
text_widget.configure(bg="#363636")
text_widget.place(x=25, y=25)

scrollbar.config(command=text_widget.yview)

# Start the Tkinter event loop
window.mainloop()
