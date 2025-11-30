def num_of_words(file_contents):
    word = []
    word = file_contents.split()
    return len(word)


def count_characters(file_contents):
    text = file_contents.lower().split()
    characters = {}
    for word in text:
        for char in word:
            if char.isalpha():
                if char in characters:
                    characters[char] += 1
                else:
                    characters[char] = 1
    return characters


def sort_characters(dictionaries):
    sorted_dict = dict(
        sorted(dictionaries.items(), reverse=True, key=lambda item: item[1])
    )
    return sorted_dict
