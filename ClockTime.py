#Q2
class ClockTime:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.time = 0

    def setHours(self, hours):
        self.hours = hours

    def setMinutes(self, minutes):
        self.minutes = minutes

    def setSeconds(self, seconds):
        self.seconds = seconds

    def setTime(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.time = str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)

    def showTime(self):
        return print("Time is: " + self.time)


result = 0
hours = int(input("Please enter hours: "))
minutes = int(input("Please enter minutes: "))
seconds = int(input("Please enter seconds: "))

ct = ClockTime()
ct.setTime(hours,minutes,seconds)
ct.showTime()