def main():
    print("""Welcome to the to do list editior
    Please enter the number of the command you want
    1.) Add a new task
    2.) Mark a task as complete
    3.) View your list
    4.) Delete tasks""")
    ans=input()
    todo_list={}
    if ans==1:
        addtasks(todo_list)
        print("Your to do list has now been updated")

main()

def addtasks(todo_list):
    num_tasks=int(input("Enter the amount of tasks you want to add to the list: "))
    for i in range(num_tasks+1):
        task=input("Enter the title of the task: ")
        todo_list[task]="incomplete"