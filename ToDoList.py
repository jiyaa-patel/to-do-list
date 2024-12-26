# indices = [i for i, x in enumerate(my_list) if x == 20]

import os
os.chdir("D:/git/to-do-list")
# print("Changed working directory:", os.getcwd())
# print("Current working directory:", os.getcwd())

def show():
    with open('ToDoList.txt' , 'r') as file:
        content = file.read() 
        print(content)

def add():
    task = input("Enter task- ")
    deadline = input("Enter deadline- ")
    with open('ToDoList.txt' , 'r') as file:
        content = file.readlines()
        print(content)
        content.insert(1, "    " + task + "\n    " + deadline + "\n\n")
        addedTask = ''.join(content)
    with open('ToDoList.txt' , 'w') as file:
        file.write(addedTask)
    show()

def delete():
    show()
    deleteTask = int(input("Enter the number of the task to be deleted: "))
    with open('ToDoList.txt', 'r') as file:
        content = file.readlines()
        print(content)
        index = [i for i,x in enumerate(content) if x == '\n']
        print(index)
        deleteTaskIndex = index[deleteTask-1]
        print(deleteTaskIndex)
        print(content[deleteTaskIndex-1] + " , " + content[deleteTaskIndex-2])
        del content[deleteTaskIndex]
        del content[deleteTaskIndex-1] 
        del content[deleteTaskIndex-2]
        deletedTasks = ''.join(content)
    with open('ToDoList.txt', 'w') as file:
        file.write(deletedTasks)
    show()
        
print("----------------> TO DO LIST <-------------------")
print("Select from the below: \n1.Show the list\n2.Add a new task\n3.Delete a task\n")
task = int(input(" "))

if task == 1:
    show()

elif task == 2:
    add()

elif task == 3:
    delete()