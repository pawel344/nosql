# -*- coding: utf-8 -*-
import urllib2
import json
from pymongo import Connection
from bson.code import Code
from  couchdb import Server,PreconditionFailed

mongoport=27017
mongosrv="127.0.0.1"
cdbport=5984
cdbsrv="127.0.0.1"

url="http://blip.pl/statuses/all?limit=5" 
data = urllib2.urlopen(url).read()
connection = Connection(mongosrv, mongoport)
dbm = connection["blip"]
json = json.loads(data) 
dbm.statusy.insert(json)

map = Code("function () {"
"this.body.match(/[a-zA-Z\u0104-\u017c]+/g).forEach(function(x) {"
"emit(x, 1);"
"});"
"}")

reduce = Code("function (key, values) {"
"var sum = 0;"
"for (var i = 0; i < values.length; i++) {"
"   sum += values[i];"
"}"
"return sum;"
"}")

result=dbm.statusy.map_reduce(map,reduce,"full_response=True")
print u"wynik dzia\u0142ania mapreduce dla mongodb:"
for row in result.find():
  print row["_id"],int(row["value"])


server = Server("http://"+cdbsrv+":"+str(cdbport))

try:
  dbc = server.create('blip')
except PreconditionFailed:
  del server['blip']
  dbc = server.create('blip')
  dbc = server['blip']
  
for row in dbm.statusy.find():
  del row["_id"]
  dbc.save(row)
  
map = '''function(doc) {
  doc.body.match(/[a-zA-Z\u0104-\u017c]+/g).forEach(function(x) {
  emit(x,1); 
} )
}'''
reduce = '''function(key,values) {
  return sum(values);
}'''
  
print
print u"wynik dzia\u0142ania  mapreduce dla Couchdb:"
for row in dbc.query(map,reduce,group=True):
  print row["key"],row["value"]
