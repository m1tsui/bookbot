import sys
from stats import count_words, sort, count_letter_in_text

global file_path

if len(sys.argv) == 2:
    file_path = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as file:
        return file.read()

def main():
    text = get_book_text(file_path)
    sum = count_words(text)
    letters_count = count_letter_in_text(text)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {file_path}...\n----------- Word Count ----------")
    print(f"Found {sum} total words")
    print("--------- Character Count -------")
    sorted_dict = sort(letters_count)
    for x in sorted_dict:
        alpha = x.isalpha()
        if alpha: 
            print ("{}: {}".format(x, sorted_dict[x]))
    print("============= END ===============")


main() 