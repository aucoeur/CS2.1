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

def merge_sort(my_list):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n log n) In all cases because it always divides array in two halves and takes linear time to merge two halves
    Memory usage: O(n) auxiliary space because it splits the two lists into a  new list but doesn't need more than O(n) space at any given time"""
    # Check if list is so small it's already sorted (base case)
    if len(my_list) < 2:
        return my_list

    # Split items list into approximately equal halves
    
    # // int division (rounds down)
    mid = len(my_list) // 2

    left = my_list[:mid]
    right = my_list[mid:]

    # Sort each half by recursively calling merge sort
    # Merge sorted halves into one list in sorted order
    return merge(merge_sort(left), merge_sort(right))

def median(x, y, z):
    pass

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot* from that range, moving pivot into index `p`, items less than pivot into range `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.

    * Pivot chosen by returning median value of items[0], items[mid_index] & items[-1]
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Choose a pivot
    # mid = len(items) // 2



    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]` around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort