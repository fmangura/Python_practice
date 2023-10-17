def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    list1 = list(f'{num1}')
    list2 = list(f'{num2}')
    return {num:list1.count(num) for num in list1} == {num:list2.count(num) for num in list2}
    return check1 == check2
