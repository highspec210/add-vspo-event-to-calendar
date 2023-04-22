from CalendarModel import CalendarModel
from datetime import datetime, timedelta
from dotenv import load_dotenv
import google.auth
import googleapiclient.discovery
import os


class CalendarManager:
    def __init__(self):
        SCOPES = ["https://www.googleapis.com/auth/calendar"]
        load_dotenv()
        self.calendar_id = os.environ["CALENDAR_ID"]
        self.gapi_creds = google.auth.load_credentials_from_file(
            "make-calendar-event-647801856e3c.json", SCOPES
        )[0]

    def add_event(self, body_model: CalendarModel):
        service = googleapiclient.discovery.build(
            "calendar", "v3", credentials=self.gapi_creds
        )

        return (
            service.events()
            .insert(calendarId=self.calendar_id, body=body_model.get_body())
            .execute()
        )
