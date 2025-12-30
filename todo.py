def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Task deleted")
    else:
        print("Invalid task index")

