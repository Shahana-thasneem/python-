import tkinter as tk
root=tk.Tk()
root.title("my first window")
root.geometry("600x800")
canvas=tk.Canvas(root,width=200,height=200)
canvas.pack()
scrollbar=tk.Scrollbar(root,orient="vertical",command=canvas.yview)
scrollbar.pack(side="right",fill="y")
canvas.cofigure(yscrollcommand=scrollbar.set)
frame=tk.Frame(canvas)
canvas.create_window((0,0),window=frame,anchor="nw")
for i in range(20):
    label=tk.Label(frame,text=f"Label {i}")
    label.pack()
canvas.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))

root.mainloop()