names = [ {'first': 'Ada', 'last': 'Lovelace'}, {'first': 'Grace', 'last': 'Hopper'}, {'first': 'Luis', 'last': 'Mendoza'} ]


def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    # list_of_names = []
    # for person in people:
    #     first_name = person.get("first")
    #     last_name = person.get("last")
    #     list_of_names.append(f"{first_name} {last_name}") 
    # return list_of_names
    
    # More concise solution below, still 0(n) time complexity

    return [f"{person['first']} {person['last']}" for person in people]


print(extract_full_names(names))