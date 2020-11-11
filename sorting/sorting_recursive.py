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
    
    # // int division (rounds down)
    mid = len(items) // 2

    left = items[:mid]
    right = items[mid:]

    # Sort each half by recursively calling merge sort
    # Merge sorted halves into one list in sorted order
    items[:] = merge(merge_sort(left), merge_sort(right))
    return items[:]
def median(x, y, z):
    ''' Returns median of three numbers
    '''
    if (x < y < z) or (z < y < x):
        return y
    elif (y < x < z) or (z < x < y):
        return x
    elif (x < z < y) or (y < z < x):
        return z
    

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range `[low...high]` by choosing a pivot* from that range, moving pivot into index `p`, items less than pivot into range `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.

    * Pivot chosen by returning median index of items[0], items[mid_index] & items[-1]
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Choose a pivot
    mid = len(items) // 2
    pivot = median(low, high, mid)

    # Move pivot to end
    items[pivot], items[high] = items[high], items[pivot]

    # Loop through all items in range [low...high]
    for i in range(low, high):
        while items[low] < items[pivot] and low < high:
            low += 1
        while items[high] > items[pivot] and high > low:
            high -= 1
        # Move items less than pivot into front of range [low...p-1]
        # Move items greater than pivot into back of range [p+1...high]
        if high < low:
            items[high], items[low] = items[low], items[high]
        
    # Move pivot item into final position [p] and return index p
    items[pivot], items[low] = items[low], items[pivot]
    return pivot

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]` around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Check if high and low range bounds have default values (not given)
    if low is None:
        low = 0
    if high is None:
        high = len(items) - 1

    # Check if list or range is so small it's already sorted (base case)
    if len(items) == 1:
        return
    # Partition items in-place around a pivot and get index of pivot
    pivot = partition(items, low, high)
    # Sort each sublist range by recursively calling quick sort
    quick_sort(items, low, pivot)
    quick_sort(items, pivot, high)
    