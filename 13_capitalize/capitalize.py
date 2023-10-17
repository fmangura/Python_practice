def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    # return "".join([letter.upper() if letter[0] else letter for letter in phrase])
    return phrase.capitalize()
    