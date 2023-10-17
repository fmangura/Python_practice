def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    list_s = list(s)
    rev_idx = 0
    answer = []
    vowels = [vowel for vowel in list_s[::-1] if vowel.lower() in 'aeiou']
    
    for i in range(len(list_s)):
        if list_s[i].lower() in 'aeiou':
            list_s[i] = vowels[rev_idx]
            answer.append(list_s[i])
            rev_idx += 1
        else:
            answer.append(list_s[i])

    return ''.join(answer)
    
    
    