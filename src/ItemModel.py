from CalendarModel import CalendarModel
from datetime import datetime


class ItemModel:
    def __init__(
        self, name: str, description: str, start: datetime, end: datetime
    ):
        self.name = name
        self.description = description
        self.start = start
        self.end = end

    def get_calendar_model(self):
        calendar_model = CalendarModel()

        calendar_model.summary = self.name
        calendar_model.description = self.description
        calendar_model.start = dict(
            dateTime=self.start.isoformat(), timeZone="Japan"
        )
        calendar_model.end = dict(
            dateTime=self.end.isoformat(), timeZone="Japan"
        )

        return calendar_model
