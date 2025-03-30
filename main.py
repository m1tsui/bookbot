def main():
    filePath="books/frankenstein.txt"
    text = get_book_text(filePath)
    print(text)

def get_book_text(path):
    with open(path) as file:
        return file.read()
        



main()