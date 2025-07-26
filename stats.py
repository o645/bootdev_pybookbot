

def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_chars(text):
    char_dict : dict[str,int] = dict()
    for char in text:
        char_dict[char.lower()] = char_dict.get(char.lower(), 0) + 1
    return char_dict