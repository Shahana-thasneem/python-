import tkinter as tk
root=tk.Tk()
root.title("my first window")
root.geometry("800x800")
text_widget=tk.Text(root,height=5,width=30)
text_widget.pack()
text_widget.insert(tk.END,"type your message here...")
message_widget=tk.Message(root,text="this is a message widget",width=150)
message_widget.pack()

root.mainloop()