class DatesWithDayOfWeek:
    def __init__(self):
        self.start_year = 1800
        self.number_of_years = 400
        self.calendar = dict()
        self.daysOfWeek = ("pon", "wto", "śro", "czw", "pią", "sob", "nie")
        self.fill_calendar_dates()

    def fill_calendar_dates(self):
        from datetime import date, timedelta
        day = date(year=self.start_year, month=1, day=1)

        while day.year <= self.start_year + self.number_of_years:
            self.calendar[(day.year, day.month, day.day)] = self.daysOfWeek[day.weekday()]
            day += timedelta(days=1)

    def print(self):
        pass
        # print(self.calendar[2022, 4, 17])


    def find_next_date_with_the_same_weekday(self):
        for day, dayOfWeek in self.calendar.items():
            # print(day, dayOfWeek)
            current_year = day[0]
            current_month = day[1]
            current_day = day[2]
            last_year = list(self.calendar.keys())[-1][0]
            for years in range(current_year, last_year):
                # print(current_year + 1, current_month, current_day, self.calendar[current_year + 1, current_month, current_day])
                # print(self.calendar.get((current_year + 1, current_month, current_day)), dayOfWeek)
                 if self.calendar.get((current_year + 1, current_month, current_day)) == dayOfWeek:
                    print(day, self.calendar[current_year + 1, current_month, current_day])


