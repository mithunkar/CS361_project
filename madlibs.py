import tkinter as tk
from tkinter import messagebox
import zmq

class MadLibsGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Mad Libs Game")

        self.entry_fields = []

        # Initialize ZMQ context and socket for communication with microservice
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:5555")

        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry fields
        fields = [
            "Adjective", "Adjective", "Noun", "Noun", "Plural Noun", "Game", "Plural Noun",
            "Verb ending in -ing", "Verb ending in -ing", "Plural Noun", "Verb ending in -ing",
            "Noun", "Plant", "Part of the Body", "A Place", "Verb ending in -ing",
            "Adjective", "Number", "Plural Noun"
        ]

        for idx, label_text in enumerate(fields):
            label = tk.Label(self.master, text=f"{label_text}:")
            label.grid(row=idx, column=0, padx=5, pady=2)

            entry_var = tk.StringVar()
            entry = tk.Entry(self.master, textvariable=entry_var)
            entry.grid(row=idx, column=1, padx=5, pady=2)
            self.entry_fields.append(entry_var)

            # Convert label text to lowercase for consistency
            word_type = label_text

            button = tk.Button(self.master, text=f"Get {word_type}", command=lambda w=entry_var, t=word_type: self.get_random_word(w, t))
            button.grid(row=idx, column=2, padx=5, pady=2)

        # Result Label
        self.result_label = tk.Label(self.master, text="Result:")
        self.result_label.grid(row=len(fields), column=0, columnspan=3, padx=5, pady=5)

        # Buttons
        button_generate = tk.Button(self.master, text="Generate Mad Lib", command=self.generate_mad_lib)
        button_clear = tk.Button(self.master, text="Clear", command=self.clear_boxes)
        button_instructions = tk.Button(self.master, text="Instructions", command=self.show_instructions)

        button_generate.grid(row=len(fields) + 1, column=0, columnspan=3, padx=5, pady=5)
        button_clear.grid(row=len(fields) + 2, column=0, columnspan=3, padx=5, pady=5)
        button_instructions.grid(row=len(fields) + 3, column=0, columnspan=3, padx=5, pady=5)

    def get_random_word(self, entry_var, word_type):
        # Request a random word from the microservice
        self.socket.send_string(word_type)
        random_word = self.socket.recv_string()

        # Set the received word in the corresponding entry field
        entry_var.set(random_word)

    def generate_mad_lib(self):
        # Get user input
        user_inputs = [entry_var.get() for entry_var in self.entry_fields]

        # Check if any entry is empty
        if any(not input_str.strip() for input_str in user_inputs):
            messagebox.showerror("Error", "Please fill in all the blanks.")
            return

        # Replace placeholders with user input
        result = mad_libs_story.format(*user_inputs)

        # Display the result
        self.result_label.config(text=result)

    def clear_boxes(self):
        # Clear the input boxes
        for entry_var in self.entry_fields:
            entry_var.set('')
        self.result_label.config(text="Result:")

    def show_instructions(self):
        instructions = """
        Fill in the blanks with words of the specified type.
        Click the 'Generate Mad Lib' button to see the result.
        Have fun!
        """
        messagebox.showinfo("Instructions", instructions)

    def __del__(self):
        # Close the ZMQ socket and context when the instance is deleted
        self.socket.close()
        self.context.term()


# Mad Libs story template with placeholders
mad_libs_story = """
A vacation is when you take a trip to some {} place with your {} family. Usually, you go to some place that is near a/an {} or up on a/an 
{}. A good vacation place is one where you can ride {} or play {} or go hunting for {} . I like to spend my time {} or {}. When parents 
go on vacation, they spend their time eating three {} a day, and fathers play golf, and mothers sit around {}. Last summer, my little 
brother fell in a/an {} and got poison {} all over his {}. My family is going to go to (the) {}, and I will practice {}. Parents need 
vacations more than kids because parents are always very {} and because they have to work {} hours every day all year making enough {} to 
pay for the vacation.
"""

if __name__ == "__main__":
    root = tk.Tk()
    app = MadLibsGenerator(root)
    root.mainloop()