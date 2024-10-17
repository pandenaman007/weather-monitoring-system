from pymongo import MongoClient
from config.config import MONGODB_URI

client = MongoClient(MONGODB_URI)
db = client.weather_db

def store_weather_data(data):
    db.weather_data.insert_one(data)
