def search(phrase: str, letters: str='aeiou'):
    return set(letters).intersection(set(phrase))