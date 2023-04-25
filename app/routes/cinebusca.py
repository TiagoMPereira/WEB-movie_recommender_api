from fastapi import APIRouter
from services.movies import MovieService
from schema.input_recommendation import InputRecommendation

router = APIRouter()


@router.get("/movie/{id_movie}")
def get_movie(id_movie: str):
    movie_service = MovieService()
    movie = movie_service.get_movie_from_mongo(id_movie)
    return movie


@router.post("/recommend")
def recommend_movie(input_recommendation: InputRecommendation):
    movie_service = MovieService()
    recommendation = movie_service.get_recommendation(input_recommendation)
    result = recommendation | {"input": input_recommendation}
    return result