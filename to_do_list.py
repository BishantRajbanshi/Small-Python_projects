import tkinter as tk
from tkinter import messagebox

class list_of_task:
  def __init__(self):
    self.tasks = []

  def add_tasks(self, task):
    self.tasks.append(task)

  def show_list(self):
    return self.tasks
  
  def delete_task(self,index):
    if 0 <= index < len(self.tasks):
      del self.tasks[index]
    else:
      print("Task not found")

def print_task(list_of_tasks):
  tasks = list_of_task.show_list()
  if tasks:
    print("Tasks list: ")
    for index,task in enumerate(tasks, start=1):
      print(f" {index}. {task}")

def add_task_gui():
  task_text = task_entry.get().strip()
  if task_text:
    task_list.add_task(task_text)
    update_task_list()

def delete_task_gui():
  index = task_listbox.curselection()
  if index:
    task_list.delete_task(index[0])
