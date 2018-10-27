# Author: Carter Brown

class Assistant:

    messages = {
        "tornado-warning":"""A tornado warning means that a tornado has been spotted
or radar indicates the presence of a thunderstorm circulation
that could result in a tornado. Please take immediate action:

*If you are outside, immediately seek shelter in a sturdy building.
                            
*If you are inside, move to an interior room on the lowest floor.
                            
*Avoid windows.
                            
*If no shelter is available, lie down in a low-lying area.
                            
*Protect yourself from flying debris.""",

        "tornado-watch":"""A tornado watch means conditions are favorable for tornadoes 
and severe thunderstorms in and close to the watch area. 

Persons in these areas should be on the lookout for threatening weather conditions

Listen for later statements and possible warnings.""",

        "tsunami-watch":"""An earthquake has occurred that has the potential to generate a tsunami,
this threat to the watch area is still being evaluated.

The watch may be upgraded to an advisory or a warning, or may be cancelled.

*Stay alert for more information.

*Be prepared to act.""",

        "tsunami-advisory": """A tsunami advisory is issued when a tsunami with the 
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
   indicate it is safe to do so.""",

        "tsunami-warning": """A tsunami warning is issued when a tsunami with the potential 
to generate widespread inundation is imminent, expected, or occurring.

URGENT ACTION  SHOULD BE TAKEN TO PROTECT LIVES AND PROPERTY. 

*Move to high ground or inland

*Stay tuned for further information""",
        
        "heatwave":"""""",
        "wildfire":""""""

    }

    flags = {
        "tornado-warning": False
    }

    def __init__(self):
        self.notify("Assistant started")

    def notify(self, msg):
        print(msg)
