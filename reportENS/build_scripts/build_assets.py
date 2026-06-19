from datetime import datetime
from itertools import chain

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from build_env.events import get_events 
from build_env.util import get_user_commits

event_types = [
    "Office",
    "Point",
    "Tech",
    "Radial Menu",
    "Mobile trame-slicer",
]

maintenance_repos = [
    "Kitware/trame",
    "Kitware/trame-tutorial",
    "Kitware/trame-vtk",
    "Kitware/trame-cookiecutter",
    "UlysseDurand/github-retriever"
]

COLORS = ["#5b8dee", "#f4a261", "#57cc99", "#e056fd", "#ff6b6b", "#7BAF01E2"]



def to_day(value):
    if not isinstance(value, str):
        if getattr(value, "tzinfo", None):
            value = value.replace(tzinfo=None)
        return value.replace(hour=0, minute=0, second=0, microsecond=0)

    formats = (None, "%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y")

    for fmt in formats:
        try:
            if fmt is None:
                dt = datetime.fromisoformat(
                    value.replace("Z", "+00:00")
                )
            else:
                dt = datetime.strptime(value, fmt)

            if dt.tzinfo:
                dt = dt.replace(tzinfo=None)

            return dt.replace(hour=0, minute=0, second=0, microsecond=0)

        except ValueError:
            pass

    raise ValueError(f"Unsupported date format: {value}")

def main():
    maintenance_commits = []
    for repo in maintenance_repos:
        maintenance_commits.extend(
            get_user_commits(repo, "UlysseDurand")
        )
    maintenance_events = [to_day(e['date']) for e in maintenance_commits]

    events = {
        name: sorted(to_day(e["start-date"]) for e in get_events(name))
        for name in event_types
    }
    events["Maintenance"] = maintenance_events
    events["Radial Menu"] += [to_day(e['date']) for e in get_user_commits("Kitware/trame-radial-menu", "UlysseDurand")]

    days = list(chain.from_iterable(events.values()))
    if not days:
        raise SystemExit("No events found.")

    x_min, x_max = min(days), max(days)
    span = (x_max - x_min).days
    pad = max(span * 0.02, 1)

    fig, ax = plt.subplots(figsize=(14, len(events.keys())))

    ax.set_yticks(range(len(events.keys())))
    ax.set_yticklabels(events.keys())

    for row, (name, color) in enumerate(zip(events.keys(), COLORS)):
        for day in events[name]:
            ax.barh(
                row,
                1,
                left=mdates.date2num(day),
                color=color,
            )

    if span <= 60:
        ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
    elif span <= 400:
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    else:
        ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 4, 7, 10]))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%b '%y"))

    ax.xaxis.set_minor_locator(mdates.DayLocator())
    ax.grid(axis="x", which="minor")
    ax.tick_params(axis="x", which="minor", length=0)

    ax.set_xlim(
        mdates.date2num(x_min) - pad,
        mdates.date2num(x_max) + 1 + pad,
    )

    fig.autofmt_xdate()
    plt.tight_layout()
    plt.savefig("assets/images/timeline.png", dpi=150, bbox_inches="tight")

if __name__ == "__main__":
    main()