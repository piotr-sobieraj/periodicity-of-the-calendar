class DatesWithDayOfWeek:
    def __init__(self):
        self.start_year = 1800
        self.number_of_years = 400
        self.calendar = dict()
        self.daysOfWeek = ("pon", "wto", "sro", "czw", "pia", "sob", "nie")
        self.fill_calendar_dates()
        self.temp_result = []
        self.result = []

    def fill_calendar_dates(self):
        from datetime import date, timedelta
        day = date(year=self.start_year, month=1, day=1)

        while day.year <= self.start_year + self.number_of_years:
            self.calendar[(day.year, day.month, day.day)] = self.daysOfWeek[day.weekday()]
            day += timedelta(days=1)

    def print(self):
        from prettytable import PrettyTable
        import operator
        self.convert_tuples_to_dates()
        pretty_result = PrettyTable()
        pretty_result.field_names = ["Badana data", "Dzień tyg.", "Nast. wystąpienie", "Za ile lat"]
        pretty_result.add_rows(self.result)
        pretty_result = pretty_result.get_string(sort_key=operator.itemgetter(0), sortby="Za ile lat", reversesort=True)

        print(pretty_result)

    def find_next_date_with_the_same_weekday(self):
        for day, dayOfWeek in self.calendar.items():
            current_year = day[0]
            current_month = day[1]
            current_day = day[2]
            last_year = list(self.calendar.keys())[-1][0]

            # Looking towards by 1 year
            # If dayOfWeeks are equal to each other - add to list
            difference_counter = 0
            for year in range(current_year + 1, last_year):
                difference_counter += 1
                if self.get_day_of_week_by_date(current_day, current_month, year) == dayOfWeek:
                    self.temp_result.append((day, dayOfWeek, (year, current_month, current_day), difference_counter))
                    break

    def get_day_of_week_by_date(self, current_day, current_month, year):
        return self.calendar.get((year, current_month, current_day))

    def convert_tuples_to_dates(self):
        for row in self.temp_result:
            row_start_date = row[0]
            row_end_date = row[2]

            self.result.append((
                "{:d}-{:02d}-{:02d}".format(row_start_date[0], row_start_date[1], row_start_date[2]),
                row[1],
                "{:d}-{:02d}-{:02d}".format(row_end_date[0], row_end_date[1], row_end_date[2]),
                row[3]
            ))

    def save_result_to_file(self):
        self.convert_tuples_to_dates()
        with open("results.csv", "w") as file:
            for line in self.result:
                file.write(str(line) + "\n")
