from pymongo.mongo_client import MongoClient
from app import app
app.config.from_pyfile('settings.py')

uri = app.config['MONGO_URL']
MONGO_DATABASE =app.config['MONGO_DATABASE']
MONGO_COLLECTION =app.config['MONGO_COLLECTION']
client = MongoClient(uri)
db = client[MONGO_DATABASE]
collection = db[MONGO_COLLECTION]