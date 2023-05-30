from collections import Counter

def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    lst_dict =  Counter(lst)
    
    return lst_dict[search_term]


print(frequency([1, 4, 3, 4, 4], 4))

print(frequency([1, 4, 3], 7))