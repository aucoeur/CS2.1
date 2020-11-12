def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
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
    return output[1:]
    # Stretch: Improve this to mutate input instead of creating new output list


    #TODO: Write some test cases

if __name__ == "__main__":
    numbers = [4,6,6,7,8,6,2,1,5,6,2,4,5,0,3]
    print(counting_sort(numbers))