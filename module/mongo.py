from pymongo import MongoClient
from config import dbconf

client = MongoClient(dbconf.db_addr,user = dbconf.db_user,password = dbconf.db_pass, authSource='admin',authMechanism='SCRAM-SHA-1')
