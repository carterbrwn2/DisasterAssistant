# Author: Carter Brown, Alyssa Langhals

from Assistant import Assistant
from threading import Thread
import GUI

def main():
  agent = Assistant()

  while 1:
      msg = input()
      if msg == "exit":

         print("Exiting...")
         break
      else:
          GUI.GUI.update_Display(msg + "\n")
      #agent.decode(msg)


threadGUI = Thread(target = GUI.create_GUI)
threadMain = Thread(target = main)
threadMain.start()
threadGUI.start()

threadMain.join()
print("ClosingMAIN")
threadGUI.join()
print("ClosingGUI")

