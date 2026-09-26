# TRIII-UI Tools Directory

This directory contains quick-start templates and implementation examples for each GUI framework listed in the TRIII-UI resource collection.

## Available Templates

### Terminal.Gui (C#)
**File:** `terminal-gui-template.cs`

A basic C# / .NET example demonstrating:
- Window creation
- Labels, buttons, and text fields
- Basic event handling
- Menu bars

**Quick Start:**
```bash
dotnet new console
dotnet add package Terminal.Gui
# Copy terminal-gui-template.cs content into Program.cs
dotnet run
```

---

### CustomTkinter (Python)
**File:** `customtkinter-template.py`

A Python example showing:
- Modern, themeable UI
- Dark/light mode toggle
- Text entry and button handling
- Frame-based layout
- Class-based application structure

**Quick Start:**
```bash
pip install customtkinter
python customtkinter-template.py
```

---

### PySimpleGUI (Python)
**File:** `pysimplegui-template.py`

A Python example demonstrating:
- Simple, minimal code
- Input fields and multiline text
- Checkboxes and buttons
- Event loop handling
- Error validation

**Quick Start:**
```bash
pip install PySimpleGUI
python pysimplegui-template.py
```

---

## Choosing a Template

| Need | Framework | Template |
|------|-----------|----------|
| .NET terminal app | Terminal.Gui | terminal-gui-template.cs |
| Modern Python desktop | CustomTkinter | customtkinter-template.py |
| Quick Python prototype | PySimpleGUI | pysimplegui-template.py |

## How to Use These Templates

1. **Copy the relevant template** for your framework
2. **Install the required package** using the command shown above
3. **Modify the code** to suit your application
4. **Run and extend** with additional features

## Learn More

- See `/skills/GUI_Framework_Selection.md` for a detailed comparison
- Visit the official repositories linked in the README
- Refer to the inline comments in each template for feature explanations
