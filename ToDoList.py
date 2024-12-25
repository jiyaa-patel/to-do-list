def show():
    with open('ToDoList.txt' , 'r') as file:
        content = file.read() 
        print(content)

def add():
    task = input("Enter task- ")
    deadline = input("Enter deadline- ")
    with open('ToDoList.txt' , 'r') as file:
        content = file.readlines()
        content.insert(1, "\n    " + task + "\n    " + deadline + "\n")
        addedtask = ''.join(content)
    with open('ToDoList.txt' , 'w') as file:
        file.write(addedtask)
    show()
    
def delete():
    deleteTask = int(input("Enter the number of the task to be delted: "))
    with open('ToDoList.txt', 'r') as file:
        content = file.readlines()
        del content[]
        
print("----------------> TO DO LIST <-------------------")
print("Select from the below: \n1.Show the list\n2.Add a new task\n3.Delete a task\n")
task = int(input(" "))

if task == 1:
    show()

elif task == 2:
    add()

elif task == 3:
    delete()