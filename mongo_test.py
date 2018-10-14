import pymongo

from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = [{ "_id" : "1", "name": "John", "address": "Highway 39" }, { "_id": 2, "name": "John", "address": "Highway 37" }]

for d in mydict:
    mycol.update({'_id':d['_id']}, d,True)

data = [i for i in mycol.find({"_id": '1'})]
print(data)

#x = mycol.insert_many(mydict)
myquery = { "limit": 1, "_id":"-1"}

cursor = mycol.find({'id':{ '$eq': '1'}})

for doc in cursor:
	print(doc)


'''nameqry = {"name": "john"}

myquery = { "sort": { "_id": -1 }}
lmt_qry =  { "limit": 1 }


mydoc = mycol.find(nameqry)

print(mydoc.count)

for x in mydoc:
    print(x)'''