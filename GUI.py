import tkinter
import tkinter.scrolledtext
import time



class GUI:
  displayedMessage = ""
  scrolledtext = None

  def __init__(self):
    self = tkinter.Tk()
    self.title("ACTIVE ALERTS")
    self.wm_iconbitmap('assets/warning_im6_icon.ico')
    # <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Warning">Warning</a> from <a href="https://www.flaticon.com/"     title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/"     title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
    #self.geometry("%dx%d+0+0" % self.maxsize())

    GUI.scrolledtext = tkinter.scrolledtext.ScrolledText(self)
    GUI.scrolledtext.pack(fill="both", expand=True)
    GUI.displayedMessage = "No current alerts"
    GUI.scrolledtext.insert(tkinter.INSERT, GUI.displayedMessage)

    self.mainloop()

  def update_Display(message):
    GUI.displayedMessage = time.ctime() + "\n" + message
    GUI.scrolledtext.insert(tkinter.INSERT, GUI.displayedMessage)




def create_GUI():
    window = GUI()









