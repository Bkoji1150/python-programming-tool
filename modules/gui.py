from functions import get_todos, write_todos
import PySimpleGUI as sg  # Part 1 - The import


# Define the window's contents
layout = [[sg.Text("Type a to-do")],  # Part 2 - The Layout
          [sg.Input(), sg.Button("Add")],
          [sg.Button('Ok')]]

# Create the window
window = sg.Window('My To-Do App', layout)  # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()  # Part 4 - Event loop or Window.read call

# Do something with the information gathered
print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()  # Part 5 - Close the Window