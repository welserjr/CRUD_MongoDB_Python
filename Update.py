import pymongo
import datetime

con = pymongo.Connection("mongodb://localhost", safe=True)
db = con.test
collection = db.scores

try:
	now = datetime.datetime.now()
	fecha = now.strftime("%y-%m-%d %H:%M:%S")
	collection.update({'student': 5, 'type': 'exam'}, {'$set': {'review_date': fecha}})
	print("Update Succesfull!!!")
except Exception as e:
	print(e.args)