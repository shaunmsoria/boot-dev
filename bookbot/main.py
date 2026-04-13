import sys
from stats import get_book_text

def main():
    arguments = sys.argv
    if (len(arguments) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        get_book_text(arguments[1])

main()

