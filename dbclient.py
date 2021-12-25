import pymongo
client = pymongo.MongoClient()
client = pymongo.MongoClient(
    "mongodb://Lalit:Lalit123@cluster0-shard-00-00.tmayz.mongodb.net:27017,cluster0-shard-00-01.tmayz.mongodb.net:27017,cluster0-shard-00-02.tmayz.mongodb.net:27017/Lalit?ssl=true&replicaSet=atlas-biw0eu-shard-0&authSource=admin")

db = client.test
print(client)
