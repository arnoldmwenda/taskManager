from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str):
        return False

    title = title.strip()

    if len(title) < 3 or len(title) > 100:
        return False

    return True
    
def validate_task_description(description):
    if description is None:
        return True

    if not isinstance(description, str):
        return False

    if len(description) > 500:
        return False

    return True
    
def validate_due_date(due_date):
    if not isinstance(due_date, str):
        return False

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False