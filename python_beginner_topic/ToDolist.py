todolist = []
completetodo = []

def addTodo():
    todocontent = input("YOUR TODO: ")
    todolist.append(todocontent)
    viewAllTodo()

def viewAllTodo():
    if len(todolist) > 0:
        print("\n======== All TODOS ========")
        for i, todo in enumerate(todolist, start=1):
            print(f"{i}) {todo}")
    else:
        print("\nNothing is there.")        

def deleteTodo():
    viewAllTodo()
    if len(todolist) == 0:
        return
    toDonum = int(input("\nEnter todo number which you want to delete: "))
    if 1 <= toDonum <= len(todolist):
        deleted = todolist.pop(toDonum - 1)
        print(f'"{deleted}" deleted successfully!')
    else:
        print(f"Todo {toDonum} not found.")
    viewAllTodo()

def completed():
    viewAllTodo()
    if len(todolist) == 0:
        return
    completedtodo = int(input("\nEnter completed Todo number: "))
    if 1 <= completedtodo <= len(todolist):
        done = todolist.pop(completedtodo - 1)
        completetodo.append(done)
        print(f'"{done}" marked as completed!')
    else:
        print(f"Todo {completedtodo} not found.")
    viewAllTodo()

def todocompleted():
    while True:
        print("\n1) View All Completed Todos")
        print("2) Mark a Todo as Completed")
        print("3) Back")
        choice = int(input("Please Select an Option: "))

        if choice == 1:
            if len(completetodo) > 0:
                print("\n===== Completed Todos =====")
                for i, com in enumerate(completetodo, start=1):
                    print(f"{i}) {com}")
            else:
                print("\nNo completed todos yet.")
        elif choice == 2:
            completed()
        elif choice == 3:
            break
        else:
            print(f"Option {choice} is invalid.")

while True:
    print("\n==== TODO MANAGER ====")
    print("1) Add Todo")
    print("2) View All Todos")
    print("3) Delete Todo")
    print("4) Completed Section")
    print("5) Exit")
    choice = int(input("Please Select an Option: "))

    if choice == 1:
        addTodo()
    elif choice == 2:
        viewAllTodo()
    elif choice == 3:
        deleteTodo()
    elif choice == 4:
        todocompleted()
    elif choice == 5:
        print("Goodbye!")
        break    
    else: 
        print(f"Option {choice} is invalid.")
