import tkinter as tk
import json

root = tk.Tk()
root.geometry("600x400")

def save_to_file():
    global task_colors
    with open('todo.json', 'w') as file:
        json.dump(task_colors, file)
def load_from_file():
    global task_colors
    try:
        with open('todo.json', 'r') as file:
            task_colors = json.load(file)
    except:
        task_colors = {}

todolist = []

task_colors = {}
load_from_file()

def getEntry():
    todo = entryToDo.get().strip()

    if todo:
        if todo not in task_colors:
            task_colors[todo] = 'black'
        entryToDo.delete(0, tk.END)
        update()

def delete(task):
    if task in task_colors:
        del task_colors[task]
        save_to_file()
    update()    

    
def change_color(button, task):
    if button.cget('fg') == 'black':
        button.config(fg='red')
    elif button.cget('fg') == 'red':
        button.config(fg='green')
    elif button.cget('fg') == 'green':  
        button.config(fg='black')
    task_colors[task] = button.cget('fg')
    save_to_file()

def update():
    for widget in button_frame.winfo_children():
        widget.destroy()
    for widget in change_color_frame.winfo_children():
        widget.destroy()
    for widget in delete_frame.winfo_children():
        widget.destroy()

    for task, color in task_colors.items():
        button = tk.Button(button_frame, text=task, fg=color)
        button.pack(anchor='w', padx=20)

        change_color_button = tk.Button(change_color_frame, text='Change State')
        change_color_button.pack(anchor='e')
        change_color_button.config(command=lambda btn=button, t=task: change_color(btn,t))

        delete_button = tk.Button(delete_frame, text='Remove Task')
        delete_button.pack(anchor='e', padx=20)
        delete_button.config(command=lambda t=task: delete(t))

    save_to_file()

entryToDo = tk.Entry(root)
entryToDo.pack()

entryButton = tk.Button(root, text="Add To-Do", command=getEntry)
entryButton.pack()

button_frame = tk.Frame(root, width=300)  # Limit width
button_frame.pack(side='left', fill='y', padx=10, pady=10)

delete_frame = tk.Frame(root)
delete_frame.pack(side='right', fill='y', padx=10, pady=10)

change_color_frame = tk.Frame(root)
change_color_frame.pack(side='right', fill='y', padx=10, pady=10)

update()
root.mainloop()
