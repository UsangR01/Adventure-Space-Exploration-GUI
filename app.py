import tkinter as tk
from Game import Game
from tkinter import BOTH, Y
from PIL import ImageTk, Image
import traceback
from tkinter import messagebox
import settings
import logs
import time

import warnings
warnings.filterwarnings('ignore')

class App():

    # Creates a Frame for the application and populates the GUI...
    def __init__(self, root):

        self.game = Game()
        # logs.log()

        # Create two frames owned by the window root.
        # In order to use multiple layout managers, the frames
        # cannot share a parent frame. Here both frames are owned
        # by a top level instance root.

        self.frame1 = tk.Frame(root, width=650, height=70, bg='LAVENDER', borderwidth=4)
        self.frame1.pack_propagate(0)  # Prevents resizing

        self.frame2 = tk.Frame(root, width=650, height=300, bg='WHITE', borderwidth=7)
        self.frame2.pack_propagate(0)  # Prevents resizing

        self.frame3 = tk.Frame(root, width=150, height=150, bg='LIGHT GREY', borderwidth=30)
        self.frame3.pack_propagate(0)  # Prevents resizing

        self.frame4 = tk.Frame(root, width=350, height=150, bg='LAVENDER', borderwidth=7)
        self.frame4.pack_propagate(0)  # Prevents resizing

        self.frame5 = tk.Frame(root, width=150, height=150, bg='LIGHT GREY', borderwidth=35)
        self.frame5.pack_propagate(0)  # Prevents resizing

        # This packs the frames into the root window...
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack(side="left", fill=Y)
        self.frame4.pack(side="left", expand=True, fill=BOTH)
        self.frame5.pack(side="right", expand=True, fill=BOTH)

        self.img = ImageTk.PhotoImage(Image.open('images/Negotiator.jpg').resize((650,300), Image.ANTIALIAS))
        self.background = tk.Label(self.frame2, image=self.img)
        self.background.pack(expand=True, fill=BOTH)

        # Now add some useful widgets...
        self.text_area1 = tk.Label(self.frame1, bg="white", fg="black", text='', font=("lucida console", 7))
        self.text_area1.pack(expand=True, fill=BOTH)

        self.text_area2 = tk.Label(self.frame4, bg="white", fg="black", text='', font=("lucida console", 7))
        self.text_area2.pack(expand=True, fill=BOTH)

        # self.text_area3 = tk.Label(self.frame5, width=13, bg="green", borderwidth=0)
        # self.text_area3.grid(row=3, columnspan=3)
        #
        # self.text_area4 = tk.Label(self.frame5, width=13, bg="yellow", borderwidth=0, text='')
        # self.text_area4.grid(row=4, columnspan=3)

        self.build_GUI()

    def build_GUI(self):
        # self.cmd_button = tk.Button(self.frame2, text='Run command', fg='black', bg='blue', command=self.do_command)
        # self.cmd_button.pack()

        self.text_area1.configure(text=self.game.print_welcome())


        # Build some direction control buttons
        self.North_button = tk.Button(self.frame5,text="🢁", bg="ivory4", borderwidth=0, command=lambda: self.process_command('Go north')).grid(row=0, column=1, pady=0, padx=0,sticky="nsew")
        self.South_button = tk.Button(self.frame5,text="🢃", bg="ivory4", borderwidth=0, command=lambda: self.process_command('Go south')).grid(row=2, column=1, pady=0, padx=0,sticky="nsew")
        self.East_button = tk.Button(self.frame5,text="🢂🢂", bg="ivory4", borderwidth=0, command=lambda: self.process_command('Go east')).grid(row=1, column=2, pady=0, padx=0,sticky="nsew")
        self.West_button = tk.Button(self.frame5,text="🢀🢀", bg="ivory4", borderwidth=0, command=lambda: self.process_command('Go west')).grid(row=1, column=0, pady=0, padx=0,sticky="nsew")

        # Build some command control buttons into frame 4...
        self.Quit = tk.Button(self.frame4, text="Quit", bg="black", fg="white", font=("Arial", 8, "bold"), borderwidth=0, command=lambda: self.frame4.quit).pack(padx=0, pady=0, side='left', expand=True) #, fill='x')
        self.Help = tk.Button(self.frame4, text="Help", bg="black", fg="white", font=("Arial", 8, "bold"), borderwidth=0, command=lambda: self.process_command('help')).pack(padx=0, pady=0, side='left', expand=True) #, fill='x')

        # Build some command control buttons into frame 3...
        self.Use = tk.Button(self.frame3, text="Use", bg="ivory4", fg="black", font=("Arial", 8, "bold"), borderwidth=0, command=lambda: self.process_command(f'use {self.game.negotiator.checkNegotiator_Bag()}')).grid(row=0, column=1, pady=0, padx=0, sticky="nsew")
        self.Drop = tk.Button(self.frame3, text="Drop", bg="ivory4", fg="black", font=("Arial", 8, "bold"), borderwidth=0, command=lambda: self.process_command(f'drop {self.game.negotiator.checkNegotiator_Bag()}')).grid(row=1, column=0, pady=0, padx=0, sticky="nsew")
        self.Pick = tk.Button(self.frame3, text="Pick", bg="ivory4", fg="black", font=("Arial", 8, "bold"), borderwidth=0, command=lambda: self.process_command(f'pick {self.game.current_location.checkLocation_inventory()}')).grid(row=1, column=2, pady=0, padx=0, sticky="nsew")
        self.Dock = tk.Button(self.frame3, text="Dock", bg="ivory4", fg="black", font=("Arial", 8, "bold"), borderwidth=0, command=lambda: self.process_command('dock')).grid(row=2, column=1, pady=0, padx=0, sticky="nsew")

    def get_command_string(self, input_line):
        """
            Fetches a command (borrowed from old TextUI).
        :return: a 2-tuple of the form (command_word, second_word)
        """
        word1 = None
        word2 = None
        if input_line != "":
            all_words = input_line.split()
            word1 = all_words[0]
            if len(all_words) > 1:
                word2 = all_words[1]
            else:
                word2 = None
            # Just ignore any other words
        return (word1, word2)

    def process_command(self, command):
        """
            Process a command.
        :param command: a 2-tuple of the form (command_word, second_word)
        """
        command_word, second_word = self.get_command_string(command)
        if command_word != None:
            command_word = command_word.upper()

            want_to_quit = False
            if command_word == "QUIT":
                want_to_quit = True
            elif command_word == "HELP":
                self.text_area1.configure(text=self.game.print_help())
            elif command_word == "DOCK":
                self.text_area1.configure(text=self.game.current_location.get_long_description())
                self.text_area2.configure(text=self.game.negotiator.showHealth())
            elif command_word == "GO":
                self.change_background(second_word)
                self.text_area1.configure(text=self.game.do_go_command(second_word))
                self.text_area2.configure(text=self.game.negotiator.show_negotiator_inv())
            elif command_word == "PICK":
                self.text_area2.configure(text=self.game.pickup(second_word))
            elif command_word == "USE":
                self.text_area1.configure(text=self.game.use_up(second_word))
            else:
                # Unknown command...
                self.text_area1.configure(text="Don't know what you mean.")

            return want_to_quit

    def report_callback_exception(self, *args):
        try:
            err = traceback.format_exception(*args)
            if settings.log_cli:
                traceback.print_exc()
            messagebox.showerror('App error', f'An exception occurred - {err[-1]}\nStack trace:\n{str(err)}')
        except Exception as e:
            print("Error while handling exception: " + str(e))
            print(traceback.format_exc())
            messagebox.showerror('Fatal error', f'A fatal error has occurred. Check the logs for more details')

    def change_background(self, second_word):
        next_location = self.game.current_location.get_exit(second_word)
        if next_location == None:
            return
        if second_word == None:
            return
        else:
            self.img = ImageTk.PhotoImage(Image.open(f"{next_location.image_path}").resize((650, 300), Image.ANTIALIAS))
            self.background.configure(image=self.img)