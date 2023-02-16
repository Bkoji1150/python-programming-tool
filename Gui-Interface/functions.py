
FILEPATH = 'todos.txt'


def get_todos(FILEPATH=FILEPATH):
    """ Read a text file and return the list of
     to-do items.
    """
    with open(FILEPATH) as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, FILEPATH=FILEPATH):
    """ Write to-do items in a text file. """
    with open(FILEPATH, 'w') as file_local:
        file_local.writelines(todos_arg)
    return None


if __name__ == "__main__":
    print("Hello from functions")
