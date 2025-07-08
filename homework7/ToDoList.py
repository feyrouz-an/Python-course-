import random

def add_task():
    name = input("Task Name: ")
    description = input("Description: ")
    tag = input("Tag (High/Low): ").capitalize()
    task = {
        "id": random.randint(1000, 9999),
        "name": name,
        "description": description,
        "status": "New",
        "tag": tag
    }
    return task

def search_task(tasks):
    search_by = input("Search by (1) ID or (2) Name? Enter 1 or 2: ")
    if search_by == "1" :
        search_id = int(input("Enter Task ID: "))
        for task in tasks:
            if task["id"] == search_id:
                print(f"Found Task: ID: {task['id']}, Name: {task['name']}, Desc: {task['description']}, Status: {task['status']}, Tag: {task['tag']}")
                return
        print("No task found with that ID.")
    elif search_by == "2":
        search_name = input("Enter Task Name: ")
        for task in tasks:
            if task["name"].lower() == search_name.lower():
                print(f"Found Task: ID: {task['id']}, Name: {task['name']}, Desc: {task['description']}, Status: {task['status']}, Tag: {task['tag']}")
                return
        print("No task found with that name.")
    else:
        print("Invalid option. Please enter 1 or 2.")

def delete_task(tasks):
    search_by = input("Delete by (1) ID or (2) Name? Enter 1 or 2: ")
    if search_by == "1":
        delete_id = int(input("Enter Task ID to delete: "))
        for task in tasks:
            if task["id"] == delete_id:
                tasks.remove(task)
                print(f"Task with ID {delete_id} deleted.")
                return
        print("No task found with that ID.")
    elif search_by == "2":
        delete_name = input("Enter Task Name to delete: ")
        for task in tasks:
            if task["name"].lower() == delete_name.lower():
                tasks.remove(task)
                print(f"Task '{delete_name}' deleted.")
                return
        print("No task found with that name.")
    else:
        print("Invalid option. Please enter 1 or 2.")

def update_status(tasks):
    search_by = input("Update status by (1) ID or (2) Name? Enter 1 or 2: ")
    if search_by == "1":
        update_id = int(input("Enter Task ID to update status: "))
        for task in tasks:
            if task["id"] == update_id:
                new_status = input("Enter new status (New/Completed): ").capitalize()
                task["status"] = new_status
                print(f"Status of Task ID {update_id} updated to {new_status}.")
                return
        print("No task found with that ID.")
    elif search_by == "2":
        update_name = input("Enter Task Name to update status: ")
        for task in tasks:
            if task["name"].lower() == update_name.lower():
                new_status = input("Enter new status (New/Completed): ").capitalize()
                task["status"] = new_status
                print(f"Status of Task '{update_name}' updated to {new_status}.")
                return
        print("No task found with that name.")
    else:
        print("Invalid option. Please enter 1 or 2.")

def list_tasks(tasks):
    print("\n--- All Tasks ---")
    for task in tasks:
        print(
            f"ID: {task['id']}\n"
            f"Name: {task['name']}\n"
            f"Description: {task['description']}\n"
            f"Status: {task['status']}\n"
            f"Tag: {task['tag']}\n"
            "------------------"
        )
    if not tasks:
        print("No tasks available.")

def filter_tasks(tasks):
    print("Filter by:")
    print("1. Tag (High/Low)")
    print("2. Status (New/Completed)")
    print("3. Both Tag and Status")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        tag = input("Enter tag (High/Low): ").capitalize()
        filtered = [task for task in tasks if task["tag"] == tag]
    elif choice == "2":
        status = input("Enter status (New/Completed): ").capitalize()
        filtered = [task for task in tasks if task["status"] == status]
    elif choice == "3":
        tag = input("Enter tag (High/Low): ").capitalize()
        status = input("Enter status (New/Completed): ").capitalize()
        filtered = [task for task in tasks if task["tag"] == tag and task["status"] == status]
    else:
        print("Invalid choice. Showing all tasks.")
        filtered = tasks

    if not filtered:
        print("No tasks match the selected filters.")
    else:
        print("\n--- Filtered Tasks ---")
        for task in filtered:
            print(
                f"ID: {task['id']}\n"
                f"Name: {task['name']}\n"
                f"Description: {task['description']}\n"
                f"Status: {task['status']}\n"
                f"Tag: {task['tag']}\n"
                "------------------"
            )

def show_statistics(tasks):
    print("\n--- Task Statistics ---")
    total_tasks = len(tasks)
    new_tasks = sum(task["status"] == "New" for task in tasks)
    completed_tasks = sum(task["status"] == "Completed" for task in tasks)
    high_priority = sum(task["tag"] == "High" for task in tasks)
    low_priority = sum(task["tag"] == "Low" for task in tasks)

menu_options = {
    "1": ("Add a new task", add_task),
    "2": ("Search for a task", search_task),
    "3": ("Delete a task", delete_task),
    "4": ("Update task status", update_status),
    "5": ("List all tasks", list_tasks),
    "6": ("Filter tasks", filter_tasks),
    "7": ("Show statistics", show_statistics),
    "q": ("Quit", None)  # Special case for quitting
}

tasks = [] 

def main():
    while True:
        # Display menu
        print("\n--- To-Do List Manager ---")
        for key, (description, _) in menu_options.items():
            print(f"{key}. {description}")

        # Get user choice
        choice = input("\nEnter your choice (1-7/q): ").strip().lower()

        # Handle quit option
        if choice == "q":
            print("Goodbye!")
            break

        # Execute the chosen function
        if choice in menu_options:
            func = menu_options[choice][1]
            func(tasks)  # Pass the tasks list to the function
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()