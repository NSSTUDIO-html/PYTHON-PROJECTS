import tkinter as tk

def create_gradient_button(parent, text, from_color, to_color, command=None, **kwargs):
    """Creates a gradient button in Tkinter."""

    button = tk.Canvas(parent, width=100, height=30, bd=0, highlightthickness=0, **kwargs)

    # Validate color inputs
    try:
        r1, g1, b1 = parent.winfo_rgb(from_color)
        r2, g2, b2 = parent.winfo_rgb(to_color)
    except tk.TclError:
        print(f"Error: Invalid color name '{from_color}' or '{to_color}'. Using default colors.")
        r1, g1, b1 = parent.winfo_rgb("blue")  # Default to blue if invalid
        r2, g2, b2 = parent.winfo_rgb("purple") # Default to purple if invalid

    for i in range(button.winfo_reqheight()):
        r = int(r1 + (r2 - r1) * i / button.winfo_reqheight())
        g = int(g1 + (g2 - g1) * i / button.winfo_reqheight())
        b = int(b1 + (b2 - b1) * i / button.winfo_reqheight())
        hex_color = f'#{r:02x}{g:02x}{b:02x}'
        button.create_line(0, i, button.winfo_reqwidth(), i, fill=hex_color)

    button.create_text(button.winfo_reqwidth() / 2, button.winfo_reqheight() / 2, text=text, fill='white', font=('Arial', 12, 'bold'))

    if command:
        button.bind("<Button-1>", lambda event: command())

    return button

def main():
    root = tk.Tk()
    root.title("Gradient Button Example")

    def button_click():
        print("Button Clicked!")

    # Use valid color names - IMPORTANT!
    gradient_button = create_gradient_button(root, "Click Me", "white", "purple", command=button_click)
    gradient_button.pack(pady=20)

    gradient_button2 = create_gradient_button(root, "Another", "green", "yellow", command=lambda: print("Another button"))
    gradient_button2.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
