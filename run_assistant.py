# Author: Carter Brown, Alyssa Langhals

from Assistant import Assistant
from GUI import GUI
from threading import Thread

window = GUI()


def main():
    global window

    # The disaster assistant
    agent = Assistant(window)

    while 1:
        # Get the message
        msg = input()
        if msg == "exit":
            print("Exiting...")
            break
        # Perform action based on message
        agent.decode(msg)

    agent.assistant_exit()
    window.close_window()


# Start running main before window
thread_main = Thread(target=main)
thread_main.start()

# Open window
window.open_window()
