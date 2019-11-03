class Time:
    def __init__(self):
        """
        Constructor
        The default time is midnight
        The default format is 24-hour
        """
        self.second = 0
        self.minute = 0
        self.hour = 0
        self.format = 24

    def set_time(self, second, minute, hour):
        """
        set_time
        :param hour: int
        :param minute: int
        :param second: int
        :return: nothing
        Does: Set the format attribute to the given integer
        """
        while True:
            if 0 <= second <= 59:
                self.second = second
                break
            else:
                print("Oops, enter a number between 0 and 59, please try again!")
                second = int(input("Enter second "))

        while True:
            if 0 <= minute <= 59:
                self.minute = minute
                break
            else:
                print("Oops, enter a number between 0 and 59, please try again!")
                minute = int(input("Enter minute "))

        while True:
            if 0 <= hour <= 23:
                self.hour = hour
                break
            else:
                print("Oops, enter a number between 0 and 23, please try again!")
                hour = int(input("Enter hour "))

    def set_format(self, new_format):
        """
        set_format
        :param: new_format
        :return: nothing
        Does: Set the time format
        """
        self.format = new_format

    def __str__(self):
        """
        __str__
        :param: nothing
        :return: Time
        """
        if self.format == 24:
            # The time format is 00:00:00
            return "{:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)
        else:
            if self.hour < 12:
                # 00:00:00 AM would be 12:00:00 AM
                if self.hour == 0:
                    hour = 12
                else:
                    hour = self.hour
                return "{:02d}:{:02d}:{:02d}".format(hour, self.minute, self.second) + " AM "
            else:
                if self.hour == 12:
                    hour = 12
                else:
                    hour = self.hour % 12
                return "{:02d}:{:02d}:{:02d}".format(hour, self.minute, self.second) + " PM "
