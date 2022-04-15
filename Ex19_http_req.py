import requests
r = requests.get('https://www.google.com')
r.status_code
r.headers['Date']
r.text
r.encoding
r.content
r.json()
r.url
r.history
r.cookies
