

tasks = []


def addtask(tasks):
    task = input("Enter task description: ")
    tasks.append(task)
    print("\n Task added successfully!") 
    
def viewtasks(tasks):
    if tasks:
        print("\nTasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print('No task to show. Please add task. ')
    

def marktaskasdone(tasks):
    if not tasks:
        print("No tasks to mark as done.")
        return

    viewtasks(tasks)  
    index = int(input("Enter task index to mark as done: ")) - 1


    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f" Task '{removed_task}' marked as done and removed.")
    else:
        print("Invalid task index.")

while True:
    print('\n\n 1. Add task \n 2. View tasks \n 3. Mark task as done  \n 4. Exit')
    n=int(input("Enter your choice: "))
    if n == 1:
        addtask(tasks)
    elif n == 2:
        viewtasks(tasks)
    elif n == 3:
        marktaskasdone(tasks)
    elif n == 4:
        print("Exit")
        break
    else:
        print("Invalid input")




