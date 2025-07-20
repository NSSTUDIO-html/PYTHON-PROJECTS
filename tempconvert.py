import tkinter as tk

def convert_celsius_to_fahrenheit():
    celsius = float(entry_celsius.get())
    fahrenheit = (celsius * 9/5) + 32
    label_result.config(text=f"{fahrenheit:.2f} °F")

window = tk.Tk()
window.title("Celsius to Fahrenheit Converter")

label_celsius = tk.Label(window, text="Celsius:")
label_celsius.pack()

entry_celsius = tk.Entry(window)
entry_celsius.pack()

button_convert = tk.Button(window, text="Convert", command=convert_celsius_to_fahrenheit)
button_convert.pack()

label_result = tk.Label(window, text="")
label_result.pack()

window.mainloop()
