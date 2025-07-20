import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog, colorchooser
import datetime
import random

class EnhancedTkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Tkinter App")

        # Menu Bar
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)

        self.tools_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Tools", menu=self.tools_menu)
        self.tools_menu.add_command(label="Color Chooser", command=self.choose_color)
        self.tools_menu.add_command(label="Date/Time", command=self.display_datetime)
        self.tools_menu.add_command(label="Random Number", command=self.generate_random_number)

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.show_about)

        # Main Frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Text Area
        self.text_area = tk.Text(self.main_frame, wrap=tk.WORD, width=60, height=20)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Status Bar
        self.status_bar = ttk.Label(root, text="Ready", anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Progress Bar
        self.progress = ttk.Progressbar(self.main_frame, orient=tk.HORIZONTAL, length=200, mode='determinate')
        self.progress.pack(pady=10)

        # Button to start progress bar
        self.progress_button = ttk.Button(self.main_frame, text="Start Progress", command=self.start_progress)
        self.progress_button.pack(pady=5)

        # Combo Box
        self.combo_label = ttk.Label(self.main_frame, text="Select Option:")
        self.combo_label.pack()

        self.combo_options = ["Option 1", "Option 2", "Option 3"]
        self.combo = ttk.Combobox(self.main_frame, values=self.combo_options)
        self.combo.pack()
        self.combo.current(0)

        # Check Buttons
        self.check_var1 = tk.IntVar()
        self.check_var2 = tk.IntVar()

        self.check1 = ttk.Checkbutton(self.main_frame, text="Check 1", variable=self.check_var1)
        self.check1.pack()

        self.check2 = ttk.Checkbutton(self.main_frame, text="Check 2", variable=self.check_var2)
        self.check2.pack()

        # Radio Buttons
        self.radio_var = tk.StringVar()
        self.radio1 = ttk.Radiobutton(self.main_frame, text="Radio 1", variable=self.radio_var, value="Radio 1")
        self.radio1.pack()
        self.radio2 = ttk.Radiobutton(self.main_frame, text="Radio 2", variable=self.radio_var, value="Radio 2")
        self.radio2.pack()
        self.radio_var.set("Radio 1")

        # Spinbox
        self.spin_label = ttk.Label(self.main_frame, text="Enter Value:")
        self.spin_label.pack()
        self.spin = ttk.Spinbox(self.main_frame, from_=0, to=100)
        self.spin.pack()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, file.read())
                    self.status_bar.config(text=f"Opened: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.text_area.get(1.0, tk.END))
                    self.status_bar.config(text=f"Saved: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

    def choose_color(self):
        color = colorchooser.askcolor(title="Select Color")
        if color:
            self.text_area.config(bg=color[1])

    def display_datetime(self):
        now = datetime.datetime.now()
        messagebox.showinfo("Date/Time", now.strftime("%Y-%m-%d %H:%M:%S"))

    def generate_random_number(self):
        num = random.randint(1, 100)
        messagebox.showinfo("Random Number", f"Random number: {num}")

    def show_about(self):
        messagebox.showinfo("About", "Enhanced Tkinter App\nCreated by AI")

    def start_progress(self):
        import time
        for i in range(101):
            time.sleep(0.02)
            self.progress['value'] = i
            self.root.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = EnhancedTkinterApp(root)
    root.mainloop()
