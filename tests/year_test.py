from app.year import Year

# A leap year is defined as one that is divisible by 4, but is not otherwise divisible by 100 unless it is also divisible by 400.

# For example:
# 2001 is a typical common year
# 1996 is a typical leap year
# 1900 is an atypical common year
# 2000 is an atypical leap year


class TestYear:
    def test_typical_common_year(self):
        year = Year(2001)
        assert year.is_leap_year() == False

    def test_typical_leap_year(self):
        year = Year(1996)
        assert year.is_leap_year() == True

    def test_atypical_common_year(self):
        year = Year(1900)
        assert year.is_leap_year() == False
