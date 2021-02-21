from tinydb import TinyDB

db=TinyDB('data.json')
user1={'name':'Sanjar','age':18}
user2={'name':'Olimjon','age':18}
user3={'name':'Javohir','age':21}
db.insert(user1)
db.insert(user2)
db.insert(user3)