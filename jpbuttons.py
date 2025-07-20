import tkinter as tk
import tkinter.messagebox

def java_button_click():
    tkinter.messagebox.showinfo("Button Clicked", "Java Button Clicked!")

def python_button_click():
    tkinter.messagebox.showinfo("Button Clicked", "Python Button Clicked!")

root = tk.Tk()
root.title("Button Example")

java_button = tk.Button(root, text="Java Button", command=java_button_click)
java_button.pack(pady=20)

python_button = tk.Button(root, text="Python Button", command=python_button_click)
python_button.pack(pady=50)

root.mainloop()
