# gui_calculator.py

import tkinter as tk
import tkinter.font as font

# Global variable to hold the expression string
expression = ""

# --- Functions to handle button presses ---

def update_display(value):
  """Updates the text in the display Entry widget."""
  # Clear the current content
  display_entry.delete(0, tk.END)
  # Insert the new value
  display_entry.insert(0, str(value))

def press_key(key):
  """Appends the pressed key (number or operator) to the expression."""
  global expression
  expression += str(key)
  update_display(expression)

def press_equal():
  """Calculates the expression shown in the display."""
  global expression
  try:
    # IMPORTANT WARNING:
    # Using eval() can be a security risk if the input is not
    # strictly controlled, as it can execute arbitrary code.
    # In this specific calculator case, since input comes ONLY
    # from button clicks we defined, the risk is lower, but
    # it's crucial to be aware of this danger in other contexts.
    # For more complex or robust applications, parse the expression
    # manually or use safer evaluation libraries.
    total = str(eval(expression))
    update_display(total)
    # Store the result so the user can start a new calculation with it
    expression = total
  except ZeroDivisionError:
    update_display("Error: Div by 0")
    expression = "" # Reset expression
  except Exception as e:
    # Catch other errors like SyntaxError (e.g., "1++2")
    update_display("Error")
    expression = "" # Reset expression
    print(f"Evaluation error: {e}") # Optional: print error to console

def press_clear():
  """Clears the display and the expression."""
  global expression
  expression = ""
  update_display("")

# --- Set up the main window ---
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("320x420") # Adjusted size for better fit
window.resizable(False, False) # Make window not resizable

# Define font for display and buttons
display_font = font.Font(family='Arial', size=24)
button_font = font.Font(family='Arial', size=18)

# --- Create the display widget (Entry) ---
display_entry = tk.Entry(
    window,
    font=display_font,
    textvariable=tk.StringVar(), # Not strictly needed here as we use update_display
    bd=10,        # Border width
    insertwidth=2, # Cursor width
    width=14,      # Width in characters
    borderwidth=4,
    justify='right' # Right-align text
)
# Place the display at the top, spanning all 4 columns
display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=10) # Added padding

# --- Create and place the buttons ---
# Define the button layout in a list of lists (rows)
button_layout = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['AC', '0', '.', '+']
]

# Create number and operator buttons using a loop
row_num = 1
for row in button_layout:
  col_num = 0
  for button_text in row:
    # Use lambda to pass the button_text to the press_key function
    # Special case for the 'C' button
    if button_text == 'AC':
      action = press_clear
    else:
      action = lambda x=button_text: press_key(x)

    button = tk.Button(
        window,
        text=button_text,
        font=button_font,
        fg="black",          # Text color
        width=4,             # Button width
        height=1,            # Button height
        bd=4,                # Button border width
        command=action
    )
    button.grid(row=row_num, column=col_num, padx=5, pady=5, sticky="nsew") # Added padding and sticky
    col_num += 1
  row_num += 1

# Create the '=' button separately, spanning columns
equal_button = tk.Button(
    window,
    text='=',
    font=button_font,
    fg="black",
    width=19, # Span width
    height=1,
    bd=4,
    command=press_equal
)
equal_button.grid(row=row_num, column=0, columnspan=4, padx=5, pady=10, sticky="nsew") # Added padding and sticky

# Configure grid row/column weights so buttons resize nicely if window were resizable
# (though we disabled resizing)
for i in range(5): # 5 rows including equals button
    window.grid_rowconfigure(i, weight=1)
for i in range(4): # 4 columns
    window.grid_columnconfigure(i, weight=1)

# --- Start the Tkinter event loop ---
window.mainloop()
