task = ["drinking", "eating","walking"]
while True:
    print("welcome to your today to_do list ")
    print("1. view the task")
    print("2. add task")
    print("3. remove a task ")
    print("4. exit")
    chose = int(input("enter your choice from(1 to 5):"))
    if chose == 1:
        if not task :
            print("no task ")
        else :
            for i ,task in enumerate(task,start=1):
                print(i,task)
    elif chose == 2:
        new_task = input("enter a new task: ")
        task.append (new_task)
        print("new task added")

    elif chose == 3 :
        remove_index = int(input("enter the index of the task you want to remove: "))
        if 1 <= remove_index <= len(task):
            task.pop (remove_index - 1)
            print("task successfully removed")
        else:
            print("invalid index ")
            print("task not found")
    elif chose == 4 :
        print("bye ")
        print("have a nice day")
        break
    else:
        print("invalid choice")

