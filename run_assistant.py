# Author: Carter Brown, Alyssa Langhals

from Assistant import Assistant

agent = Assistant()

while 1:
    msg = input()
    if msg == "exit":
        print("Exiting...")
        break

    agent.decode(msg)