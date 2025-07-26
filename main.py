def get_book_text(filename):
    with open(filename) as f:
        filecontents = f.read()
        return str(filecontents)

def number_of_words(text):
    words = text.split()
    return len(words)


def main():
    content = get_book_text("./books/frankenstein.txt")
    print(f'{number_of_words(content)} words found in the document')

main()