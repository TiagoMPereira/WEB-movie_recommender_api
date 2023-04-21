from dataclasses import dataclass
from pydantic import BaseModel, Field
from typing import List
import numpy as np


class InputRecommendation(BaseModel):
    genres: List[str]
    language: str
    runtime: float
    release_year: float