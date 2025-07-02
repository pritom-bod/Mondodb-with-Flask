from pymongo import MongoClient
from bson import ObjectId
# MongoDB Atlas or local connection string
MONGO_URI = "mongodb+srv://pritomsarker406:2voCIiSjQBEYMvGb@cluster0.aegipsm.mongodb.net/"

client = MongoClient(MONGO_URI)
db = client["blog_db"]


