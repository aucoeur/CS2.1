#!python

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) linear  because passes through list once 
    Memory usage: O(n) linear because iterates through original list """
    # Check that all adjacent items are in order, return early if so
    for index, item in enumerate(items[:-1]):
        if item > items[index+1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n^2) Worst/avg case O(n) best case items already sorted
    Memory usage: O(1) because sorting occurs in-place"""
    unsorted = True

    # Repeat until all items are in sorted order
    while unsorted:
        # set to False, if swap occurs, sets back to True
        unsorted = False
    
        for index in range(len(items)-1):
            if items[index] > items[index+1]:
                # Swap adjacent items that are out of order
                items[index], items[index+1] = items[index+1], items[index]
                unsorted = True

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) In all cases
    Memory usage: O(1) Because the sorting is done in-place"""

    # Selection sort works by finding and placing minimum items, so for each pass, the min index is set to i
    for i in range(len(items)):
        min_index = i
        
        # Find minimum item in remaining unsorted items
        for j in range(i+1, len(items)):
            if items[j] < items[min_index]:
                # set new min to j
                min_index = j

        if min_index != i:
            # Swap it with first unsorted item
            items[i], items[min_index] = items[min_index], items[i]
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: 
        - Worst/Avg: O(n^2) when items are in reverse sorted order or randomly scrambled 
        - Best: O(n) when current value is > then precending value, insertion is O(1) constant time (outer loop runs n times but inner loop doesn't run at all) or if array is already sorted
    Memory usage: O(1), extra variable used"""

    # Set sorted subarray starting at index 0, unsorted subarray starting at index 1
    for i in range(1, len(items)):
        # Take first unsorted item
        current = items[i]
        previous = i - 1

        # Exits when previous = -1 or if current > preceding value
        while previous >= 0 and current < items[previous]:
            # slide sorted value one index to the right
            items[previous+1] = items[previous]
            # move sorted index pointer back one to evaluate if current < precendin prev 
            previous = previous - 1
            
        # Insert current in sorted order in front of previous item pointer
        items[previous + 1] = current
    return items

if __name__ == "__main__":
    items = [3,2,8,6,4,1]
    print(items)
    print(selection_sort(items))