from datetime import datetime, timedelta
import googleapiclient.discovery
import google.auth
import os
from dotenv import load_dotenv


class CalendarManager:
    def __init__(self):
        SCOPES = ["https://www.googleapis.com/auth/calendar"]
        load_dotenv()
        self.calendar_id = os.environ["CALENDAR_ID"]
        self.gapi_creds = google.auth.load_credentials_from_file(
            "make-calendar-event-647801856e3c.json", SCOPES
        )[0]

    def add_test_event(self):
        service = googleapiclient.discovery.build(
            "calendar", "v3", credentials=self.gapi_creds
        )
        now = datetime.now()
        body = {
            "summary": "今から1時間後に1時間のテスト予定",
            "description": "今は" + now.strftime("%Y/%m/%d %H:%M:%S"),
            "start": {
                "dateTime": (now + timedelta(hours=1)).isoformat(),
                "timeZone": "Japan",
            },
            "end": {
                "dateTime": (now + timedelta(hours=2)).isoformat(),
                "timeZone": "Japan",
            },
        }

        print(service.events().insert(calendarId=self.calendar_id, body=body).execute())
