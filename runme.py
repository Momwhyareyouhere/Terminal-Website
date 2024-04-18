import tkinter as tk
import time

def type_message_slowly(label, message, delay):
    for char in message:
        label.config(text=label.cget("text") + char)
        label.update()
        time.sleep(delay)

def close_window():
    root.destroy()

root = tk.Tk()
root.title("Welcome to Terminal")

message_label = tk.Label(root, text="")
message_label.pack()

message = "Hello User, Welcome to Terminal. You can use this Linux console with Python for free, and by the way, you can do much more things."
type_delay = 0.05

type_message_slowly(message_label, message, type_delay)

# Schedule window closure after message display
root.after(10000, close_window)  # 10 seconds delay

root.mainloop()

