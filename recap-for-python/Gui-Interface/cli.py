from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y, %H:%M:%S")
print(f"Time is: {now}")

while True:
    user_action = input("Type add, show, edit, complete: ").lower()
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        # Calling read function
        todos = get_todos()

        todos.append(todo)

        # Calling read function
        write_todos(todos)

    elif  user_action.startswith('show'):
        # Calling read function
        todos = get_todos()

        for item,v in enumerate(todos, 1):
            v = v.strip('\n')
            print(f"{item}. {v.capitalize()}")
    elif  user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            # Calling read function
            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"
            # Calling read function
            write_todos(todos)

        except ValueError:
            print(f"Ooops! please provide only number.")
        except IndexError:
            print(f"Index number {number} doesn't exist")

    elif  user_action.startswith('complete'):

        try:
            number = int(user_action[9:])

            # Calling read function
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            # Calling read function
            write_todos(todos)
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
