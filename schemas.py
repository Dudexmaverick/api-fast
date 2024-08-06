from enum import Enum
from pydantic import BaseModel


class GenreURLChoices(Enum):
    Rock = 'rock'
    MPB = 'mpb'
    Rock_nacional = 'rock nacional'

class Band(BaseModel):
    #
