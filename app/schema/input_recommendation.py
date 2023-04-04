from dataclasses import dataclass
from pydantic import BaseModel, Field
from typing import List


class InputRecommendation(BaseModel):
    genders: List[str]
    runtime: float
    release_year: int
    language: str