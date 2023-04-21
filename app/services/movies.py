from repositories.movies_repository import MovieRepository
from schema.movies import MovieSchema
from schema.input_recommendation import InputRecommendation
from services.input import InputService
from services.movie_model import load_model, map_input_recommendation_to_predict
from movie_engine.models.DAO import InputPredict

class MovieService():

    def __init__(self):
        self.repository = MovieRepository()
    
    def get_movie_from_mongo(self, imdb_id: str, as_dict: bool = False):
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
        if not as_dict:
            return movie.title
        return movie.dict()



    def get_recommendation(self, input_recommendation: InputRecommendation):
        input_service = InputService()

        is_valid = input_service.validate_input_data(input_recommendation)
        if not (is_valid):
            return {"status": "invalid input", "movies": {}}

        model = load_model()
        input_predict = map_input_recommendation_to_predict(input_recommendation)

        recommended = model.predict(input_predict)

        if len(recommended) == 0:
            return {"status": "no movie recommended", "movies": {}}
        
        recommended_ids = recommended["imdb_id"].tolist()
        movies = {}
        for imdb_id in recommended_ids:
            try:
                movie_info = self.get_movie_from_mongo(str(imdb_id), as_dict=True)
            except:
                movie_info = None
            movies[str(imdb_id)] = movie_info

        return {"status": "ok", "movies": movies}