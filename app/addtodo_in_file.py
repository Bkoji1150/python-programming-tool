
while True:
    user_action = input("Type add, show, edit, complete, exit todo list: ").strip().lower()
    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + "\n"
            with open('file/todos.txt') as file:
                todos = file.readlines()

            todos.append(todo)
            with open('file/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open('file/todos.txt') as file:
                todos = file.readlines()

            for index, item in enumerate(todos, 1):
                item = item.strip("\n")
                print(f"{index}.: {item.title()}")

        case 'edit':
            number = int(input('Number of the todo to edit: '))
            number = number - 1

            with open('file/todos.txt') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open('file/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input('Number of the todo to complete: '))

            with open('file/todos.txt') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_removed = todos[index].strip('\n')
            todos.pop(index)

            with open('file/todos.txt', 'w') as file:
                file.writelines(todos)

            print(f"Item with name: {todo_to_removed} was removed from your todo list")

        case 'exit' | 'q' | 'quite':
            break
        case _:
            print('Sorry command was not valid')

print('Thanks for visiting!')