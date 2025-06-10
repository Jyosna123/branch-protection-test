import os
import requests

token = os.environ.get("GH_TOKEN")
if not token:
    raise Exception("GH_TOKEN is not set")

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

url = "https://api.github.com/repos/Jyosna123/Project/branches/master/protection"

payload = {
    "required_pull_request_reviews": {"dismiss_stale_reviews": True},
    "enforce_admins": False,
    "restrictions": None,
    "required_status_checks": None
}

res = requests.put(url, headers=headers, json=payload)
print(res.status_code, res.text)
