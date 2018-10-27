import tkinter
import tkinter.scrolledtext


class GUI:
    displayed_message = ""
    scrolledtext = None

    def __init__(self):
      self = tkinter.Tk()
      self.title("ACTIVE ALERTS")
      self.wm_iconbitmap('assets/warning_im6_icon.ico')

      GUI.scrolledtext = tkinter.scrolledtext.ScrolledText(self)
      GUI.scrolledtext.pack(fill="both", expand=True)
      GUI.scrolledtext.insert(tkinter.INSERT, GUI.displayed_message)

      self.mainloop()

    def update_display(message):
        GUI.displayed_message = message + "\n"
        GUI.scrolledtext.insert(tkinter.INSERT, GUI.displayed_message)


def create_gui():
    window = GUI()
