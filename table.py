from tinydb import TinyDB

db=TinyDB('table.json')
# db.truncate('table.json',all)
table=db.table('t1')
table1=db.table('t2')

table.insert({'name':'Iqboljon'})
table.insert({'name':'Umidjon'})

table1.insert({'name':'Azizbek'})
table1.insert({'name':'Nurbek'})
