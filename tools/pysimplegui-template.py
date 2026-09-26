#!/usr/bin/env python3
"""
PySimpleGUI Quick Start Template
Framework: PySimpleGUI (Python)
Reference: https://github.com/PySimpleGUI/PySimpleGUI
"""

import PySimpleGUI as sg

# Set theme
sg.theme("DarkBlue2")

# Define the layout
layout = [
    [sg.Text("TRIII-UI PySimpleGUI Application", font=("Arial", 18, "bold"))],
    [sg.Text("A simple and fast desktop GUI framework", font=("Arial", 10))],
    [sg.Text("")],  # Spacer
    [sg.Text("Enter your name:"), sg.InputText(key="-NAME-", size=(20, 1))],
    [sg.Text("Enter your message:"), sg.Multiline(size=(30, 5), key="-MESSAGE-")],
    [sg.Checkbox("Accept terms", key="-ACCEPT-")],
    [sg.Text("")],  # Spacer
    [
        sg.Button("Submit"),
        sg.Button("Clear"),
        sg.Button("Exit")
    ],
    [sg.Text("", key="-OUTPUT-", text_color="lightblue")]
]

# Create the window
window = sg.Window("TRIII-UI Example", layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    elif event == "Submit":
        name = values["-NAME-"]
        message = values["-MESSAGE-"]
        accepted = values["-ACCEPT-"]

        if name and message and accepted:
            output = f"Hello {name}! Your message: {message}"
            window["-OUTPUT-"].update(output)
        else:
            sg.popup_error("Please fill in all fields and accept terms")

    elif event == "Clear":
        window["-NAME-"].update("")
        window["-MESSAGE-"].update("")
        window["-ACCEPT-"].update(False)
        window["-OUTPUT-"].update("")

window.close()

"""
Installation:
pip install PySimpleGUI

Key Features:
- Minimal boilerplate code
- Easy to learn and use
- Fast development cycle
- Simple event handling
- Good for rapid prototyping
"""
