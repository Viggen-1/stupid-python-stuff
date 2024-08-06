import tkinter as tk

def close_window(event):
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Click anywhere :)")

# Set the size of the window
root.geometry("300x200")

# Bind any mouse click to the close_window function
root.bind("<Button-1>", close_window)

# Run the application
root.mainloop()
