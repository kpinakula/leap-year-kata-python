from app.leap_year_checker import LeapYearChecker

# A leap year is defined as one that is divisible by 4, but is not otherwise divisible by 100 unless it is also divisible by 400.

# For example:
# 2001 is a typical common year
# 1996 is a typical leap year
# 1900 is an atypical common year
# 2000 is an atypical leap year


class TestYear:
    def test_common_year(self):
        year = 2001
        leap_year_checker = LeapYearChecker()
        assert leap_year_checker.is_leap_year(year) == False
