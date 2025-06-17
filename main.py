import tkinter as tk
from tkinter import Tk ,Label, Button, messagebox, Frame



class ToDoList:
   def __init__(self):
      self.root=Tk()
      self.root.geometry('700x700+160+20')
      self.root.maxsize(width=1000,height=1000)
      self.root.title('To-Do List App')
      self.tasks=[]

      # Header
      header_label = Label(self.root, text="To-Do List App", font=("Courier New", 24,'bold'))
      header_label.pack(pady=20)

      label = Label(self.root, text="Welcome to your To Do List App\nyou can proceed with ur daily tasks <3", font=("Ink Free", 18))
      label.pack(pady=20)
      # frame 1
      f1=Frame(self.root,
               width=200,
               height=700,
               relief=tk.GROOVE,
               bg='lightblue',
               cursor='hand2',
               highlightbackground='lightblue',
               highlightthickness=100)
      f1.pack(padx=10,pady=10)

      #options
      option1=Button(f1,text='Add Task',font=('Arial',12),width=20,height=3,command=self.AddTaskWindow)
      option1.pack(pady=10,padx=10)
      option2=Button(f1,text='Remove Task',font=('Arial',12),width=20,height=3)
      option2.pack(pady=10,padx=10)
      option3=Button(f1,text='Complete Task',font=('Arial',12),width=20,height=3)
      option3.pack(pady=10,padx=10)
      self.root.mainloop()


   def AddTaskWindow(self):
      add_task_window=Tk()
      add_task_window.geometry('400x400+100+50')
      add_task_window.title('Add New Task')

      label = Label(add_task_window, text="Add Your New Task :3", font=("Ink Free", 18))
      label.pack(pady=20)

      f1=Frame(add_task_window,
               width=300,
               height=800,
               relief=tk.GROOVE,
               bg='lightblue',
               cursor='hand2',
               highlightbackground='lightblue',
               highlightthickness=0)
      f1.pack(padx=10,pady=10)

      # Task entry
      task_entry = tk.Entry(f1, width=35, font=("Arial", 14))
      task_entry.pack(pady=20)


      # Add task button
      add_task_button = tk.Button(f1, text="Add Task",command= lambda: self.addtask(task_entry.get()))                                     
      add_task_button.pack(pady=10)

   def addtask(self,task):
      if task:
            self.tasks.append(task)
            # self.task_list.insert(tk.END, task)
            # task_entry.delete(0, tk.END)
      else:
         print('error')
         messagebox.ERROR
      #   self.mark_completed_button.pack(side=tk.LEFT, padx=10)

      




# if __name__== "main":
t1=ToDoList()
