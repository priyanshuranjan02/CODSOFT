# Simple To-Do List in Python

# Define the list to store tasks
tasks = []

def add_task(description):
    "Add a new task to the to-do list."
    task = {"description": description, "done": False}
    tasks.append(task)
    print(f'Task "{description}" added.')

def view_tasks():
    "View all tasks in the to-do list."
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. {task['description']} - {status}")

def mark_task_done(task_number):
    "Mark a task as done."
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        print(f'Task {task_number} marked as done.')
    else:
        print("Invalid task number.")

def delete_task(task_number):
    "Delete a task from the to-do list."
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'Task "{removed_task["description"]}" deleted.')
    else:
        print("Invalid task number.")

def main():
    "Main loop to run the to-do list application."
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            description = input("Enter task description: ")
            add_task(description)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to mark as done: "))
            mark_task_done(task_number)
        elif choice == "4":
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main loop
if __name__ == "__main__":
    main()
