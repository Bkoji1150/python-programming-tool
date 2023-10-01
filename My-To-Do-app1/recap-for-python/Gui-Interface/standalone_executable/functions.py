import os
FILEPATH = 'todos.txt'

if not os.path.exists(FILEPATH):
    with open(FILEPATH, 'w') as file:
        pass

def get_todos(FILEPATH=FILEPATH):
    """ Read a text file and return the list of
     to-do items.
    """
    with open(FILEPATH) as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(content, FILEPATH=FILEPATH):
    """ Write to-do items in a text file. """
    with open(FILEPATH, 'w') as file_local:
        file_local.writelines(content)
    return None

if __name__ == "__main__":
    print("Hello from functions")
