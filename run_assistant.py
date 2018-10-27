# Author: Carter Brown, Alyssa Langhals

from Assistant import Assistant

# The disaster assistant
agent = Assistant()

while 1:
    # Get the message
    msg = input()

    if msg == "exit":
        print("Exiting...")
        break

    # Perform action based on message
    agent.decode(msg)