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
    if ans==2:
        markcomplete(todo_list)

main()

def addtasks(todo_list):
    num_tasks=int(input("Enter the amount of tasks you want to add to the list: "))
    for i in range(num_tasks):
        task=input("Enter the title of the task: ")
        todo_list[task]="incomplete"

def markcomplete(todo_list):
    num_tasks=int(input("Enter the amount of tasks you want to mark as complete: "))
    for i in range(num_tasks):
        target=input("Enter the name of the task you want to mark as complete: ")
        todo_list[target]="complete"
