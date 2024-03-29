class Year:
    def __init__(self, year):
        self.year = year

    def is_leap_year(self):
        if self.year % 400 == 0:
            return True

        if self.year % 100 == 0:
            return False

        return self.year % 4 == 0
