def number_of_words(book_string):
    number = (book_string.split())
    return len(number)

def symbol_count(book_string):
    characters = {}
    for word in book_string:
        lower_case = word.lower()
        if lower_case in characters:
            characters[lower_case] += 1
        else:
            characters[lower_case] = 1
    return characters
            