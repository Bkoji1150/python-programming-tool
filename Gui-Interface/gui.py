from functions import get_todos, write_todos
import PySimpleGUI as sg  # Part 1 - The import


# Define the window's contents
layout = [[sg.Text("Type a to-do")],  # Part 2 - The Layout
          [sg.InputText(key="todo"), sg.Button("Add")],
          [sg.Listbox(values=get_todos(),
                      key='todos',
                      enable_events=True,
                      size=[45,10]),
          sg.Button("Edit"), sg.Button("Complete")
           ],
          [sg.Button('Exit')]
          ]

# Create the window
window = sg.Window('My To-Do App', layout, font=('Helvetica', 20),)

while True:
    event, values = window.read()
    print('added', values,"! Thanks for visiting my To-Do app")
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = get_todos()
            todos.remove(todo_to_complete)
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update('')
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break




# Finish up by removing from the screen
window.close()  # Part 5 - Close the Window