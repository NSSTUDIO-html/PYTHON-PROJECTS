import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

def create_gradient_image(width, height, start_color, end_color, direction='horizontal'):
    """Creates a gradient image using PIL.

    Args:
        width: The width of the image.
        height: The height of the image.
        start_color: The starting color (tuple of RGB values, e.g., (255, 0, 0) for red).
        end_color: The ending color (tuple of RGB values).
        direction: 'horizontal' or 'vertical' gradient.
    Returns:
        A PIL ImageTk.PhotoImage object.
    """
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    r1, g1, b1 = start_color
    r2, g2, b2 = end_color

    if direction == 'horizontal':
        for x in range(width):
            r = int(r1 + (r2 - r1) * x / width)
            g = int(g1 + (g2 - g1) * x / width)
            b = int(b1 + (b2 - b1) * x / width)
            draw.line((x, 0, x, height), fill=(r, g, b))
    elif direction == 'vertical':
        for y in range(height):
            r = int(r1 + (r2 - r1) * y / height)
            g = int(g1 + (g2 - g1) * y / height)
            b = int(b1 + (b2 - b1) * y / height)
            draw.line((0, y, width, y), fill=(r, g, b))

    return ImageTk.PhotoImage(image)

def create_gradient_button(window, width, height, start_color, end_color, text, direction='horizontal'):
  """Creates a button with a gradient background.

  Args:
    window: The Tkinter window.
    width: Button width.
    height: Button height.
    start_color: Gradient start color (RGB tuple).
    end_color: Gradient end color (RGB tuple).
    text: Button text.
    direction: 'horizontal' or 'vertical'.
  """
  gradient_image = create_gradient_image(width, height, start_color, end_color, direction)
  button = tk.Button(window, image=gradient_image, text=text, compound="center")
  button.image = gradient_image #keep a reference!
  button.pack()

# Example usage:
root = tk.Tk()
root.title("Gradient Button Example")

create_gradient_button(root, 200, 50, (255, 0, 0), (0, 0, 255), "Red to Blue", 'horizontal')
create_gradient_button(root, 300, 100, (0, 255, 0), (255, 255, 0), "Green to Yellow", 'vertical')

root.mainloop()
