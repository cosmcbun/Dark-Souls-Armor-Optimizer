import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from customtkinter import CTkImage


# Function to be called when the button is clicked
def button_clicked():
    quit()

# Function to resize the image while maintaining aspect ratio
def resize_image(event):
    # Minimum size the window can be resized to
    min_width = 200
    min_height = int(min_width / original_aspect_ratio)

    # Ensure the window doesn't go below a minimum size
    if event.width < min_width or event.height < min_height:
        app.geometry(f"{min_width}x{min_height}")
        return

    # Calculate new dimensions based on the aspect ratio
    new_width = max(event.width, min_width)
    new_height = int(new_width / original_aspect_ratio)

    # Adjust the window size to maintain the aspect ratio
    app.geometry(f"{new_width}x{new_height}")

    # Resize and update the image
    resized_image = background_image.resize((new_width, new_height), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized_image)
    image_label.configure(image=photo)
    image_label.image = photo

def max_window_size(aspect_ratio):
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    if screen_width / screen_height > aspect_ratio:
        return round(screen_height * aspect_ratio), screen_height
    else:
        return screen_width, round(screen_width / aspect_ratio)

# Create the main window
app = ctk.CTk()
app.title("Dark Souls Armor Calculator")
app.resizable(False, False)

# Load the image
background_image = Image.open("DS inventory example.jpeg") # Replace with your image path
original_aspect_ratio = background_image.width / background_image.height
window_width, window_height = max_window_size(original_aspect_ratio)
app.geometry(f"{window_width}x{window_height}")  # Initial size of the window
photo = CTkImage(background_image, size=(window_width, window_height))

# Create a label to display the image
image_label = ctk.CTkLabel(app, image=photo)
image_label.image = photo  # Keep a reference to avoid garbage collection
image_label.place(x=0, y=0, relwidth=1, relheight=1)  # Stretch to fill the window

# Bind the resize event to the resize_image function
#app.bind("<Configure>", resize_image)


# Create a button
button = ctk.CTkButton(app, text="Quit", command=quit)
button.place(relx=0.25, rely=0.5, anchor=tk.CENTER)  # Position the button at the center

app.mainloop()
