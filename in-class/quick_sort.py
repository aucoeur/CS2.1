def median(x, y, z):
    ''' Returns median of three numbers
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
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    
    # Choose a pivot
    p_index = median(low, high, len(items) // 2) # // int div, keeps only int

    # Move pivot to end
    # print(f'before {items}')
    items[p_index], items[high] = items[high], items[p_index]
    pivot = high
    start = low
    print(f'{items[pivot]} -- pivot to end {items}')

    # Loop through all items in range [low...high]
    for i in range(low, high):
        while items[low] <= items[pivot] and low < high:
            low += 1
        print(f'low {items[low]}')
        while items[high] >= items[pivot] and high > low:
            high -= 1
        print(f'high {items[high]}')
        # Move items less than pivot into front of range [low...p-1]
        # Move items greater than pivot into back of range [p+1...high]

        if low <= high:
            items[high], items[low] = items[low], items[high]
            print(f'{low, high}cross {items}')
    
    # Move pivot item into final position [p] and return index p
    items[pivot], items[low] = items[low], items[pivot]
    print(f'{items[pivot]} {pivot} pivot return {items}')
    return low

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]` around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Check if high and low range bounds have default values (not given)
    if low is None:
        low = 0
    if high is None:
        high = len(items) -1

    # Check if list or range is so small it's already sorted (base case)
    if low < high:
        # Partition items in-place around a pivot and get index of pivot
        pivot = partition(items, low, high)
        print(f'first partition {pivot}')
        # Sort each sublist range by recursively calling quick sort
        quick_sort(items, low, pivot-1)
        quick_sort(items, pivot+1, high)

if __name__ == "__main__":
    items = 'Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()
    # items = 'one fish two fish red fish blue fish'.split()
    # items = random_ints(10, 1, 20)
    print(items)
    quick_sort(items)
    print(items)