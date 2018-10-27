# Author: Carter Brown

class Assistant:

    messages = {
        "tornado-warning":"""A tornado warning means that a tornado has been spotted
or radar indicates the presence of a thunderstorm circulation
that could result in a tornado. Please take immediate action:

If you are outside, immediately seek shelter in a sturdy building.
                            
If you are inside, move to an interior room on the lowest floor.
                            
Avoid windows.
                            
If no shelter is available, lie down in a low-lying area.
                            
Protect yourself from flying debris."""
    }

    flags = {
        "tornado-warning": False
    }

    msg_history = []

    def __init__(self):
        self.notify("Assistant started")

    def notify(self, msg, msg_key=None):
        if msg_key is None:
            print(msg)
        else:
            print(self.messages[msg_key])

    def decode(self, msg):
        msg_arr = msg.split("&&")
        command, arg, value = msg_arr[0:3]
        if command == "notify":
            self.notify(None, arg)
        elif command == "setflag":
            self.flags[arg] = value
        else:
            self.notify(command, None)


