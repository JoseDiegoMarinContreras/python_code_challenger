def _flattening_dictionary_gen(data: dict, parent_key: str, sep: str) -> dict:
    for key, val in data.items():
        if isinstance(val, dict):
            yield from flattening_dictionary(val, parent_key + key + sep, sep).items()
        else:
            yield parent_key + key, val

def flattening_dictionary(data: dict, parent_key: str="", sep: str=". ") -> dict:
    return dict(_flattening_dictionary_gen(data, parent_key, sep))


value = {
    'a': 1,
    'c': {
        'a': 2,
        'b': {
            'x': 3,
            'y': 4,
            'z': 5
            }
        },
    'd': [6, 7, 8]
}

print(flattening_dictionary(value, sep="_"))
