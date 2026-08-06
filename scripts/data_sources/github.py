import json
import subprocess
import urllib.error
import urllib.parse
import urllib.request

GITLAB_HOST = "gitlab.kitware.com"
GITLAB_API = f"https://{GITLAB_HOST}/api/v4"
GITLAB_PER_PAGE = 100


def get_user_commits(repo: str, username: str):
    if repo.startswith(f"{GITLAB_HOST}/"):
        return get_user_commits_glab(repo, username)
    return get_user_commits_gh(repo, username)


def get_user_commits_gh(repo: str, username: str):
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

    request = [
        "gh",
        "api",
        "graphql",
        "-f",
        f"query={query}",
        "-F",
        f"owner={owner}",
        "-F",
        f"name={name}",
    ]

    result = subprocess.run(request, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(
            "Error executing command "
            f"{' '.join(request)[:100]}:\n{result.stderr}\n{result.stdout}"
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
                        "branch": branch["name"],  # include branch it's on
                    }
                )

    return commits


def get_user_commits_glab(repo: str, username: str):
    project = repo.removeprefix(f"{GITLAB_HOST}/")
    base_url = (
        f"{GITLAB_API}/projects/{urllib.parse.quote(project, safe='')}"
        f"/repository/commits?author={urllib.parse.quote(username)}"
        f"&per_page={GITLAB_PER_PAGE}"
    )

    commits = []
    page = 1
    while True:
        try:
            with urllib.request.urlopen(f"{base_url}&page={page}") as response:
                data = json.load(response)
        except urllib.error.HTTPError as exc:
            raise RuntimeError(
                f"Error fetching commits for {repo}: HTTP {exc.code} {exc.reason}"
            ) from exc

        for commit in data:
            commits.append(
                {
                    "repo": repo,
                    "sha": commit["id"],
                    "date": commit["committed_date"],
                    "message": commit["title"],
                    "url": commit["web_url"],
                    "branch": "",
                }
            )
        if len(data) < GITLAB_PER_PAGE:
            break
        page += 1

    return commits
