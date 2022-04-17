class DatesWithDayOfWeek:
    def __init__(self):
        self.calendar = dict()
        self.daysOfWeek = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
        self.fill_calendar_dates()

    def fill_calendar_dates(self):
        from datetime import date, timedelta
        start_year = 2022
        date = date(year=start_year, month=1, day=1)
        while date.year <= start_year + 400:
            self.calendar[(date.year, date.month, date.day)] = self.daysOfWeek[date.weekday()]
            date += timedelta(days=1)

    def print(self):
        print(self.calendar)
