def words_number(text):
    text_list = text.split()
    return len(text_list)

def count_characters(text):
    letters = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }
    letters_list = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z',
    ]
    for c in text:
        lowercase_c = c.lower()
        if lowercase_c in letters_list:
            letters[lowercase_c] += 1
    for key in letters:
        print(f"The {key} character was found {letters[key]} times")
    

def main (path):
    with open(path) as f:
        file_contents = f.read()
        print(f"{words_number(file_contents)} words found in the document")
        count_characters(file_contents)

main("books/frankenstein.txt")