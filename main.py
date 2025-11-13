import sys
from stats import get_num_words, count_chars, sort_on

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    try:
        with open(book_path, "r", encoding="utf-8") as f:
            book_text = f.read()
    except FileNotFoundError:
        print(f"File not found: {book_path}")
        sys.exit(1)
    num_words = get_num_words(book_text)
    count_dict = count_chars(book_text)

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
