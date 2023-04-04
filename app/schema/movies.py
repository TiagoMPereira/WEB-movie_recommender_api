from dataclasses import dataclass


@dataclass
class MovieSchema:
    genres: list
    release_year: int
    runtime: float
    vote_average: float
    overview: str
    title: str
    original_language: str
    popularity: float
    production_countries: list
    production_companies: list
    belongs_to_collection: str
    poster_path: str
    imdb_id: str
    tmdb_id: int
