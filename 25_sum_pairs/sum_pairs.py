def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    # take each number > add one by one > find what equals the target > find the quickest answer
    li = {}
    for num in nums:
        for el in nums[nums.index(num)+1:]: 
            if el + num == goal:
                if num > el:
                    li[f'{num - el}'] = (num, el)
                else:
                    li[f'{el - num}'] = (num, el)
                    
    if li == {}:
        return ()
    else:
        return sorted(li.values())[0]
        
#     least_pairs(sample_tuple)


# def least_pairs(list_tuples):
            
    # for num in nums:
    #     [nums[nums.index(num)+1:] for el in nums[nums.index(num)+1:] if el + num == goal]
           
    
    # for num in nums.sort():
    #     for el in nums[nums.index(num)+1:]:
    #         if num + el == goal:
    #             print(len(nums[nums.index(num)+1:]))