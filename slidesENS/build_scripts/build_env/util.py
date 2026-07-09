import yaml
import subprocess
import json
import os
from dotenv import load_dotenv
load_dotenv()

def read_yml(filename):
    with open("../assets/infos/" + filename, 'r') as f:
        infos = yaml.safe_load(f)
        return infos

def get_events_from_ics(start_date, end_date):
    url = os.getenv("LOCAL_CALENDAR_URL")
    cmd = [
        "icalendar-events-cli",
        "--calendar.url", url,
        "-s", start_date, "-e", end_date,
        "--output.format", "json"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Error running icalendar-events-cli: {result.stderr}")
    
    events = json.loads(result.stdout)["events"]
    return events

def get_user_commits(repo: str, username: str):
    owner, name = repo.split("/")

    query = """
    query($owner: String!, $name: String!) {
      repository(owner: $owner, name: $name) {
        refs(refPrefix: "refs/heads/", first: 100) {
          nodes {
            name
            target {
              ... on Commit {
                history(first: 100) {
                  nodes {
                    oid
                    committedDate
                    messageHeadline
                    url
                    author {
                      user {
                        login
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    """

    result = subprocess.run(
        [
            "gh",
            "api",
            "graphql",
            "-f",
            f"query={query}",
            "-F",
            f"owner={owner}",
            "-F",
            f"name={name}",
        ],
        capture_output=True,
        text=True,
        check=True
    )

    data = json.loads(result.stdout)

    commits = []
    seen_commits = set()  # To avoid duplicates if a commit exists on multiple branches

    # Iterate through all branches
    for branch in data["data"]["repository"]["refs"]["nodes"]:
        for commit in branch["target"]["history"]["nodes"]:
            commit_oid = commit["oid"]
            
            # Skip if we've already processed this commit
            if commit_oid in seen_commits:
                continue
            seen_commits.add(commit_oid)

            author = commit.get("author", {}).get("user")
            
            # Check if the author matches the given username
            if author and author.get("login") == username:
                commits.append(
                    {
                        "repo": repo,
                        "sha": commit_oid,
                        "date": commit["committedDate"],
                        "message": commit["messageHeadline"],
                        "url": commit["url"],
                        "branch": branch["name"],  # Optional: include which branch it's on
                    }
                )
    
    return commits