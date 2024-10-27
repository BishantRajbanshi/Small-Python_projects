import tkinter as tk
from tkinter import messagebox

class list_of_quest:
  def __init__(self):
    self.quests = []

  def add_quests(self, quest):
    self.quests.append(quest)

  def show_list(self):
    return self.quests
  
  def delete_quest(self,index):
    if 0 <= index < len(self.quests):
      del self.quests[index]
    else:
      print("quest not found")

def print_quest(list_of_quests):
  quests = list_of_quest.show_list()
  if quests:
    print("quests list: ")
    for index,quest in enumerate(quests, start=1):
      print(f" {index}. {quest}")

def add_quest_gui():
    quest_text = quest_entry.get().strip()
    if quest_text:
        quest_list.add_quest(quest_text)
        update_quest_list()
    
def delete_quest_gui():
    index = quest_listbox.curselection()
    if index:
        quest_list.delete_quest(index[0])
        update_quest_list()
    else:
        messagebox.showwarning("warning","please select a quest to delete")

def update_quest_list():
    quest_listbox.delete(0, tk.END) 
    for quest in quest_list.show_list():
        quest_listbox.insert(tk.END ,quest)

quest_list = list_of_quest()

root = tk.Tk()
root.title("To do list app")

quest_entry = tk.Entry(root, width=40)
quest_entry.grid(row=0, column=0, padx=50, pady=10)

add_button = tk.Button(root, text="Add quest", command=add_quest_gui)
add_button.grid(row=0, column=1, padx=10, pady=20)

quest_listbox = tk.Listbox(root, width=50)
quest_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete quest", command=delete_quest_gui)
delete_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)  
root.update()
# to center the window
root_width = root.winfo_width()
root_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (root_width / 2))
y = int((screen_height / 2) - (root_height / 2))

root.geometry(f"{root_width}x{root_height}+{x}+{y-35}")

root.mainloop()
    
