# Import functions from task_manager.task_utils package
from task_manager import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks

# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)
        elif choice == "2":
            index = int(input("Task index: "))
            mark_task_as_complete(index, tasks)
        elif choice == "3":
            print(view_pending_tasks(tasks))
        elif choice == "4":
            print(f"Progress: {calculate_progress(tasks):.2f}%")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
