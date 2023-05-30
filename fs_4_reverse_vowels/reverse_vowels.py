def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
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
    vowels = []
    vowel_indices = []

    for i, char in enumerate(s):
        if char.lower() in "aeiou":
            vowels.append(char)
            vowel_indices.append(i)
            
    vowels = vowels[::-1]

    for vowel, index in zip(vowels, vowel_indices):
        s = s[:index] + vowel + s[index + 1:]

    return s
            
            
print(reverse_vowels("Hello!"))
print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("aeiou"))
print(reverse_vowels("why try, shy fly?"))
    
    