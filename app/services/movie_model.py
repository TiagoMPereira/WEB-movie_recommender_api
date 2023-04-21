from movie_engine.models.recommender import MovieModel
from movie_engine.models.DAO import InputPredict
from schema.input_recommendation import InputRecommendation
from utils.settings import Settings
import numpy as np


def load_model(path: str = None) -> MovieModel:
    if not path:
        path = Settings().movie_path
    return MovieModel.load(path)

def map_input_recommendation_to_predict(
    input_recommendation: InputRecommendation
) -> InputPredict:
    
    input_predict = InputPredict()

    # genres
    genre_to_predict = []
    genre_input = input_recommendation.genres
    genres_max_size = 3
    for i in range(genres_max_size):
        if i < len(genre_input):
            genre_to_predict.append(genre_input[i])
        else:
            genre_to_predict.append(None)

    genre1, genre2, genre3 = genre_to_predict

    input_predict.genre1 = genre1 
    input_predict.genre2 = genre2
    input_predict.genre3 = genre3

    if input_recommendation.release_year == 0.0:
        input_predict.release_year = 2017           # Most recent
    else:
        input_predict.release_year = input_recommendation.release_year

    if input_recommendation.runtime == 0.0:
        input_predict.runtime = 100                 # average
    else:
        input_predict.runtime = input_recommendation.runtime

    input_predict.language = input_recommendation.language

    return input_predict
    