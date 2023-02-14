

todos = []

while True:
    user_action = input("Type add, show, edit, complete, exit todo list: ").strip().lower()
    match user_action:

        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)

        case 'show' | 'display':
            for index, item in enumerate(todos, 1):
                print(f"{index}.: {item.title()}")

        case 'edit':
            number = int(input('Number of the todo to edit: '))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case 'complete':
            number = int(input('Number of the todo to complete: '))
            todos.pop(number - 1)

        case 'exit' | 'q' | 'quite':
            break
        case _:
            print('Sorry command was not valid')

print('Bye')