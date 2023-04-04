from pymongo import MongoClient


class MovieRepository(object):

    def __init__(self):
        self.client = MongoClient("mongodb+srv://cinebusca_user:sc5aPHHyULJU0yHW@clustermovies.eeje8oz.mongodb.net/?retryWrites=true&w=majority")
        self.database = self.client["cinebusca_db"]
        self.collection = self.database["movies"]
    
    def find_movie_by_id(self, movie_id: str):
        movie = self.collection.find_one({"imdb_id": movie_id})
        del movie["_id"]
        return movie

