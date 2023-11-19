import tkinter as tk
from tkinter import messagebox

# Mad Libs story template with placeholders
mad_libs_story = """
A vacation is when you take a trip to some {} place with your {} family. Usually you go to some place that is near a/an {} or up on a/an 
{}. A good vacation place is one where you can ride {} or play {} or go hunting for {} . I like to spend my time {} or {}. When parents 
go on a vacation, they spend their time eating three {} a day, and fathers play golf, and mothers sit around {}. Last summer, my little 
brother fell in a/an {} and got poison {} all over his {}. My family is going to go to (the) {}, and I will practice {}. Parents need 
vacations more than kids because parents are always very {} and because they have to work {} hours every day all year making enough {} to 
pay for the vacation.
"""


def generate_mad_lib():
    # Get user input
    user_inputs = [entry_var.get() for entry_var in entry_fields]

    # Replace placeholders with user input
    result = mad_libs_story.format(*user_inputs)

    # Display the result
    label_result.config(text=result)


def clear_boxes():
    # Clear the input boxes
    for entry_var in entry_fields:
        entry_var.set('')
    label_result.config(text="Result:")


def show_instructions():
    instructions = """
    Fill in the blanks with words of the specified type.
    Click the 'Generate Mad Lib' button to see the result.
    Have fun!
    """
    messagebox.showinfo("Instructions", instructions)


# Create the main window
window = tk.Tk()
window.title("Mad Libs Game")

# Create a list of StringVar for input fields
entry_fields = []


# Labels and Entry fields
fields = [
    "Adjective 1", "Adjective 2", "Noun 1", "Noun 2", "Plural Noun 1", "Game 1", "Plural Noun 2",
    "Verb ending in -ing 1", "Verb ending in -ing 2", "Plural Noun 3", "Verb ending in -ing 3", 
    "Noun 3", "Plant 1", "Part of the Body 1", "A Place 1", "Verb ending in -ing 4", 
    "Adjective 3", "Number 1", "Plural Noun 4"
]

for idx, label_text in enumerate(fields):
    label = tk.Label(window, text=f"{label_text}:")
    label.grid(row=idx, column=0, padx=5, pady=2)
    
    entry_var = tk.StringVar()
    entry = tk.Entry(window, textvariable=entry_var)
    entry.grid(row=idx, column=1, padx=5, pady=2)
    entry_fields.append(entry_var)


# Result Label
label_result = tk.Label(window, text="Result:")
label_result.grid(row=len(fields), column=0, columnspan=2, padx=5, pady=5)

# Buttons
button_generate = tk.Button(window, text="Generate Mad Lib", command=generate_mad_lib)
button_clear = tk.Button(window, text="Clear", command=clear_boxes)
button_instructions = tk.Button(window, text="Instructions", command=show_instructions)

button_generate.grid(row=len(fields) + 1, column=0, columnspan=2, padx=5, pady=5)
button_clear.grid(row=len(fields) + 2, column=0, columnspan=2, padx=5, pady=5)
button_instructions.grid(row=len(fields) + 3, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI event loop
window.mainloop()