def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    if parens.count('(') == parens.count(')'):
        for char in parens:
            if char == '(' and parens.index(char) <= len(parens)-1/2:
                return True
            elif char == ')' and parens.index(char) >= len(parens)-1/2:
                return True
            else:
                return False
    else:
        return False

