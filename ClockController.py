from Displays import LCDDisplay
from Button import *
from Clock import *

class ClockController:
    """ Our implementation of the Clock Controller
        4 buttons for setting month, date, hour, min
        LCD display to show the time
    """

    def __init__(self):
        self._clock = Clock()
        self._display = LCDDisplay(sda=0, scl=1, i2cid=0)
        self._buttons = [Button(10, 'white', buttonhandler=self),
                            Button(11, 'red', buttonhandler=self),
                            Button(12, 'yellow', buttonhandler=self),
                            Button(13, 'blue', buttonhandler=self)]
    def showTime(self):
        """" Show the time on the display """

        (year, month, date, hour, minute, sec, wd, yd) = self._clock.getTime()
        self._display.showText(f'{year:}/{month:}/{date:}   {wd:}:{yd:} \n{hour:}:{minute:}:{sec:} ')

    
    def buttonPressed(self, name):
       
        if name == 'white':
            # get the current month
            month = self._clock.getMonth()
            # set the month to 1 + the current month
            self._clock.setMonth(month + 1)

        if name == 'red':
            # get the current date
            date = self._clock.getDate()
            # set the date to 1 + the current date
            self._clock.setDate(date + 1)
        
        if name == 'yellow':
            # get the current hour
            hour = self._clock.getHour()
            # set the hour to 1 + the current hour
            self._clock.setHour(hour + 1)

        if name == 'blue':
            # get the current minute
            minute = self._clock.getMinute()
            # set the minute to 1 + the current minute
            self._clock.setMinute(minute + 1)

    def buttonReleased(self, name):
        pass

    