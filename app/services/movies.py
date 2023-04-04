from repositories.movies_repository import MovieRepository
from schema.movies import MovieSchema
from schema.input_recommendation import InputRecommendation
from services.input import InputService

class MovieService():

    def __init__(self):
        self.repository = MovieRepository()
    
    def get_movie_from_mongo(self, imdb_id: str):
        movie = self.repository.find_movie_by_id(imdb_id)
        movie = MovieSchema(
            title=movie.get("title", None),
            genres=movie.get("genres", None),
            release_year=movie.get("release_year", None),
            runtime=movie.get("runtime", None),
            vote_average=movie.get("vote_average", None),
            overview=movie.get("overview", None),
            original_language=movie.get("original_language", None),
            popularity=movie.get("popularity", None),
            production_countries=movie.get("production_countries", None),
            production_companies=movie.get("production_companies", None),
            belongs_to_collection=movie.get("belongs_to_collection", None),
            poster_path=movie.get("poster_path", None),
            imdb_id=movie.get("imdb_id", None),
            tmdb_id=movie.get("tmdb_id", None)
        )
        return movie.title


    def get_recommendation(input_recommendation: InputRecommendation):
        input_service = InputService()

        is_valid = input_service.validate_input_data(input_recommendation)

        if not (is_valid):
            return {"status": "invalid input"}
        return {"status": "ok"}