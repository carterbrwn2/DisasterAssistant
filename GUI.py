# Author: Carter Brown, Alyssa Langhals

import tkinter
import tkinter.scrolledtext


class GUI:
    displayed_message = ""

    def __init__(self):
        """
        Constructor for GUI

        Initializes tkinter window

        """
        self.root = tkinter.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.title("ACTIVE ALERTS")
        self.root.wm_iconbitmap('assets/warning_im6_icon.ico')
        self.root.scrolledtext = tkinter.scrolledtext.ScrolledText(self.root)
        self.root.scrolledtext.pack(fill="both", expand=True)
        self.root.protocol('WM_DELETE_WINDOW', donothing)
        self.root.resizable(0, 0)

    def update_display(self, message):
        """
        Updates the display with a received message

        :param message: The message to display
        :return: None
        """
        self.displayed_message = message + "\n"
        self.root.scrolledtext.insert("0.0", self.displayed_message)

    def open_window(self):
        """
        Opens the tkinter window

        :return: None
        """
        self.root.mainloop()

    def close_window(self):
        """
        Closes the tkinter window

        :return: None
        """
        self.root.quit()

    def new_alert(self, message):
        # Create a new pop-up window
        top = tkinter.Toplevel()
        top.title("NEW ALERT")
        top.wm_iconbitmap('assets/urgent_icon.ico')
        scrolled_text = tkinter.scrolledtext.ScrolledText(top)
        scrolled_text.pack(fill="both", expand=True)
        scrolled_text.insert(tkinter.INSERT, message)


def donothing():
    pass
