from pymongo import MongoClient
from utils.settings import Settings


class MovieRepository(object):

    def __init__(self):
        self.client = MongoClient(f"mongodb+srv://{Settings().mongo_user}:{Settings().mongo_password}@clustermovies.eeje8oz.mongodb.net/?retryWrites=true&w=majority")
        self.database = self.client[Settings().mongo_client]
        self.collection = self.database[Settings().mongo_db]
    
    def find_movie_by_id(self, movie_id: str):
        movie = self.collection.find_one({"imdb_id": movie_id})
        del movie["_id"]
        return movie

