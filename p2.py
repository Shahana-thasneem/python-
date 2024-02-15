import tkinter as tk
root=tk.Tk()
root.title("my first window")
root.geometry("1800x1300")
def button_click():
    print("button clicked")
label=tk.Label(root,text="welcome to tkinder")
button=tk.Button(root,text="click me",command=button_click)
entry=tk.Entry(root)
label.pack()
button.pack()
entry.pack()
root.mainloop()