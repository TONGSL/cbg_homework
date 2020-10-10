import pymongo

def connectDB():
	#连接到mongodb及对应collection
	#client = pymongo.MongoClient(host='localhost')
	#db = client.cbg_homework
	#collection = db.zijinzhidian
	print("connected to:"+str(db.collection_names()))

def singledata():
	result = collection.find_one()
	print(result)

def findSumScore():
	result = collection.find({'价格':{'$gt':'800000.00'}}).count()
	print(result)

if __name__=='__main__':
	#连接到mongodb及对应collection
	client = pymongo.MongoClient(host='localhost')
	db = client.cbg_homework
	collection = db.zijinzhidian
	connectDB()
	singledata()
	findSumScore()