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
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) In all cases
    Memory usage: O(1) Because the sorting is done in-place"""
    
    # Repeat until all items are in sorted order
    for i in range(len(items)-1):
        # increments after each pass/sort
        min_index = i
        
        # Find minimum item in remaining unsorted items
        for j in range(i+1, len(items)-1):
            if items[j] < items[min_index]:
                min_index = j

        # Swap it with first unsorted item
        items[i], items[min_index] = items[min_index], items[i]


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: Worst/Avg O(n^2) when items are in opposite order or randomly scrambled Best O(n) when array is already sorted, outer loop runs n times but inner loop doesn't run at all
    Memory usage: O(1) because extra variable used"""
    # Repeat until all items are in sorted order
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1

        # Take first unsorted item
        while j >= 0 and key < items[j]:
            items[j+1] = items[j]
            j = j - 1
        # Insert it in sorted order in front of items
        items[j + 1] = key

if __name__ == "__main__":
    items = [2,3,4,8,7,5]
    print(bubble_sort(items))