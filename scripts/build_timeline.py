from datetime import datetime
from itertools import chain

import matplotlib.pyplot as plt
from data_sources.calendar import get_calendar_events
from data_sources.github import get_user_commits

EVENT_TYPES = [
    "Office",
    "Point",
    "Tech",
    "Radial Menu",
    "Mobile trame-slicer",
]
MAINTENANCE_REPOS = {
    "Kitware/trame": "UlysseDurand",
    "UlysseDurand/trame": "UlysseDurand",
    "Kitware/trame-tutorial": "UlysseDurand",
    "UlysseDurand/trame-tutorial": "UlysseDurand",
    "Kitware/trame-vtk": "UlysseDurand",
    "UlysseDurand/trame-vtk": "UlysseDurand",
    "Kitware/trame-cookiecutter": "UlysseDurand",
    "UlysseDurand/trame-cookiecutter": "UlysseDurand",
    "UlysseDurand/github-retriever": "UlysseDurand",
    "Kitware/trame-rca": "UlysseDurand",
    "UlysseDurand/trame-rca": "UlysseDurand",
    "conda-forge/staged-recipes": "UlysseDurand",
    "UlysseDurand/staged-recipes": "UlysseDurand",
    "conda-forge/trame-radial-menu-feedstock": "UlysseDurand",
}
RADIAL_MENU_REPOS = {
    "Kitware/trame-radial-menu": "UlysseDurand",
}
MOBILE_TRAME_SLICER_REPOS = {
    "gitlab.kitware.com/vtk/vtk": "ulysse.durand",
    "Slicer/Slicer": "UlysseDurand",
    "UlysseDurand/Slicer": "UlysseDurand",
    "KitwareMedical/SlicerCore": "UlysseDurand",
    "UlysseDurand/SlicerCore": "UlysseDurand",
}
EVENT_COLORS = ["#5b8dee", "#f4a261", "#57cc99", "#e056fd", "#ff6b6b"]


def to_date(value):
    if not isinstance(value, str):
        if getattr(value, "tzinfo", None):
            value = value.replace(tzinfo=None)
        return value.replace(hour=0, minute=0, second=0, microsecond=0)
    formats = (None, "%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y")
    for fmt in formats:
        try:
            if fmt is None:
                dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
            else:
                dt = datetime.strptime(value, fmt)
            if dt.tzinfo:
                dt = dt.replace(tzinfo=None)
            return dt.replace(hour=0, minute=0, second=0, microsecond=0)
        except ValueError:
            pass
    raise ValueError(f"Unsupported date format: {value}")


def get_commit_days(repos):
    commits = []
    for repo, username in repos.items():
        commits.extend(get_user_commits(repo, username))
    return [to_date(e["date"]) for e in commits]


def main():
    events = {
        name: sorted(to_date(e["start-date"]) for e in get_calendar_events(name))
        for name in EVENT_TYPES
    }
    events["Maintenance"] = get_commit_days(MAINTENANCE_REPOS)
    events["Radial Menu"] += get_commit_days(RADIAL_MENU_REPOS)
    events["Mobile trame-slicer"] += get_commit_days(MOBILE_TRAME_SLICER_REPOS)

    # --- categorical x-axis: only Office days exist ---
    office_days = sorted(set(events.pop("Office")))
    if not office_days:
        raise SystemExit("No Office events found.")
    day_to_index = {day: i for i, day in enumerate(office_days)}

    events = {
        name: [day_to_index[day] for day in day_list if day in day_to_index]
        for name, day_list in events.items()
    }

    all_indices = list(chain.from_iterable(events.values()))
    if not all_indices:
        raise SystemExit("No events found on Office days.")

    n = len(office_days)
    pad = max(n * 0.02, 0.5)

    _, ax = plt.subplots(figsize=(14, len(events.keys())))
    ax.set_yticks(range(len(events.keys())))
    ax.set_yticklabels(events.keys())

    for row, (name, color) in enumerate(zip(events.keys(), EVENT_COLORS, strict=True)):
        for idx in events[name]:
            ax.barh(row, 1, left=idx, color=color)

    # tick selection: aim for a readable number of labels regardless of n
    max_ticks = 20
    step = max(1, n // max_ticks)
    tick_idx = list(range(0, n, step))
    if tick_idx[-1] != n - 1:
        tick_idx.append(n - 1)

    ax.set_xticks(tick_idx)
    ax.set_xticklabels(
        [office_days[i].strftime("%d %b") for i in tick_idx],
        rotation=45,
        ha="right",
    )

    ax.set_xlim(-pad, n + pad)
    ax.grid(axis="x", which="major", alpha=0.3)

    plt.tight_layout()
    plt.savefig("../assets/images/timeline.png", dpi=150, bbox_inches="tight")


if __name__ == "__main__":
    main()
