

file_name = 'files/todos.txt'

while True:
    user_action = input("Type add, show, edit, complete: ").lower()
    user_action = user_action.strip()

    if user_action == 'add':
        todo = input("Enter a todo: ") + "\n"
        with open(file_name) as file:
            todos = file.readlines()

        todos.append(todo)

        with open(file_name, 'w') as file:
            file.writelines(todos)

    elif  user_action == 'show':
        with open(file_name) as file:
                todos = file.readlines()

        for item,v in enumerate(todos, 1):
            v = v.strip('\n')
            print(f"{item}. {v.capitalize()}")
    elif  user_action == 'edit':

        try:
            number = int(input("Number of the item to edit:  "))
            number = number - 1
            with open(file_name) as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"
            with open(file_name, 'w') as file:
                file.writelines( todos)

        except ValueError:
            print("please provide only number.")

    elif  user_action == 'complete':

        try:
            number = int(input("Number of the item to complete:  "))

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
    else:
        break

print("Bye!")
