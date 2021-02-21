from tinydb import TinyDB, Query
from pprint import pprint
db=TinyDB('data.json')
data=db.all()
q=Query()
user=db.search(q.age==18)
for i in user:
    pprint(i)