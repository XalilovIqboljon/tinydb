from tinydb import TinyDB
from pprint import pprint
db=TinyDB('product.json')
f=open('products.csv').read().split('\n')
for i in f[1:]:
    data=i.split(',')
    db.insert({'category':data[1],'company':data[2]})
