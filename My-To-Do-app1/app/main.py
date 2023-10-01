
#
# user_prompt = "Enter a todo: "
#
# todos = []
#
# while True:
#     todo = input(user_prompt)
#     todos.append(todo)
#     print(todos)

# user_action = input("Type add, show, edit, complete, exit todo list: ").strip()

todo = input('Enter a todo: ') + "\n"
file = open('file/todos.txt', 'r')
todos = file.readlines()
file.close()

todos.append(todo)
file = open('file/todos.txt', 'w')
file.writelines(todos)
file.close()