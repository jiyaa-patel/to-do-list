def show():
    with open('ToDoList.txt' , 'r') as file:
        content = file.read() 
        print(content)


print("----------------> TO DO LIST <-------------------")
print("Select from the below: \n1.Show the list\n2.Add a new task\n3.Delete a task\n")
task = int(input(" "))
# print(task)
if task == 1:
    show()
