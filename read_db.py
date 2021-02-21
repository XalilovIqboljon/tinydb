from tinydb import TinyDB
from pprint import pprint
db=TinyDB('data.json')
data=db.all()
for i in data:
    print(i['name'][0])