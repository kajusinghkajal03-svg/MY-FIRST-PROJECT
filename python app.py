import tkinter as tk
from tkinter import messagebox
import random
import webbrowser

# Music data
music_data = {
    "Happy": [
        ("Happy - Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
        ("Kala Chashma", "https://www.youtube.com/watch?v=k4yXQkG2s1E")
    ],
    "Sad": [
        ("Let Her Go - Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA"),
        ("Channa Mereya", "https://www.youtube.com/watch?v=284Ov7ysmfA")
    ],
    "Energetic": [
        ("Believer - Imagine Dragons", "https://www.youtube.com/watch?v=7wtfhZwyrcc"),
        ("Malhari", "https://www.youtube.com/watch?v=l_MyUGq7pgs")
    ],
    "Calm": [
        ("Weightless", "https://www.youtube.com/watch?v=UfcAVejslrU"),
        ("Raabta (Instrumental)", "https://www.youtube.com/watch?v=6FURuLYrR_Q")
    ]
}

# Function
def recommend_song():
    mood = mood_var.get()
    
    if mood not in music_data:
        messagebox.showerror("Error", "Please select a mood")
        return
    
    song = random.choice(music_data[mood])
    result_label.config(text=f"🎵 {song[0]}")
    
    global current_link
    current_link = song[1]

def open_song():
    try:
        webbrowser.open(current_link)
    except:
        messagebox.showwarning("Warning", "No song selected")

# GUI window
root = tk.Tk()
root.title("🎧 Mood Music Recommender")
root.geometry("400x300")

# Dropdown
mood_var = tk.StringVar()
mood_var.set("Select Mood")

dropdown = tk.OptionMenu(root, mood_var, *music_data.keys())
dropdown.pack(pady=20)

# Button
btn = tk.Button(root, text="Recommend Song", command=recommend_song)
btn.pack(pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Open button
open_btn = tk.Button(root, text="Open Song ▶", command=open_song)
open_btn.pack(pady=10)

# Run app
root.mainloop()