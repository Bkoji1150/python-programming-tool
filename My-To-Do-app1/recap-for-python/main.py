

file_name = 'files/todos.txt'

while True:
    user_action = input("Type add, show, edit, complete: ").lower()
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        with open(file_name) as file:
            todos = file.readlines()

        todos.append(todo)

        with open(file_name, 'w') as file:
            file.writelines(todos)

    elif  user_action.startswith('show'):
        with open(file_name) as file:
                todos = file.readlines()

        for item,v in enumerate(todos, 1):
            v = v.strip('\n')
            print(f"{item}. {v.capitalize()}")
    elif  user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            with open(file_name) as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"
            with open(file_name, 'w') as file:
                file.writelines( todos)

        except ValueError:
            print(f"Ooops! please provide only number.")
        except IndexError:
            print(f"Index number {number} doesn't exist")

    elif  user_action.startswith('complete'):

        try:
            number = int(user_action[9:])

            with open(file_name) as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            with open(file_name, 'w') as file:
                file.writelines(todos)
            print(f"Todo item '{todo_to_remove}' was removed from the list.")

        except ValueError:
            print("please provide only number.")
        except IndexError:
            print(f"Index number {number} doesn't exist")
    elif user_action.startswith('exit'):
        print("Thanks for visiting my website.")
        break
    else:
        print("Please type in either: (add, show, edit, complete and exit to end the program).")

print("Bye!")
