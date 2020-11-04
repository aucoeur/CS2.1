def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n log n) In all cases because it always divides array in two halves and takes linear time to merge two halves
    Memory usage: O(n) auxiliary space because it merges the two lists into a  new list but doesn't need more than O(n) space at any given time"""
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
    # Check if list is so small it's already sorted (base case)
    if len(my_list) < 2:
        return my_list

    # Split items list into approximately equal halves
    mid = len(my_list) // 2
    left = my_list[:mid]
    right = my_list[mid:]

    # Sort each half by recursively calling merge sort
    # Merge sorted halves into one list in sorted order
    return merge(merge_sort(left), merge_sort(right))
        

my_list = [3, 6, 10, 1, 30, 29, 2]
merge_sort(my_list)
print(merge_sort(my_list))
# print(merge([3,4,5], [1, 8, 9]))