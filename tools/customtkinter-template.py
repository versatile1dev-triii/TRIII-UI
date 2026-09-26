#!/usr/bin/env python3
"""
CustomTkinter Quick Start Template
Framework: CustomTkinter (Python)
Reference: https://github.com/TomSchimansky/CustomTkinter
"""

import customtkinter as ctk

class TriiiUIApp(ctk.CTk):
    """TRIII-UI Application using CustomTkinter"""

    def __init__(self):
        super().__init__()

        # Configure window
        self.title("TRIII-UI CustomTkinter App")
        self.geometry("500x400")

        # Set appearance mode
        ctk.set_appearance_mode("dark")  # "light", "dark", "system"
        ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

        # Create main frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Title label
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="Welcome to TRIII-UI",
            font=("Arial", 24, "bold")
        )
        self.title_label.pack(pady=10)

        # Description label
        self.desc_label = ctk.CTkLabel(
            self.main_frame,
            text="A modern Python GUI using CustomTkinter",
            font=("Arial", 12)
        )
        self.desc_label.pack(pady=5)

        # Text entry
        self.entry = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Enter text here"
        )
        self.entry.pack(pady=10, padx=10, fill="x")

        # Button
        self.button = ctk.CTkButton(
            self.main_frame,
            text="Click Me",
            command=self.button_clicked
        )
        self.button.pack(pady=10, padx=10, fill="x")

        # Output label
        self.output_label = ctk.CTkLabel(
            self.main_frame,
            text="Output will appear here",
            font=("Arial", 11),
            text_color="gray"
        )
        self.output_label.pack(pady=10)

        # Appearance mode toggle
        self.appearance_toggle = ctk.CTkSwitch(
            self.main_frame,
            text="Dark Mode",
            command=self.toggle_appearance
        )
        self.appearance_toggle.pack(pady=10)

    def button_clicked(self):
        """Handle button click event"""
        text = self.entry.get()
        self.output_label.configure(
            text=f"You entered: {text}" if text else "Please enter some text"
        )

    def toggle_appearance(self):
        """Toggle between light and dark mode"""
        mode = "light" if ctk.get_appearance_mode() == "dark" else "dark"
        ctk.set_appearance_mode(mode)


if __name__ == "__main__":
    """
    Installation:
    pip install customtkinter

    Key Features:
    - Modern, polished appearance
    - Themeable (light/dark modes)
    - Consistent styling across platforms
    - Built on top of Tkinter
    """
    app = TriiiUIApp()
    app.mainloop()
