# indices = [i for i, x in enumerate(my_list) if x == 20]

import os
os.chdir("D:/git/to-do-list")
# print("Changed working directory:", os.getcwd())
# print("Current working directory:", os.getcwd())

def show():                                                     #Show the to-do-list by read the whole file
    with open('ToDoList.txt' , 'r') as file:
        content = file.read() 
        print(content)

def add():                                                      #Add a task by reading the lines and adding it at the top using .readlines(convert it to list), .insert(to insert at index 1 in the list) & .join to convert list to string
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

def delete():                                                    #Delete a task
    show()
    deleteTask = int(input("Enter the number of the task to be deleted: "))
    with open('ToDoList.txt', 'r') as file:
        content = file.readlines()
        # print(content)
        index = [i for i,x in enumerate(content) if x == '\n']    #Index of all \n to get the ending of tasks 
        # print(index)
        deleteTaskIndex = index[deleteTask-1]                     #To get that index of \n of which the task is to be deleted (if its the first task we get the 0th index of the lists of index(containing \n))
        # print(deleteTaskIndex)
        del content[deleteTaskIndex]                              #Delete the task (the line containing \n, line containing date and that containing task name)
        del content[deleteTaskIndex-1] 
        del content[deleteTaskIndex-2]
        deletedTasks = ''.join(content)                           #Convert the list to string to write to the file
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