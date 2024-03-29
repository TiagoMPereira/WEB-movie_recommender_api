from schema.input_recommendation import InputRecommendation


class InputService():

    def _validate_genres(self, genres: list):
        return not (len(genres) == 0)
    
    def _validate_runtime(self, runtime: float):
        return not (runtime is None)

    def _validate_release_year(self, release_year: int):
        return not (release_year is None)

    def _validate_language(self, language: str):
        return not (language is None or language == "")

    def validate_input_data(self, input_recommendation: InputRecommendation):
        is_genre_valid = self._validate_genres(input_recommendation.genres)
        is_runtime_valid = self._validate_runtime(input_recommendation.runtime)
        is_release_year_valid = self._validate_release_year(input_recommendation.release_year)
        is_language_valid = self._validate_language(input_recommendation.language)

        is_valid_input = (int(is_genre_valid) + int(is_runtime_valid) + int(is_release_year_valid) + int(is_language_valid)) >= 3
        return is_valid_input
        
