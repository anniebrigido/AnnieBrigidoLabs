from Counters import Time

class Clock:
    """
    Our implementation of the Clock class
    """
    
    def getMonth(self):
        """ return the current month as an int """
        timetuple = Time.getTime()
        return timetuple[1]

    def setMonth(self, month):
        """ Sets the RTC month to the month parameter """
        # First, get the current time from the system
        timetuple = Time.getTime()
        # Convert the tuple into a list
        timelist = list(timetuple)
        # Change the month to the new month
        timelist[1] = month
        # Save it back to the system
        Time.setTime(timelist)

    def getDate(self):
        """ return the current date as an int """
        timetuple = Time.getTime()
        return timetuple[2]

    def setDate(self, date):
        """ Sets the RTC date to the date parameter """
        # First, get the current time from the system
        timetuple = Time.getTime()
        # Convert the tuple into a list
        timelist = list(timetuple)
        # Change the date to the new date
        timelist[2] = date
        # Save it back to the system
        Time.setTime(timelist)
    
    def getTime(self):
            return Time.getTime()

    def setTime(self, timetuple):
            Time.setTime(timetuple)

    def getHour(self):
        """ return the current hour as an int """
        timetuple = Time.getTime()
        return timetuple[3]

    def setHour(self, hour):
        """ Sets the RTC Hour to the hour parameter """
        # First, get the current time from the system
        timetuple = Time.getTime()
        # Convert the tupple into a list
        timelist = list(timetuple)
        # Change the hour to the new hour
        timelist[3] = hour
        # Save it back to the system
        Time.setTime(timelist)
    
    def getMinute(self):
        """ return the current minute as an int """
        timetuple = Time.getTime()
        return timetuple[4]

    def setMinute(self, minute):
        """ Sets the RTC minute to the minute parameter """
        # First, get the current time from the system
        timetuple = Time.getTime()
        # Conver the tupple into a list
        timelist = list(timetuple)
        # Change the minute to the new minute
        timelist[4] = minute
        # Save it back to the system
        Time.setTime(timelist)

    