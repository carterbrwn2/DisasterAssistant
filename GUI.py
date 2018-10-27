from tkinter import *
import tkinter.scrolledtext



class GUI:
    displayed_message = ""
    scrolled_text = None

    def __init__(self):
      self = tkinter.Tk()
      self.title("ACTIVE ALERTS")
      self.wm_iconbitmap('assets/warning_im6_icon.ico')
      self.protocol('WM_DELETE_WINDOW', donothing)
      self.resizable(0,0)

      GUI.scrolled_text = tkinter.scrolledtext.ScrolledText(self)
      GUI.scrolled_text.pack(fill="both", expand=True)
      GUI.scrolled_text.insert(tkinter.INSERT, GUI.displayed_message)


      self.mainloop()

    def update_display(message):
        GUI.displayed_message = message + "\n"
        GUI.scrolled_text.insert(tkinter.INSERT, GUI.displayed_message)

    def new_alert(message):
        #create a new pop-up window
        top = Toplevel()
        top.title("NEW ALERT")
        top.wm_iconbitmap('assets/urgent_icon.ico')
        scrolled_text = tkinter.scrolledtext.ScrolledText(top)
        scrolled_text.pack(fill="both", expand=True)
        scrolled_text.insert(tkinter.INSERT, message)

def create_gui():
    window = GUI()


def donothing():
  pass