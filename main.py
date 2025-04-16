from stats import get_word_num, character_counter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents=f.read()
        return file_contents

def main():
    filepath="/home/alfred/workplace/github.com/lwc49/bookbot/books/frankenstein.txt"
    print(f"{get_word_num(filepath)} words found in the document")
    print(character_counter(filepath))

main()