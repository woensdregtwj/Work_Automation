"""
Auto-calculates the reporting deadlines set by HQ. The deadlines usually are
WD1, WD2, WD3, WD5. This exclude weekends, so if WD1 starts on Fri, then WD2
will be on Monday.
"""

import datetime


class Deadlines:
    def __init__(self, now=None):
        """Calls class Date for receiving the proper attributes for
        the date. 2 empty lists created in which we will append the
        deadline dates."""
        self.date = Date(now)
        self.deadline_days = []
        self.deadline_days_text = []

    def prepare_deadline_dates(self):
        """if self.isNow is True, it is assumed that the upcoming
        deadlines are being requested. If the 9th day of the current
        month was passed, then we already passed the deadlines of the
        self.date value and will determine the deadlines for the next
        month.
        If self.isNow is False, it is assumed that the deadlines of the
        specified month is being requested.
        """
        if self.date.day > 9 and self.date.isNow:
            deadline_day = datetime.datetime(
                self.date.year, self.date.month + 1, 1
            )
            while len(self.deadline_days) < 5:
                if deadline_day.weekday() in [5, 6]:
                    deadline_day = datetime.datetime(
                        self.date.year,
                        self.date.month + 1,
                        self.date.day + 1
                    )
                    continue
                else:
                    self.deadline_days.append(deadline_day.day)
                    deadline_day = datetime.datetime(
                        self.date.day,
                        self.date.month,
                        deadline_day.day + 1
                    )
        else:
            deadline_day = datetime.datetime(
                self.date.year, self.date.month, 1
            )
            while len(self.deadline_days) < 5:
                if deadline_day.weekday() in [5, 6]:
                    deadline_day = datetime.datetime(
                        self.date.year,
                        self.date.month,
                        deadline_day.day + 1
                    )
                    continue
                else:
                    self.deadline_days.append(deadline_day.day)
                    deadline_day = datetime.datetime(
                        self.date.year,
                        self.date.month,
                        deadline_day.day + 1
                    )

    def format_deadline_text(self):
        """Grabs the year, month of self.date and also the days that
        were defined through method 'prepare_deadline_dates'. These
        days are appended into self.deadline_days."""
        try:
            for deadline in range(5):
                self.deadline_days_text.append(
                    "Next Deadline: {}{:02d}".format(
                        self.date.datetime.strftime('%Y/%m/'),
                        (self.deadline_days[deadline]))
                )
        except IndexError as e:
            raise NoDatesPreparedError(
                f"{e} - Call the method .prepare_deadline_dates() first!"
            )


class Date:
    def __init__(self, datetime=None):
        """Composition for class 'Deadlines'. Sets up the date that
        will determine for what month the deadlines will be created."""
        self.datetime = self.set_date(datetime)

        self.year = self.datetime.year
        self.month = self.datetime.month
        self.day = self.datetime.day

        self.isNow = False

    def set_date(self, now):
        """Assigns a datetime.datetime to the self.datetime property.
        If no argument in the init was given, we use the .now() date."""
        if now and not isinstance(now, datetime.datetime):
            raise DateInputError(
                "This class only accepts a datetime.datetime instance "
                "as a valid argument")
        elif now:  # User set their own date
            self.isNow = False
            return now
        else:  # No date set, we default to .now()
            self.isNow = True
            return datetime.datetime.now()
            self.date = datetime.datetime.now()


class DateInputError(Exception):
    pass


class NoDatesPreparedError(Exception):
    pass
