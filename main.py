import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('700x700+160+20')
        self.root.maxsize(width=1000, height=1000)
        self.root.title('To-Do List App')
        self.tasks = []
        
        # Create container frame
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)
        
        # Create all frames but don't show them yet
        self.create_main_menu()
        self.create_add_task_view()
        
        # Show the main menu initially
        self.show_frame("main_menu")
        
        self.root.mainloop()
    
    def create_main_menu(self):
        # Main menu frame
        self.main_menu = tk.Frame(self.container)
        
        # Header
        header_label = tk.Label(self.main_menu, 
                              text="To-Do List App", 
                              font=("Courier New", 24, 'bold'))
        header_label.pack(pady=20)
        
        label = tk.Label(self.main_menu, 
                        text="Welcome to your To Do List App\nyou can proceed with ur daily tasks <3", 
                        font=("Ink Free", 18))
        label.pack(pady=20)
        
        # Options frame
        f1 = tk.Frame(self.main_menu,
                     width=200,
                     height=700,
                     relief=tk.GROOVE,
                     bg='lightblue',
                     cursor='hand2')
        f1.pack(padx=10, pady=10)
        
        # Buttons
        option1 = tk.Button(f1, text='Add Task', font=('Arial',12), 
                          width=20, height=3, 
                          command=lambda: self.show_frame("add_task"))
        option1.pack(pady=10, padx=10)
        
        option2 = tk.Button(f1, text='Remove Task', font=('Arial',12), 
                          width=20, height=3)
        option2.pack(pady=10, padx=10)
        
        option3 = tk.Button(f1, text='Complete Task', font=('Arial',12), 
                          width=20, height=3)
        option3.pack(pady=10, padx=10)
    
    def create_add_task_view(self):
        # Add task frame
        self.add_task = tk.Frame(self.container)
        
        # Header
        label = tk.Label(self.add_task, 
                        text="Add Your New Task :3", 
                        font=("Ink Free", 18))
        label.pack(pady=20)
        
        # Content frame
        f1 = tk.Frame(self.add_task,
                     width=200,
                     height=300,
                     relief=tk.GROOVE,
                     bg='lightblue')
        f1.pack(padx=10, pady=10)
        
        # Task entry
        self.task_entry = tk.Entry(f1, width=35, font=("Arial", 14))
        self.task_entry.pack(pady=20)
        
        # Buttons
        add_btn = tk.Button(f1, text="Add Task", command=self.add_task)
        add_btn.pack(side="left", padx=10)
        
        back_btn = tk.Button(f1, text="Back", 
                           command=lambda: self.show_frame("main_menu"))
        back_btn.pack(side="right", padx=10)
    
    def show_frame(self, frame_name):
        # Hide all frames
        for frame in [self.main_menu, self.add_task]:
            frame.pack_forget()
        
        # Show requested frame
        if frame_name == "main_menu":
            self.main_menu.pack(fill="both", expand=True)
        elif frame_name == "add_task":
            self.add_task.pack(fill="both", expand=True)
            self.task_entry.focus()
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            print('done')
            messagebox.showinfo("Success", "Task added successfully!")
            self.task_entry.delete(0, 'end')
            self.show_frame("main_menu")
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

if __name__ == "__main__":
    t1 = ToDoList()
