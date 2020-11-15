def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n+k) Runs through input list twice
    Memory usage: O(n+k) Uses two additional arrays, output and a count (k is maximum possible value in array)"""
    # Find range of given numbers (minimum and maximum integer values)
    output = list() * len(numbers)
    # Create list of counts with a slot for each number in input range
    count = [0 for each in range(max(numbers)+1)]

    # Loop over given numbers and increment each number's count
    for num in numbers:
        count[num] += 1
    # print(count)
    # Loop over counts and append that many numbers into output list
    for i, each in enumerate(count):
        for _ in range(each):
            output.append(i)
    return output

# Stretch: Improve this to mutate input instead of creating new output list
def counting_sort_mutated(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n+k) Runs through input list once and all possible values (count)
    Memory usage: O(k) Uses additional count array (which makes this one not stable)"""
    # Find range of given numbers (minimum and maximum integer values)
    # Create list of counts with a slot for each number in input range
    count = [0 for each in range(max(numbers)+1)]

    # Loop over given numbers and increment each number's count
    for num in numbers:
        count[num] += 1

    # Loop over counts and append that many numbers into output list
    j = 0
    for i, each in enumerate(count):
        while each > 0:
            numbers[j] = i
            each -= 1
            j += 1
    return numbers

#TODO: Write some test cases

if __name__ == "__main__":
    # numbers = [4,6,6,7,8,6,2,1,5,6,2,4,5,0,3]
    numbers = [1,0,3,1,3,1]
    print(numbers)
    print(counting_sort(numbers))
    print(counting_sort_mutated(numbers))