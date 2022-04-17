class DatesWithDayOfWeek:
    def __init__(self):
        self.start_year = 1800
        self.number_of_years = 10
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
            # Looking towards by 1 year
            # If dayOfWeeks are equal to each other - add to list
            for year in range(current_year, last_year):
                if self.calendar.get((year, current_month, current_day)) == dayOfWeek:
                    print(day, (year, current_month, current_day),  self.calendar[year, current_month, current_day])
                    break


