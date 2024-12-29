def get_book_contents(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def word_count(text):
    return len(text.split())


def character_count(text):
    chars = {}
    for char in text.lower():
        if char not in chars:
            chars[char] = 0

        chars[char] += 1

    return chars


def sort_by_key(dictionary, reverse=False):
    return dict(sorted(dictionary.items(), reverse=reverse))


def sort_by_value(dictionary, reverse=False):
    return dict(sorted(dictionary.items(), key=lambda kv: (kv[1], kv[0]), reverse=reverse))


def print_book_report(file_path):
    text = get_book_contents(file_path)
    print(f"--- Begin report for {file_path} ---")
    print(f"{word_count(text)} found in the document\n")

    char_dict = character_count(text)
    for char in sort_by_value(char_dict, reverse=True):
        if char.isalpha():
            print(f"The {char} character was found {char_dict[char]} times")

    print("\n--- End report ---")


def main():
    file_path = "books/frankenstein.txt"
    print_book_report(file_path)



main()
