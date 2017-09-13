from pymongo import MongoClient

client = MongoClient('mongodb://:@/admin?authMechanism=SCRAM-SHA-1')
