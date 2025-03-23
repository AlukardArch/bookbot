from stats import number_of_words, symbol_count, characters_to_sorted_list

def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    words = number_of_words(book)
    symbols = symbol_count(book)
    chars_sorted = characters_to_sorted_list(symbols)
    print_report(book_path, words, chars_sorted)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents  

def print_report(book_path, words, chars_sorted_list):
    print("============== BOOKDROID ===============")
    print(f"Analyzing book found atr {book_path}...")
    print("------------- Word Count -------------")
    print(f"Found {words} total words")
    print("---------- Characted Count -----------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
        
    print("=========== USELESS KAPPA =============")
    
main()