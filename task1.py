class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task.description} (Due: {task.due_date}) - Status: {task.status}")

    def mark_complete(self, task_index):
        self.tasks[task_index - 1].status = "Complete"


def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Complete")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            new_task = Task(description, due_date)
            todo_list.add_task(new_task)

        elif choice == "2":
            todo_list.display_tasks()

        elif choice == "3":
            try:
                index = int(input("Enter task index to mark as complete: "))
                todo_list.mark_complete(index)
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        self.tasks = []

        self.label = tk.Label(master, text="To-Do List")
        self.label.pack()

        self.task_entry = tk.Entry(master)
        self.task_entry.pack()

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.listbox = tk.Listbox(master)
        self.listbox.pack()

        self.complete_button = tk.Button(master, text="Mark as Complete", command=self.mark_complete)
        self.complete_button.pack()

    def add_task(self):
        task_description = self.task_entry.get()
        if task_description:
            self.tasks.append(task_description)
            self.listbox.insert(tk.END, task_description)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task description cannot be empty.")

    def mark_complete(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.itemconfig(selected_index, {'bg': 'green'})
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
