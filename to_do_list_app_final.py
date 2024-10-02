def add_task():
    print()
    try:
        amount_tasks = int(input("How many tasks would you like to add?\n"))
        try:
            for i in range(amount_tasks):
                task = input("Enter the task you would like to add to the list:\n")
                if task not in to_do_list:
                    to_do_list.append({"task": task, "complete": False})
                    print(f"{task} added to To-Do list.\n")
                else:
                    print("This task is already on your To-Do list.\n")
        except ValueError:
            print("Invalid input. Please enter letters only.\n")

    except ValueError:
        print("Invalid input. Please enter a number.\n")


def view_tasks():
    print("\nTasks:")
    for index, task in enumerate(to_do_list):
        status = "Complete" if task["complete"] else "Incomplete"
        print(f"{index + 1}. {task['task']} - {status}")


def complete_task():
    try:
        task_index = int(
            input("Enter the task number you would like to mark as complete:\n")
        )
        if 0 <= task_index <= len(to_do_list):
            to_do_list[task_index - 1]["complete"] = True
            print("Task marked as complete")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def delete_task():
    try:
        del_task = int(
            input("Enter the number of the task you would like to delete:\n")
        )
        if 1 <= del_task <= len(to_do_list):
            deleted_task = to_do_list.pop(del_task - 1)
            print(f"Task '{deleted_task['task']}' has been deleted.\n")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


to_do_list = []
print("\n-----Welcome to the To-Do List App!-----\n")
while True:
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")
    try:
        user_choice = int(input("Enter choice:\n"))

        if user_choice == 1:
            add_task()
        elif user_choice == 2:
            view_tasks()
        elif user_choice == 3:
            complete_task()
        elif user_choice == 4:
            delete_task()
        elif user_choice == 5:
            print("Have a nice day!")
            break
        else:
            print("Please enter a valid choice from the list [1-5]")
    except ValueError:
        print("Invalid input. Please enter numbers only. [1-5]")
