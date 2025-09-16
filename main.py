
from fastapi import FastAPI, HTTPException
from models.schemas import SortRequest, SortResponse
from sorting.algorithms import merge_sort, bubble_sort, quick_sort
import time
from typing import Callable, List, Union

app = FastAPI(
    title="Sorting Service API",
    description="An API to sort lists of integers or strings using different algorithms.",
    version="1.0.0",
)

def perform_sort(algorithm: Callable[[List[Union[int, str]]], List[Union[int, str]]], data: SortRequest) -> SortResponse:
    """Helper function to time and execute a sorting algorithm."""
    start_time = time.time()
    
    # Check for mixed types (e.g., list of strings and integers)
    if len(data.items) > 1:
        first_item_type = type(data.items[0])
        if not all(isinstance(item, first_item_type) for item in data.items):
            raise HTTPException(
                status_code=400,
                detail="Mixed types in the list are not allowed. All items must be either integers or strings."
            )
            
    sorted_list = algorithm(data.items)
    end_time = time.time()
    time_taken = end_time - start_time
    return SortResponse(sorted_items=sorted_list, time_taken=time_taken)

@app.post("/sort/merge", response_model=SortResponse, summary="Sort with Merge Sort")
async def sort_merge(data: SortRequest):
    """
    Sorts a list of items using the **Merge Sort** algorithm.
    - **Best Case:** O(n log n)
    - **Average Case:** O(n log n)
    - **Worst Case:** O(n log n)
    """
    return perform_sort(merge_sort, data)

@app.post("/sort/bubble", response_model=SortResponse, summary="Sort with Bubble Sort")
async def sort_bubble(data: SortRequest):
    """
    Sorts a list of items using the **Bubble Sort** algorithm.
    - **Best Case:** O(n)
    - **Average Case:** O(n^2)
    - **Worst Case:** O(n^2)
    """
    return perform_sort(bubble_sort, data)

@app.post("/sort/quick", response_model=SortResponse, summary="Sort with Quick Sort")
async def sort_quick(data: SortRequest):
    """
    Sorts a list of items using the **Quick Sort** algorithm.
    - **Best Case:** O(n log n)
    - **Average Case:** O(n log n)
    - **Worst Case:** O(n^2)
    """
    return perform_sort(quick_sort, data)

@app.get("/", summary="Health Check")
async def read_root():
    """Health check endpoint to ensure the service is running."""
    return {"status": "ok"}
