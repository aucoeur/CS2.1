#!python

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order, and return a new list containing all items in sorted order.
    Running time: O(n+m) because it goes through each item on both lists once
    Memory usage: O(n+m) auxiliary space because it merges the two lists into a  new list"""
    merged = []
    # Repeat until one list is empty
    while items1 or items2:
        if items1 and items2:
            # Find minimum item in both lists and append it to new list
            if items1[0] < items2[0]:
                num = items1.pop(0)
            else:
                num = items2.pop(0)
        # Append remaining items in non-empty list to new list
        else:
            if items1:
                num = items1.pop(0)
            if items2:
                num = items2.pop(0)
        merged.append(num)
    return merged

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n log n) In all cases because it always divides array in two halves and takes linear time to merge two halves
    Memory usage: O(n) auxiliary space because it splits the two lists into a  new list but doesn't need more than O(n) space at any given time"""
    # Check if list is so small it's already sorted (base case)
    if len(items) < 2:
        return items

    # Split items list into approximately equal halves
    mid = len(items) // 2 # // int division (rounds down)

    left = items[:mid]
    right = items[mid:]

    # Sort each half by recursively calling merge sort
    # Merge sorted halves into one list in sorted order
    items[:] = merge(merge_sort(left), merge_sort(right))
    return items[:]

def median(x, y, z):
    ''' Returns median of three numbers - O(1)
    '''
    if (x <= y <= z) or (z <= y <= x):
        return y
    elif (y <= x <= z) or (z <= x <= y):
        return x
    elif (x <= z <= y) or (y <= z <= x):
        return z
    
def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range `[low...high]` by choosing a pivot* from that range, moving pivot into index `p`, items less than pivot into range `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.

    * Pivot chosen by returning median index of items[0], items[mid_index] & items[-1]
    Running time: Avg: O(n) because partitioning requires going through the entire list once
    Memory usage: O(1) because it swaps in place"""
    
    # Choose a pivot
    p_index = median(low, high, len(items) // 2) # // int div, keeps only int

    # Move pivot to end
    items[p_index], items[high] = items[high], items[p_index]
    pivot = high


    # Loop through all items in range [low...high]
    for _ in range(low, high):
        while items[low] <= items[pivot] and low < high:
            low += 1
        
        while items[high] >= items[pivot] and high > low:
            high -= 1
        
        # Move items less than pivot into front of range [low...p-1]
        # Move items greater than pivot into back of range [p+1...high]

        if low <= high:
            items[high], items[low] = items[low], items[high]
    
    # Move pivot item into final position [p] and return index p
    items[pivot], items[low] = items[low], items[pivot]

    return low

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]` around a pivot item and recursively sorting each remaining sublist range.

    Best case running time: O(n log n) Partitioning takes O(n) and recursing on subarrays is O(log n)
    Worst case running time: O(n^2) when the pivot is unbalanced and on the far low/high ends, for median of three pivot, it would be terrible if the array was rotated/off by one
    Memory usage: O(log n) Because it uses two recursive calls. where each subarray is half the size of the one before"""
    # Check if high and low range bounds have default values (not given)
    if low is None:
        low = 0
    if high is None:
        high = len(items) -1

    # Check if list or range is so small it's already sorted (base case)
    if low < high:
        # Partition items in-place around a pivot and get index of pivot
        pivot = partition(items, low, high)

        # Sort each sublist range by recursively calling quick sort
        quick_sort(items, low, pivot-1)
        quick_sort(items, pivot+1, high)