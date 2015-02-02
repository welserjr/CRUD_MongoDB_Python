import pymongo

con = pymongo.Connection("mongodb://localhost", safe=True)
db = con.test
collection = db.people

try:
	collection.remove({'name': 'Fred'})
	print("Delete Succesfull!!!")
except Exception as e:
	print(e.args)