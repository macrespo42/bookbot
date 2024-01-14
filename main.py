def count_words_in_book(text: str) -> int:
    return len(text.split())


def count_letters_in_book(text: str) -> dict:
    letter_count = {}
    for letter in text.lower():
        if not letter_count.get(letter, None):
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    return letter_count


def read_book(path_to_book: str) -> str:
    with open(path_to_book, 'r') as f:
        return f.read()


def main() -> None:
    book = 'books/frankeinstein.txt'
    book_text = read_book(book)
    print(f"--- Begin report of {book} ---")
    print(f"{count_words_in_book(book_text)} words found in the document")
    print()
    letters_count = count_letters_in_book(book_text)
    sorted_letter = sorted(letters_count.items(), key=lambda x: x[1], reverse=True)
    for letter in sorted_letter:
        if letter[0].isalpha():
            print(f"the '{letter[0]}' character was found {letter[1]} times")
    print("--- end of report ---")


main()
