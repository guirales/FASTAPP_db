from pyArango import ArangoClient

# Initialize the ArangoDB client.
client = ArangoClient()
db = client.db("mydb", username="root", password="guirales123")
users = db.collection("Prueba")
print(users.ids())