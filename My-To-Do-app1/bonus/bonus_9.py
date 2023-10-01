import PySimpleGUI as sg  # Part 1 - The import

# Define the window's contents
layout = [
          [sg.Text("Select files to compress:")],  # Part 2 - The Layout
          [sg.Input(),sg.FilesBrowse("choose")],
          [sg.Text("Select destination folder")],
          [sg.Input(),sg.FolderBrowse("choose")],
          [sg.Button("compress")]
    ]

# Create the window
window = sg.Window('File compressor', layout)  # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()  # Part 4 - Event loop or Window.read call

# Do something with the information gathered
print('Hello', values[0], "! Thanks for visiting my To-Do app")

# Finish up by removing from the screen
window.close()  # Part 5 - Close the Window