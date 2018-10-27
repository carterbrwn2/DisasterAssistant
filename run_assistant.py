# Author: Carter Brown, Alyssa Langhals

from Assistant import Assistant
from threading import Thread
import GUI

def main():
    # The disaster assistant
  sagent = Assistant()

  while 1:
      #Get the message
      msg = input()
      if msg == "exit":
          print("Exiting...")
          break
      else:
          GUI.GUI.update_Display(msg + "\n")
    # Perform action based on message
      agent.decode(msg)

  agent.assistant_exit()

#start threads
threadGUI = Thread(target = GUI.create_GUI)
threadMain = Thread(target = main)
threadMain.start()
threadGUI.start()

threadMain.join()
print("ClosingMAIN")
threadGUI.join()
print("ClosingGUI")
