from .util import read_yml
import re

def get_prs():
    prs = read_yml("accomplished.yml")["PR"]
    for pr in prs:
        pr["fullName"] = to_full_name(pr["url"])
        pr["prNb"] = to_pr_nb(pr["url"])
    return prs

def to_full_name(url):
    return re.compile(r"github.com/([^/]*/[^/]*)/.*$").findall(url)[0]

def to_pr_nb(url):
    return re.compile(r"github.com/.*/pull/*(.*)$").findall(url)[0]

def get_issues():
    return read_yml("accomplished.yml")["Issues"]