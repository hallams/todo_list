#i will add this file to github
tasks = []

while True:

    print(message)

    choice = input("Enter your choice:")

    if choice == "1":

        # add task to tasks list

        add_task()

    elif choice == "2":

        mark_task_complete()

    elif choice == "3":

        view_tasks()

    elif choice == "4":

        break

    else:

        print("Invalid choice, please enter a number between 1 and 4")