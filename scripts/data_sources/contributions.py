import re

from .io import load_yaml

CONTRIBUTIONS_FILE = "../config/contributions.yml"

_REPO_PATTERNS = (
    re.compile(r"github\.com/([^/]+/[^/]+)"),
    re.compile(r"gitlab\.kitware\.com/([^/]+/[^/]+)"),
)
_PR_NB = re.compile(r"/(?:pull|merge_requests)/(\d+)/?$")


def get_prs():
    prs = load_yaml(CONTRIBUTIONS_FILE)["PR"]
    for pr in prs:
        pr["fullName"] = to_full_name(pr["url"])
        pr["prNb"] = to_pr_nb(pr["url"])
    return prs


def to_full_name(url):
    for pattern in _REPO_PATTERNS:
        match = pattern.search(url)
        if match:
            return match.group(1)
    return ""


def to_pr_nb(url):
    match = _PR_NB.search(url)
    return match.group(1) if match else ""


def get_issues():
    return load_yaml(CONTRIBUTIONS_FILE)["issues"]
