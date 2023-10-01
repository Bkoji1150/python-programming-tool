
while True:
    user_action = input("Type add, show, edit, complete, exit todo list: ").strip().lower()

    if user_action.startswith('add'):
        todo = user_action[4:]

        with open('file/todos.txt') as file:
            todos = file.readlines()

        todos.append(todo + "\n")
        with open('file/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):

        with open('file/todos.txt') as file:
            todos = file.readlines()

        for index, item in enumerate(todos, 1):
            item = item.strip("\n")
            print(f"{index}.: {item.title()}")

    elif user_action.startswith('edit'):
        number = int(user_action[5:])
        number = number - 1

        with open('file/todos.txt') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"

        with open('file/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('complete'):
        number = int(user_action[9:])

        with open('file/todos.txt') as file:
            todos = file.readlines()

        index = number - 1
        todo_to_removed = todos[index].strip('\n')
        todos.pop(index)

        with open('file/todos.txt', 'w') as file:
            file.writelines(todos)

        print(f"Item with name: {todo_to_removed} was removed from your todo list")

    else:
        print('ended the program!')
        break

print('Thanks for visiting!')