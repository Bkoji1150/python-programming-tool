from functions import get_todos, write_todos

while True:
    user_action = input("Type add, show, edit, complete, exit todo list: ").strip().lower()
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()
        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show') or user_action.startswith('list'):
        todos = get_todos()

        for index, item in enumerate(todos, 1):
            item = item.strip('\n')
            print(f"{index}.: {item.title()}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print('Your command was invalid\nPlease Enter just a number.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()

            index = number - 1
            todo_to_removed = todos[index].strip('\n')
            todos.pop(index)

            write_todos( todos)

            print(f"Item with name '{todo_to_removed}' was removed from your todo list")
        except IndexError:
            print(f"Item with index {index} isn't available in the list")
    else:
        print('Ended the program!')
        break

if __name__ == "__main__":
    print('Thanks for visiting!')

