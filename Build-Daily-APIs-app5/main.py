import requests
from pprint import pprint
from send_email import send_email

api_key = "b0e4bea097324433a012937cb4788bd4"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-09-02&sortBy=publishedAt&api" \
      "Key=b0e4bea097324433a012937cb4788bd4"

# Make a request
r = requests.get(url)

# Get dictionary
content = r.json()

# Access title and description from the new
body = ""
for article in content['articles']:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"


message = f"""\
Subject: Latest news article

From: kojibello058@.gmail.com
{body}
"""
message = message.encode('utf-8')
send_email(message)
