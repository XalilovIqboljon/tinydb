from tinydb import TinyDB
from pprint import pprint
db=TinyDB('specifications.json')
f=open('specifications.csv').read().split('\n')
for i in f[1:]:
    data=i.split(',')
    db.insert({'model':data[1],'company':data[2],'price':data[3]})