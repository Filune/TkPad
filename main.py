import sys
import os
from tkinter import PhotoImage, Tk
from tkpad import TkPad


def launch():
    """Launches the TkPad application."""
    script_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    icon_path = os.path.join(script_dir, 'images/tkpad_icon.png')

    root = Tk()
    root.title("TkPad")
    root.geometry("800x500")
    photo = PhotoImage(file=icon_path)
    root.iconphoto(False, photo)

    center_window(root)
    TkPad(root)
    root.mainloop()


def center_window(window):
    """Centers the given window on the screen.

    Args:
        window (Tk): The window to be centered.
    """
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.update()


if __name__ == "__main__":
    launch()