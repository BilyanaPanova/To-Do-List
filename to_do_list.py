import datetime


def welcome():
    date = datetime.datetime.now()
    day = date.strftime("%A")
    print("=====TO-DO LIST=====")
    print(f"     {date.day}/{date.month}/{date.year}   ")
    print(f"     {day}   ")
    print("====================")


def show_menu():
    menu = ["Add Task", "Completed Task", "Add Priorities", "Completed Priorities", "View To-Do List",
            "Task For Tomorrow", "Quit"]
    for index, el in enumerate(menu, start=1):
        print(f"{index} - {el}")


def add_task(task_list):
    task = input("\nEnter your task:")
    task_list.append(task)
    print("Successfully added a task to your To-Do list.\n")


def add_priorities(priorities):
    priority = input("\nEnter your priority:")
    priorities.append(priority)
    print("Successfully added a priority to your To-Do list.\n")


def strike(text):
    result = ''
    for letter in text:
        result = result + letter + '\u0336'
    return result


def completed_priorities(priorities):
    for index, el in enumerate(priorities, start=1):
        print(f"{index} - {el}")
    index = int(input("\nPlease,enter the number of the completed priority:"))

    if 0 <= index <= len(priorities):
        priority = priorities.pop(index - 1)
        priorities.insert(index - 1, strike(priority))
        print("You successfully completed priority!\n")
    else:
        print("Invalid number!")
        completed_priorities(priorities)


def completed_task(task_list):
    for index, el in enumerate(task_list, start=1):
        print(f"{index} - {el}")
    index = int(input("\nPlease,enter the number of the completed task:"))

    if 0 <= index <= len(task_list):
        priority = task_list.pop(index - 1)
        task_list.insert(index - 1, strike(priority))
        print("You successfully completed task!\n")
    else:
        print("Invalid number!\n")
        completed_priorities(task_list)


def to_do_list_program():
    task_list = []
    priorities = []
    for_tomorrow = []
    welcome()
    while True:
        show_menu()
        choice = input("\nEnter your choice:")

        if choice == "1":
            add_task(task_list)
        elif choice == "3":
            add_priorities(priorities)
        elif choice == "5":
            welcome()
            print("Priorities:")
            for index, el in enumerate(priorities, start=1):
                print(f"{index} - {el}")
            print("-------------------")
            print("To do:")
            for index, el in enumerate(task_list, start=1):
                print(f"{index} - {el}")
            print("--------------------")
            print("For tomorrow:")
            for index, el in enumerate(for_tomorrow, start=1):
                print(f"{index} - {el}")
            print("---------------------")
        elif choice == "4":
            completed_priorities(priorities)
        elif choice == "2":
            completed_task(task_list)
        elif choice == "6":
            task = input("\nPlease,enter your task: ")
            for_tomorrow.append(task)
            print("You successfully added task for tomorrow.\n")
        elif choice == "7":
            print("~What ever you decide to do,make sure it makes you HAPPY!~")
            break
        else:
            print("Invalid choice! \nPlease,enter a number between 1-7.\n")


to_do_list_program()
