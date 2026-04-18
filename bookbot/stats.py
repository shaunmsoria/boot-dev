def count_book_char(book_content):
    char_count = {}
    for char in book_content.lower():
        if char_count.get(char) == None:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_on(items):
    return items["num"]

def sorted_dictionaries(char_count):
    list_dictionaries = []
    for char in char_count:
        list_dictionaries.append({"char": char, "num": char_count[char]})
    list_dictionaries.sort(reverse=True, key=sort_on)
    return list_dictionaries


def get_book_text(path: str):
    with open(path) as book:
        book_content = book.read()
        word_count = len(book_content.split())
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        count_char = count_book_char(book_content)
        dictionaries = sorted_dictionaries(count_char)
        print("--------- Character Count -------")
        for char in dictionaries:
            if char["char"].isalpha() == True:
                character = char["char"]
                number = char["num"]
                print(f"{character}: {number}")
        print("============= END ===============")
        return None