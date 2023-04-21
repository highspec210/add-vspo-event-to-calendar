from datetime import datetime, timedelta
import googleapiclient.discovery
import google.auth
import os
from dotenv import load_dotenv
from CalendarModel import CalendarModel


class CalendarManager:
    def __init__(self):
        SCOPES = ["https://www.googleapis.com/auth/calendar"]
        load_dotenv()
        self.calendar_id = os.environ["CALENDAR_ID"]
        self.gapi_creds = google.auth.load_credentials_from_file(
            "make-calendar-event-647801856e3c.json", SCOPES
        )[0]

    def add_event(self, bodyModel: CalendarModel):
        service = googleapiclient.discovery.build(
            "calendar", "v3", credentials=self.gapi_creds
        )

        return (
            service.events()
            .insert(calendarId=self.calendar_id, body=bodyModel.getBody())
            .execute()
        )

    def add_test_event(self):
        service = googleapiclient.discovery.build(
            "calendar", "v3", credentials=self.gapi_creds
        )
        now = datetime.now()
        calendarModel = CalendarModel()
        calendarModel.summary = "今から1時間後に1時間のテスト予定"
        calendarModel.description = "今は" + now.strftime("%Y/%m/%d %H:%M:%S")
        calendarModel.start = dict(
            dateTime=(now + timedelta(hours=1)).isoformat(), timeZone="Japan"
        )
        calendarModel.end = dict(
            dateTime=(now + timedelta(hours=2)).isoformat(),
            timeZone="Japan",
        )
        body = calendarModel.getBody()

        return service.events().insert(calendarId=self.calendar_id, body=body).execute()
