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


