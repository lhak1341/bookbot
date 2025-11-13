from stats import get_num_words, count_chars, sort_on

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    count_dict = count_chars(book_text)
    # count_dict.sort(reverse=True, key=sort_on)

    new_list = []
    for ch, n in count_dict.items():
        new_list.append({"char": ch, "num": n})
    new_list.sort(reverse=True, key=sort_on)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in new_list:
        if item["char"].isalpha():
          print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
