import functions
import time

print("It is ", time.strftime("%b %d, %Y %H:%M:%S"))

while True:
    user_action = input("enter your choice\nshow, add, complete, edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("show"):
        todos = functions.get_todos()
        todos = [item.strip('\n') for item in todos]  # List Comprehension.
        for index, item in enumerate(todos):
            print(f"{index + 1}-{item}")

    elif user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)
        x = todo.strip('\n')
        print(f"{x} is successfully added.")

    elif user_action.startswith("edit"):
        try:  # error handling
            todos = functions.get_todos()
            number = int(user_action[5:])
            todo_to_edit = todos[number - 1].strip("\n")
            new_todo = input("enter new todo to replace: ")
            todos[number - 1] = new_todo + "\n"
            functions.write_todos(todos)
            print(f"{todo_to_edit} is successfully replaced with {new_todo}.")
        except ValueError:
            print("your command is not valid!!\nuse 'show' and use the corresponding index.")
            continue
        except IndexError:
            print("enter index with in range!!\nuse 'show' and use the corresponding index.")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()
            number = int(user_action[9:])
            todo_to_remove = todos[number - 1].strip("\n")
            todos.pop(number - 1)
            functions.write_todos(todos)
            print(f"{todo_to_remove} is removed from todos.")
        except ValueError:
            print("your command is not valid!!\nuse 'show' and use the corresponding index.")
            continue
        except IndexError:
            print("enter index with in range!!\nuse 'show' and use the corresponding index.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("command is not valid!!")

print("thanks!!")
