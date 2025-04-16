import sys
from stats import get_word_num, character_counter, sorting

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents=f.read()
        return file_contents

def main():
    if len(sys.argv) == 2:
        filepath=sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text=get_book_text(filepath)
    word_numbers=get_word_num(text)
    character_count=character_counter(text)
    sorted_list=sorting(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_numbers} total words")
    print("--------- Character Count -------")
    for s in sorted_list:
        if s["name"].isalpha() is True:
            print(f"{s["name"]}: {s["num"]}")
    print("============= END ===============")
    
main()