FILEPATH = "todo.txt"


def get_todos(filepath=FILEPATH):
    """ it takes file path as argument and returns the list of todos. """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ it takes todos list and file path and over write todos_arg in that file. """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())
