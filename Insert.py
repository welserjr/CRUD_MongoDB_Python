import pymongo

#Establecemos una conexion a la base de datos
con = pymongo.Connection("mongodb://localhost", safe=True)
#Elegimos la base de datos
db = con.test
#Elegimos la collection
collection = db.people

welser = {'name': 'Welser Munoz', 'company': '10gen', 
			'interests': ['coding', 'dancing', 'guitar']}
orlando = {'_id': 'orlando', 'name': 'Orlando Munoz', 'company': '10gen',
               'interests': ['futbol', 'games', 'running']}

try:
	#collection.insert(welser)
	collection.insert(orlando)
	print("Insert Succesfull!!!")
except Exception as e:
	print(e.args)