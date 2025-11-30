import sys
from stats import num_of_words, sort_characters, count_characters


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = get_book_text(sys.argv[1])
        num_words = num_of_words(book)
        dictionary = count_characters(book)
        sorted = sort_characters(dictionary)
        print("============ BOOKBOT ============")
        print(f"Analzying book fount as {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char in sorted:
            print(f"{char}: {sorted[char]}")
        print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


main()
