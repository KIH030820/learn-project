def load_tasks():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")