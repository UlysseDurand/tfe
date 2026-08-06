import json
import subprocess


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
