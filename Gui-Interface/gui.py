from functions import get_todos, write_todos
import PySimpleGUI as sg
import time

clock = sg.Text('',key='clock')
sg.theme('Black')

layout = [[clock],
          [sg.Text("Type a to-do")],
          [sg.InputText(key="todo"), sg.Button("Add")],
          [sg.Listbox(values=get_todos(),
            key='todos',
            enable_events=True,
            size=[45,10]),
          sg.Button("Edit"), sg.Button("Complete")],
          [sg.Button('Exit', size=10)]
        ]

# Create the window
window = sg.Window('My To-Do App', layout, font=('Helvetica', 20),)

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print('added', values,"! Thanks for visiting my To-Do app")
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select an item first',font=('Helvetica', 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = get_todos()
                todos.remove(todo_to_complete)
                write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update('')
            except IndexError:
                sg.popup('Please select an item first', font=('Helvetica', 20))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()