// Terminal.Gui Quick Start Template
// Framework: Terminal.Gui (C# / .NET)
// Reference: https://github.com/tui-cs/Terminal.Gui

using Terminal.Gui;

class Program
{
    static void Main()
    {
        Application.Init();

        // Create a window
        var window = new Window("TRIII-UI Terminal App")
        {
            X = 0,
            Y = 1,
            Width = Dim.Fill(),
            Height = Dim.Fill()
        };

        // Add a label
        var label = new Label("Welcome to Terminal.Gui!")
        {
            X = 1,
            Y = 1
        };

        // Add a button
        var button = new Button("Click Me")
        {
            X = 1,
            Y = 3
        };
        button.Clicked += () =>
        {
            MessageBox.Query("Message", "Button clicked!", "OK");
        };

        // Add a text field
        var textField = new TextField("Enter text here")
        {
            X = 1,
            Y = 5,
            Width = 30
        };

        // Add controls to window
        window.Add(label, button, textField);

        // Add a menu bar
        var menu = new MenuBar(new MenuBarItem[] {
            new MenuBarItem("_File", new MenuItem[] {
                new MenuItem("_Quit", "", () => Application.RequestStop())
            })
        });

        Application.Top.Add(menu, window);
        Application.Run();
    }
}

/*
 * Installation:
 * dotnet add package Terminal.Gui
 *
 * Key Features:
 * - Windows, Labels, Buttons, TextFields
 * - Menu bars and dialog boxes
 * - Rich terminal UI elements
 * - Cross-platform support
 */
