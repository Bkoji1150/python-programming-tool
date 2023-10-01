from functions import get_todos, write_todos
import PySimpleGUI as sg
import time


clock = sg.Text('',key="clock")
# sg.theme('Black')

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo",key="todo")
add_button = sg.Button(size=2,image_source='images/add.png', mouseover_colors='LightBlue2',
                     tooltip='add ToDo', key='Add')
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=get_todos(),
            key='todos',
            enable_events=True,
            size=[45,10]
)
complete_box = sg.Button('Complete')
refresh_button = sg.Button("Refresh")

layout = [
        [clock],
        [label],
        [input_box, add_button],
        [list_box, edit_button,complete_box],
        [sg.Button('Exit', size=10),refresh_button]
]
window = sg.Window('My To-Do App',
         layout=layout,
         font=('Helvetica', 20)
)

while True:
    event,values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print('added', values,"! Thanks for visiting my To-Do app")
    if event == "Add":
        todos = get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        write_todos(todos)
        window['todos'].update(values=todos)
    if event == "Edit":
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
#             if len(new_todo)
            todos = get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            write_todos(todos)
            window['todos'].update(values=todos)
        except IndexError:
            sg.popup('Please select an item first',font=('Helvetica', 20))
    if event == "Complete":
         try:
            todo_to_complete = values['todos'][0]
            todos = get_todos()
            todos.remove(todo_to_complete)
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update('')
         except IndexError:
            sg.popup('Please select an item first', font=('Helvetica', 20))
    if event == 'todos':
        window['todo'].update(value=values['todos'][0])
    if event == "Refresh":
       todos = get_todos()
       window['todos'].update(values=todos)
    if event == 'Exit':
        break
    if event == sg.WIN_CLOSED:
        break


window.close()