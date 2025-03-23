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
            
def sort_on(d):
    return d["num"]

def characters_to_sorted_list(num_char_dict):
    sorted_list = []
    for ch in num_char_dict:
        sorted_list.append({"char":ch, "num": num_char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list