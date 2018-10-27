# Author: Carter Brown, Alyssa Langhals

from threading import *


class Assistant:

    # ------------------------------------------------------------------------------
    # CLASS OBJECT ATTRIBUTES
    # ------------------------------------------------------------------------------

    #
    # DICTIONARY OF STATUS MESSAGES
    #

    messages = {
        "tornado-warning": (
                """
A tornado warning means that a tornado has been spotted
or radar indicates the presence of a thunderstorm circulation
that could result in a tornado. Please take immediate action:

    *If you are outside, immediately seek shelter in a sturdy building.

    *If you are inside, move to an interior room on the lowest floor.

    *Avoid windows.

    *If no shelter is available, lie down in a low-lying area.

    *Protect yourself from flying debris.
""",
                "\nThe tornado warning is no longer in effect.\n"),


        "tornado-watch": (
            """
A tornado watch means conditions are favorable for tornadoes 
and severe thunderstorms in and close to the watch area. 

Persons in these areas should be on the lookout for threatening weather conditions

Listen for later statements and possible warnings.
""",
            "\nThe tornado watch is no longer in effect.\n"),


        "tsunami-watch": (
            """
An earthquake has occurred that has the potential to generate a tsunami,
this threat to the watch area is still being evaluated.

The watch may be upgraded to an advisory or a warning, or may be cancelled.

    *Stay alert for more information.

    *Be prepared to act.
""",
            "\nThe tsunami watch is no longer in effect.\n"),


        "tsunami-advisory": (
            """
A tsunami advisory is issued when a tsunami with the 
potential to generate strong currents or waves dangerous to those 
in or very near the water is imminent, expected, or occurring.

An advisory may be upgraded to a warning or cancelled.

The tsunami may appear as water moving rapidly out to sea,
a gentle rising tide like flood with no breaking wave,
as a series of breaking waves, or a frothy wall of water.

If you are in a tsunami advisory area:

     * Move out of the water, off the beach, and away from
       harbors, marinas, breakwaters, bays and inlets.

     * Be alert to and follow instructions from your local
       emergency officials because they may have more detailed or
       specific information for your location.

     * If you feel a strong earthquake or extended ground rolling
       take immediate protective actions such as moving inland
       and/or uphill preferably by foot.

     * Do not go to the shore to observe the tsunami.

     * Do not return to the coast until local emergency officials
       indicate it is safe to do so.
""",
            "\nThe tsunami advisory is no longer in effect\n"),


        "tsunami-warning": (
            """
A tsunami warning is issued when a tsunami with the potential 
to generate widespread inundation is imminent, expected, or occurring.

URGENT ACTION  SHOULD BE TAKEN TO PROTECT LIVES AND PROPERTY. 

*Move to high ground or inland

*Stay tuned for further information
""",
            "\nThe tsunami warning is no longer in effect\n"),


        "heatwave": (
            """""",
            ""),


        "wildfire": (
            """""",
            "")

    }

    #
    # DICTIONARY OF STATUS FLAGS
    #

    flags = {
        "tornado-warning": False,
        "tornado-watch": False,
        "tsunami-watch": False,
        "tsunami-advisory": False,
        "tsunami-warning": False,
        "heatwave": False,
        "wildfire": False
    }

    #
    # MESSAGE HISTORY
    #

    msg_history = []

    # ------------------------------------------------------------------------------
    # CLASS METHODS
    # ------------------------------------------------------------------------------

    def __init__(self):
        """Constructor for Assistant

        Starts the client updater

        """

        self.send_message("Assistant started")

        # Start the auto updater
        self.update_flag = True
        self.stop_ev = Event()
        self.update_thread = Thread(target=self.update_client_on_status)
        self.update_thread.start()

    def decode(self, msg):
        """
        Decodes the incoming message to take action on client

        :param msg: String - Message from the console
            In the format: <command>&&<arguments>&&<value>
            Possible commands: notify, send
        :return: None
        """

        # Add console message to log
        self.update_history(msg)

        # Parse message
        msg_arr = msg.split("&&")
        command, arg, value = msg_arr[0:3]

        # Perform action based on message
        if command == "notify":
            # Set disaster flag
            self.flags[arg] = self.convert_value(value)
            # Notify client of new information
            self.notify(arg)
        elif command == "send":
            # Send message to client
            self.send_message(arg)

    def notify(self, msg_key):
        """
        Notifies the user of an incoming message

        :param msg_key: String - The key to the messages dictionary
        :return: None
        """

        # Determine what message to send
        index = 0 if self.flags[msg_key] else 1

        self.update_client_window(self.messages[msg_key][index])

    def send_message(self, msg):
        """
        Send a text message to the client

        :param msg: String - The message to send to the client
        :return: None
        """
        self.update_client_window(msg)

    def update_client_window(self, msg):
        """
        Updates the client window

        :param msg: String - The string to send to the client window
        :return: None
        """
        print(msg)

    def update_history(self, msg):
        """
        Updates the console log

        :param msg: Message from the console
        :return: None
        """
        self.msg_history.append(msg)

    def update_client_on_status(self):
        """
        Periodically (10 min) updates the client on the current status of advisories/warnings

        :return: None
        """
        while self.update_flag:
            for label, flag in self.flags.items():
                if flag:
                    self.send_message(self.messages[label][0])
            self.stop_ev.wait(15)
        print("Done")

    def assistant_exit(self):
        """
        Unsets the update_flag, terminating the update loop

        :return: None
        """
        self.update_flag = False
        self.stop_ev.set()

    def convert_value(self, value):
        """
        Converts passed String to a bool

        :param value: String to convert to a bool
        :return: True or False based on value
        """
        s = value.lower()
        if s == "true":
            return True
        elif s == "false":
            return False
        else:
            print("Error: invalid value argument")
            return False
