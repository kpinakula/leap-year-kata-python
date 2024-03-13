class Year:
    def __init__(self, year):
        self.year = year

    def is_leap_year(self):
        return self.year % 4 == 0
