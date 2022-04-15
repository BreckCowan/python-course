import requests
r = requests.get('https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple')
r.status_code
print(r.text)
type(r.text)

import json
question = json.loads(r.text)

import pprint
pprint.pprint(question)

r = requests.get(
    'https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple')
r.status_code
print(r.text)
type(r.text)

question = json.loads(r.text)

pprint.pprint(question)

print(question['results'][0]['category'])

person = {'name': 'John', 'age': '27', 'job': 'developer'}
person_json = json.dumps(person)
print(person_json)
