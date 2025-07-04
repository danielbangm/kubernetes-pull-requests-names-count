import requests

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"

response = requests.get(url)
list_count = {}


if response.status_code == 200:
    pulls = response.json()
    for pull in pulls:
        user = pull['user']['login']
        if user in list_count:
            list_count[user] += 1
        else:
            list_count[user] = 1
    for user, count in list_count.items():
        print(f"{user}: {count} pull requests")       
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
