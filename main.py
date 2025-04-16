from stats import get_word_num, character_counter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents=f.read()
        return file_contents

def main():
    filepath="/home/alfred/workplace/github.com/lwc49/bookbot/books/frankenstein.txt"
    text=get_book_text(filepath)
    word_numbers=get_word_num(text)
    character_count=character_counter(text)
    print(f"{word_numbers} words found in the document")
    print(character_count)

main()