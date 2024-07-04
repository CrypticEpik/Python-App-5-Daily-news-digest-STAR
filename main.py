import requests as reqs

api_key = "a2ac804a72cc48aea19b8b8ecb7da47f"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-06-04&sortBy=publishedAt&apiKey=a2ac804a72cc48aea19b8b8ecb7"
       "da47f")
# Make request
request = reqs.get(url)

# Get a dictionary with data
content = request.json()

#Access the article titles and description
for article in content["articles"]:
       print(article["title"])