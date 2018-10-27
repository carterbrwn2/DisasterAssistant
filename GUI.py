import tkinter
import tkinter.scrolledtext


class GUI:
    displayed_message = ""

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.title("ACTIVE ALERTS")
        self.root.wm_iconbitmap('assets/warning_im6_icon.ico')
        self.root.scrolledtext = tkinter.scrolledtext.ScrolledText(self.root)
        self.root.scrolledtext.pack(fill="both", expand=True)

    def update_display(self, message):
        self.displayed_message = message + "\n"
        self.root.scrolledtext.insert("0.0", self.displayed_message)

    def open_window(self):
        self.root.mainloop()

    def close_window(self):
        self.root.quit()
