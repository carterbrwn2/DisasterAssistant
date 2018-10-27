# Author: Carter Brown, Alyssa Langhals

from Assistant import Assistant
from threading import Thread
from time import sleep
import GUI


def main():
    # The disaster assistant
    sleep(1)
    agent = Assistant(GUI)

    while 1:
        # Get the message
        msg = input()
        if msg == "exit":
            print("Exiting...")
            break
        # Perform action based on message
        agent.decode(msg)

    agent.assistant_exit()


thread_main = Thread(target=main)
thread_main.start()

GUI.create_gui()
