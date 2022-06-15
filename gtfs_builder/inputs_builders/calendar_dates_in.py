from gtfs_builder.core.core import OpenGtfs

import pandas as pd

import datetime

class CalendarDates(OpenGtfs):

    def __init__(self, core, input_file="calendar_dates.txt"):

        super(CalendarDates, self).__init__(core, core.path_data, input_file)

        if self.is_df_empty(self._input_data):
            raise ValueError(f"'{input_file}' is empty")

        self._format_date_column()

    def _format_date_column(self):
        self._input_data["date"] = [datetime.datetime.strptime(row, '%Y%m%d') for row in self._input_data["date"]]