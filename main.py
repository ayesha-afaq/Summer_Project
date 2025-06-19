import tkinter as tk
from tkinter import Tk,messagebox,Label,Button,Frame,Entry,Listbox

class ToDoList:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('700x700+160+20')
        self.root.maxsize(width=1000, height=1000)
        self.root.title('To-Do List App')
        self.tasks = {}
        
        # Create main container frame
        self.container = Frame(self.root)
        self.container.pack(fill="both", expand=True)
        
        # Create all frames but don't show them yet
        self.create_main_menu()
        self.create_add_task_view()
        self.create_delete_task_view()
        self.create_complete_task_view()
        
        # Show the main menu initially
        with open('tasklist.txt','r') as f:
                tasks=f.readline().split(',')
                if len(tasks)>1:
                    for i in tasks:
                        if len(i)>1:
                            self.tasks[i.split('|')[0]]=i.split('|')[1]

        self.main_menu_frame.pack(fill="both", expand=True)
        # self.show_frame("main_menu")
        
        self.root.mainloop()
    
    def create_main_menu(self):
        # Main menu frame
        self.main_menu_frame = Frame(self.container)
        
        # Header
        header_label = Label(self.main_menu_frame, 
                              text="To-Do List App", 
                              font=("Courier New", 24, 'bold'))
        header_label.pack(pady=20)
        
        label = Label(self.main_menu_frame, 
                        text="Welcome to your To Do List App\nyou can proceed with ur daily tasks <3", 
                        font=("Ink Free", 18))
        label.pack(pady=20)
        
        # Options frame
        f1 = Frame(self.main_menu_frame,
                     width=400,
                     height=700,
                     relief=tk.GROOVE,
                     bg='lightblue',
                     cursor='hand2',
                     highlightthickness=50)
        f1.pack(padx=10, pady=10)
        
        # Buttons
        option1 =Button(f1, text='Add Task', font=('Arial',12), 
                          width=20, height=3, 
                          command=lambda: self.show_frame("add_task"))
        option1.pack(pady=10, padx=10)
        
        option2 = Button(f1, text='Remove Task', font=('Arial',12), 
                          width=20, height=3,
                          command= lambda: self.show_frame('remove_task'))
        option2.pack(pady=10, padx=10)
        
        option3 = Button(f1, text='Complete Task', font=('Arial',12), 
                          width=20, height=3,
                          command= lambda: self.show_frame('complete_task'))
        option3.pack(pady=10, padx=10)
    
    def create_add_task_view(self):
        # Add task frame
        self.add_task_frame = Frame(self.container)
        
        # Header
        label = Label(self.add_task_frame, 
                        text="Add Your New Task :3", 
                        font=("Ink Free", 18))
        label.pack(pady=20)
        
        # Content frame
        f1 =Frame(self.add_task_frame,
                     width=200,
                     height=300,
                     relief=tk.GROOVE,
                     bg='lightblue')
        f1.pack(padx=10, pady=10)
        
        # Task entry
        self.task_entry =Entry(f1, width=35, font=("Arial", 14))
        self.task_entry.pack(pady=20)
        
        # Buttons
        add_btn = Button(f1, text="Add Task", command=self.add_task)
        add_btn.pack(side="left", padx=10)
        
        back_btn = Button(f1, text="Back", 
                           command=lambda: self.show_frame("main_menu"))
        back_btn.pack(side="right", padx=10)


    def create_delete_task_view(self):
        #delte task frame
        self.delete_task_frame=Frame(self.container)

        # Content frame
        f1 =Frame(self.delete_task_frame,
                     width=200,
                     height=300,
                     relief=tk.GROOVE,
                     bg='lightblue')
        f1.pack(padx=10, pady=10)

        # Header
        label = Label(f1, 
                        text="Remove as many tasks as u want :3", 
                        font=("Ink Free", 18))
        label.pack(pady=20)
        

        self.task_list = Listbox(f1, width=40, font=("Arial", 14),selectmode="multiple")
        self.task_list.pack(pady=20)


        for index,task in enumerate(self.tasks.keys(),start=1):
            self.task_list.insert('end',f'{task}')

        remove_btn = Button(f1, text="Remove", command=self.remove_task)
        remove_btn.pack(side="left", padx=10)

        back_btn = Button(f1, text="Back", 
                           command=lambda: self.show_frame("main_menu"))
        back_btn.pack(side="right", padx=10)
            

    def create_complete_task_view(self):
        # Add task frame
        self.complete_task_frame = Frame(self.container)
        
        # Header
        label = Label(self.complete_task_frame, 
                        text="Select the task u have completed :3", 
                        font=("Ink Free", 18))
        label.pack(pady=20)
        
        # Content frame
        f1 =Frame(self.complete_task_frame,
                     width=200,
                     height=300,
                     relief=tk.GROOVE,
                     bg='lightblue')
        f1.pack(padx=10, pady=10)

        self.task_list = Listbox(f1, width=40, font=("Arial", 14),selectmode="multiple")
        self.task_list.pack(pady=20)
        
        # print(self.tasks)
        for index,task in enumerate(self.tasks.keys(),start=1):
            if self.tasks[task]=='False':
                self.task_list.insert('end',f'{task}')
            elif self.tasks[task]=='True':
                self.task_list.insert('end',"✓ " + task)

        remove_btn = Button(f1, text="Mark As Complete",command=self.mark_complete)
        remove_btn.pack(side="left", padx=10)

        back_btn = Button(f1, text="Back", 
                           command=lambda: self.show_frame("main_menu"))
        back_btn.pack(side="right", padx=10)

            

    def mark_complete(self):
        selected = self.task_list.curselection()
        if selected:
            index=selected[0]
            task=self.task_list.get(index)
            try:
                if not self.tasks[task]=='True':
                    self.tasks[task]='True'
                    self.update_listbox()
            except:
                pass

    def update_listbox(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks.keys():
            text=task
            if self.tasks[task]=='True':
                # Add checkmark and strikethrough for completed tasks
                text = "✓ " + text
                self.task_list.insert(tk.END, text)
                self.task_list.itemconfig(tk.END, {'fg': 'gray'})
            else:
                self.task_list.insert(tk.END, text)


    def remove_task(self):
        #deletes tasks
        for i in (self.task_list.curselection()):
            task=self.task_list.get(i)
            self.task_list.delete(i)
            #removes from dictionary
            self.tasks.pop(f'{task}')


    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks[task]='False'
            messagebox.showinfo("Success", "Task added successfully!")
            self.task_entry.delete(0, 'end')
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def show_frame(self, frame_name):
        # Hide all frames
        for frame in [self.main_menu_frame, self.add_task_frame,self.delete_task_frame,self.complete_task_frame]:
            frame.pack_forget()
        
        # Show requested frame
        if frame_name == "main_menu":
            ##loads the tasks from file
            with open('tasklist.txt','w') as f:
                for task in self.tasks.keys():
                    f.write(f'{task}|{self.tasks[task]},')


            self.main_menu_frame.pack(fill="both", expand=True)
            

        elif frame_name == "add_task":
            self.add_task_frame.pack(fill="both", expand=True)
            #focus on entry box
            self.task_entry.focus()

        elif frame_name=='remove_task':
            self.create_delete_task_view()
            self.delete_task_frame.pack(fill='both',expand=True)

        elif frame_name=='complete_task':
            self.create_complete_task_view()
            self.complete_task_frame.pack(fill='both',expand=True)
    

if __name__ == "__main__":
    t1 = ToDoList()
