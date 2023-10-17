def list_check(lsts):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for lst in lsts:
        if isinstance(lst, list) == False:
            return False
        else:
            continue
    return True