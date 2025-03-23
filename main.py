from stats import number_of_words, symbol_count

def main():
    book = get_book_text("books/frankenstein.txt")
    words = number_of_words(book)
    symbols = symbol_count(book)
    print(f"{words} words found in the document")
    print(symbols)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents  

main()