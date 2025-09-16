
from typing import List, Union

def merge_sort(items: List[Union[int, str]]) -> List[Union[int, str]]:
    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left: List, right: List) -> List:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def bubble_sort(items: List[Union[int, str]]) -> List[Union[int, str]]:
    n = len(items)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if items[j] > items[j+1] :
                items[j], items[j+1] = items[j+1], items[j]
    return items

def quick_sort(items: List[Union[int, str]]) -> List[Union[int, str]]:
    if len(items) <= 1:
        return items
    else:
        pivot = items[len(items) // 2]
        left = [x for x in items if x < pivot]
        middle = [x for x in items if x == pivot]
        right = [x for x in items if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
