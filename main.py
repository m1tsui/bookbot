import sys
from stats import count_words, count_letters

raamat_adress = "./books/raamat.txt"
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book = sys.argv[1]


def main(book):
    words = count_words(book)
    letters = count_letters(book)
    letters = "\n".join(f"{k}: {v}" for k, v in letters.items() if k.isalpha())
    print (f"""============ BOOKBOT ============
Analyzing book found at {book}...
----------- Word Count ----------
{words}
--------- Character Count -------
{letters}
============= END ===============""")


if __name__ == "__main__":
    main(book)