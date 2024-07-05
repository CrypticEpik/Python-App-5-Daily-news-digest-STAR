import requests as reqs
from send_email import send_email

topic = "tesla"
api_key = "a2ac804a72cc48aea19b8b8ecb7da47f"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2024-06-04&sortBy=publishedAt&"
       "apiKey=a2ac804a72cc48aea19b8b8ecb7"
       "da47f")
# Make request
request = reqs.get(url)

# Get a dictionary with data
content = request.json()

#Access the article titles and description
body = ""
for article in content["articles"][:20]:
       if article["title"] is not None:
              body = "Subject: Today's news" + "\n" + (body + article["title"] + "\n" +article["description"] + "\n" +article["url"] + 2*"\n")

body = body.encode("utf-8")
send_email(message=body)