from datetime import datetime

# Import validation functions
from .validation import validate_due_date, validate_task_description, validate_task_title

# Define tasks list
tasks = [{"title": "",
          "description": "",
          "due_date": "",
          "completed": False}]

# Implement add_task function
def add_task(title, description, due_date):
    if not validate_task_title(title):
        raise ValueError("Invalid task title")

    if not validate_task_description(description):
        raise ValueError("Invalid task description")

    if not validate_due_date(due_date):
        raise ValueError("Invalid due date")

    newTask = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date,
        "completed": False,
    }

    tasks.append(newTask)
    print("Task added successfully!")
    return newTask
    
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        return True
    print("Task marked as complete!")
    return False
   
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    return [task for task in tasks if not task["completed"]]

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0.0

    completed = sum(1 for task in tasks if task["completed"])
    progress = (completed / len(tasks)) * 100
    return progress
    