tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

add_task("GitHub hesabı aç")
add_task("Legion Score yükselt")
show_tasks()
