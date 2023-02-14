
todos = []

while True:
    user_action = input("Type add or show or exit: ").strip()
    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                print(item.title())
        case 'exit' | 'q' | 'quite':
            break
        case _:
            print('Sorry command was not valid')


print('Bye')
