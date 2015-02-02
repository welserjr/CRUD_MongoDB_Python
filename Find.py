import pymongo

con = pymongo.Connection("mongodb://localhost", safe=True)
db = con.test
collection = db.scores

query = {'type': 'exam'}
try:
	cursor = collection.find(query)
	cDoc = 0
	for doc in cursor:
		print(doc)
		cDoc += 1
		if(cDoc > 10):
			break
except Exception as e:
	print(e.args)

