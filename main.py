from stats import number_of_words, number_of_chars

def get_book_text(filename):
    with open(filename) as f:
        filecontents = f.read()
        return str(filecontents)

def main():
    content = get_book_text("./books/frankenstein.txt")
    print(f'{number_of_words(content)} words found in the document')
    print(number_of_chars(content))
main()