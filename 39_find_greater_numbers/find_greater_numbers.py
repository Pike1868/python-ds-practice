def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
        
        
        # Using enumerate() we can count the number of times a number is followed by a greater number by returning True for each time the condition is met. Then adding up how many times we returned True.
    """
   
    return sum(num < next_num for count, num in enumerate(nums) for next_num in nums[count:])
    

print(find_greater_numbers([1, 2, 3]))
print(find_greater_numbers([6, 1, 2, 7]))
print(find_greater_numbers([5, 4, 3, 2, 1]))
print(find_greater_numbers([]))