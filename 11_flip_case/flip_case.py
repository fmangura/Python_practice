def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped = []

    for letter in phrase:
        if letter.upper() == to_swap.upper():
            if letter == letter.upper():
                swapped.append(letter.lower())
            else:
                swapped.append(letter.upper())
        else:
            swapped.append(letter)
    return "".join(swapped)