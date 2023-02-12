import tkinter as tk

from app import App


def main():
    win = tk.Tk()                           # Create a window
    win.title("Adventure World with GUI")   # Set window title
    win.geometry("650x500")                 # Set window size
    win.resizable(False, False)             # Both x and y dimensions...

    # Create the GUI as a Frame and attach it to the window...
    myApp = App(win)

    # Call the GUI mainloop...
    win.mainloop()

if __name__ == "__main__":
    main()
