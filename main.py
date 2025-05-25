import sys
from stats import count_words, count_char, sorted_list_of_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main(file_path):
    try:
        book = get_book_text(file_path)
        counted= count_words(book)
        characters = count_char(book)
        result = sorted_list_of_dict(characters)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}")
        print("----------- Word Count ----------")
        print(f"{counted}")
        print("--------- Character Count -------")
        for i in result:
            if i["char"].isalpha():
                print(f'{i["char"]}: {i["num"]}')
        print("============= END ===============")
    except Exception:
        sys.exit(1)
if len(sys.argv) == 2:
    print(f"Usage: python3 main.py {sys.argv[1]}")
    main(sys.argv[1])

else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
