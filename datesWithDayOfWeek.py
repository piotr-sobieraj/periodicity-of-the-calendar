class DatesWithDayOfWeek:
    def __init__(self):
        self.calendar = {}
        self.fill_calendar_dates()

    def fill_calendar_dates(self):
        self.calendar["year"] = 1900

    def print(self):
        print(self.calendar)