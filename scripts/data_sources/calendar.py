import json
import os
import re
import subprocess

from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

CALENDAR_START = "2026-03-30"
CALENDAR_END = "2026-08-22"

EVENT_PATTERNS = {
    "": r"",
    "Point": r"Ulysse / Julien",
    "Tech": r"Techtip|TechMeet|Reading Group|Techlunch",
    "Radial Menu": r"Ulysse / Lucie|Ulysse/Lucie|Point Krita",
    "Mobile trame-slicer": r"trame-slicer mobile",
    "Office": r"Office",
}


def fetch_calendar_events(start_date, end_date):
    url = os.getenv("LOCAL_CALENDAR_URL")
    cmd = [
        "icalendar-events-cli",
        "--calendar.url", url,
        "-s", start_date, "-e", end_date,
        "--output.format", "json",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(f"Error running icalendar-events-cli: {result.stderr}")
    return json.loads(result.stdout)["events"]


def get_calendar_events(category):
    events = fetch_calendar_events(CALENDAR_START, CALENDAR_END)
    pattern = EVENT_PATTERNS[category]
    return [event for event in events if re.search(pattern, event["summary"])]
