# GUI Framework Selection Skill

## Overview
This skill helps developers select the right GUI framework for their project based on requirements, programming language, and use case.

## Key Frameworks

### Terminal.Gui
- **Language:** C# / .NET
- **Best for:** Terminal-first applications, command-line interfaces with rich UI
- **Characteristics:** Modern terminal-based UIs, cross-platform
- **GitHub:** https://github.com/tui-cs/Terminal.Gui

### CustomTkinter
- **Language:** Python
- **Best for:** Python desktop apps needing modern, polished appearance
- **Characteristics:** Themeable, desktop-style look, extension of Tkinter
- **GitHub:** https://github.com/TomSchimansky/CustomTkinter

### PySimpleGUI
- **Language:** Python
- **Best for:** Simple to medium complexity desktop apps, rapid prototyping
- **Characteristics:** Beginner-friendly, fast development cycle, minimal boilerplate
- **GitHub:** https://github.com/PySimpleGUI/PySimpleGUI

## Selection Guide

### Choose Terminal.Gui if:
- You're building a .NET application
- Your primary interface is terminal-based
- You want rich UI elements within a terminal environment
- Cross-platform terminal compatibility is important

### Choose CustomTkinter if:
- You're using Python
- You need a modern, desktop-quality appearance
- You want theme customization
- You want something more polished than vanilla Tkinter

### Choose PySimpleGUI if:
- You're using Python and want the fastest development
- Your application has simple to moderate UI complexity
- You want minimal setup and learning curve
- Rapid prototyping is your priority

## Decision Matrix

| Factor | Terminal.Gui | CustomTkinter | PySimpleGUI |
|--------|-------------|---------------|------------|
| Language | C# / .NET | Python | Python |
| Complexity | Medium-High | Medium | Low-Medium |
| Learning Curve | Medium | Medium | Low |
| Development Speed | Medium | Medium | Fast |
| Modern Look | Terminal Style | Yes | Standard |
| Customization | Good | Excellent | Good |

## Usage Examples

See the `/tools/` directory for implementation examples and quick-start templates for each framework.

## References

- Terminal.Gui: https://github.com/tui-cs/Terminal.Gui
- CustomTkinter: https://github.com/TomSchimansky/CustomTkinter
- PySimpleGUI: https://github.com/PySimpleGUI/PySimpleGUI
