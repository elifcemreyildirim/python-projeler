to_do_list=[]

def add_task(to_do_list):
    task=input("enter the task= ")
    to_do_list.append(task)

def show_tasks(to_do_list):
    print(to_do_list)

def delete_task(to_do_list):
    task=input()
    to_do_list.remove(task)

while True:
    choice=input("1-2-3-4")


    if choice==1:
        add_task(to_do_list)
    elif choice==2:
        show_tasks(to_do_list)
    elif choice==3:
        delete_task(to_do_list)
    elif choice==4:
        break
    else:
        print("invalid selection.")
