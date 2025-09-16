
from pydantic import BaseModel, Field, conlist
from typing import List, Union, Any

class SortRequest(BaseModel):
    items: conlist(Union[int, str], min_length=1, max_length=1000) = Field(
        ...,
        description="A list of integers or strings to be sorted. The list must contain between 1 and 1000 items."
    )

class SortResponse(BaseModel):
    sorted_items: List[Union[int, str]]
    time_taken: float
