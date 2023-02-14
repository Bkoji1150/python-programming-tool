

def get_todos(path='file/todos.txt', mode='r'):
    """ Read a text file and return the list of
     to-do items.
    """
    with open(path) as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, path='file/todos.txt'):
    """ Write to-do items in a text file. """
    with open(path, 'w') as file_local:
        file_local.writelines(todos_arg)
    return None

if __name__ == "__main__":
    print("Hello from functions")
