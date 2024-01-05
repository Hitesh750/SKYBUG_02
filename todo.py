from tkinter import *
import tkinter.messagebox
from tkinter import simpledialog

root=Tk()
root.title("ToDo App")

def task_adding():
    task=add_task.get()
    
    if task!="":
        todo_box.insert(END,task)
        add_task.delete(0,END)
    else:
         Message(title="Attention",Message="Are you want to delete")

def remove_task():
        task_removing=todo_box.curselection()[0]
        todo_box.delete(task_removing)
    
def update_task():
    selected_index = todo_box.curselection()
    if selected_index:
        new_text = add_task.get()
        todo_box.delete(selected_index)
        todo_box.insert(selected_index,new_text)
        add_task.delete(0, END) 
           

list_frame=Frame(root)
list_frame.pack()

todo_box=Listbox(list_frame,height=20,width=50)
todo_box.pack(side=LEFT)

scroller=Scrollbar(list_frame)
scroller.pack(side=RIGHT,fill=Y)
todo_box.config(yscrollcommand=scroller.set)
#scroller.config(command=list_frame.yview)

add_task=Entry(root,width=50)
add_task.pack()


add_task_button=Button(root,text="Add Task",font=("arial",10,"bold"),background="blue",width=20 ,command=task_adding)
add_task_button.pack()

remove_task_button=Button(root,text="Remove task",background="red",width=20,font=("arial",10,"bold"),command=remove_task)
remove_task_button.pack()

update_task_button=Button(root,text="Update task",background="Green",width=20,font=("arial",10,"bold"),command=update_task)
update_task_button.pack()




root.mainloop()