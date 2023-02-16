from functions import get_todos, write_todos
import PySimpleGUI as sg  # Part 1 - The import


# Define the window's contents
layout = [[sg.Text("Type a to-do")],  # Part 2 - The Layout
          [sg.InputText(key="todo"), sg.Button("Add")],
          ]

# Create the window
window = sg.Window('My To-Do App', layout, font=('Helvetica', 20))

while True:
    event, values = window.read()
    print('added', values,"! Thanks for visiting my To-Do app")
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            write_todos(todos)
        case sg.WIN_CLOSED:
            break




# Finish up by removing from the screen
window.close()  # Part 5 - Close the Window