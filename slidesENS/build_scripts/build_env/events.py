import re

from .util import get_events_from_ics

def get_events(key):
    events = get_events_from_ics("2026-03-30", "2026-08-22")
    patterns = {
        "": r"",
        "Point": r"Ulysse / Julien",
        "Tech": r"Techtip|TechMeet|Reading Group|Techlunch",
        "Radial Menu": r"Ulysse / Lucie|Ulysse/Lucie|Point Krita",
        "Mobile trame-slicer": r"trame-slicer mobile",
        "Office": r"Office",
    }
    events = list(filter(lambda event: re.search(patterns[key], event["summary"]), events))
    return events