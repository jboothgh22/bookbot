# Read in frankenstein
# text

from stats import count_words, count_characters, sorted_list
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        txt = f.read()
    
    return txt

def main():
    fpathbase = "/home/jbplc/workspace/github.com/jboothgh22/bookbot/"
    
    if len(sys.argv) != 2:
        print(f"ERROR: You must input the location of the book to analyze.")
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    
    fbook = sys.argv[1]#"/books/frankenstein.txt"
    fpath = fpathbase + fbook
   
    the_text = get_book_text(fpath)

    n_words = count_words(the_text)

    # Determine the number of occurences of each letter
    char_count_dict = count_characters(the_text)

    # Sort the occurences into descending frequency as a list
    new_list = sorted_list(char_count_dict)

    print(f"============ BOOKBOT ============")
    print(f" Analyzing book found at {fbook}")
    print(f"---------Word Count--------------")
    print(f"Found {n_words} total words")
    print(f"---------Character Count --------")
    for d in new_list:
        print(f"{d["char"]}: {d["num"]}")

    return 0

if __name__ == '__main__':
    main()

