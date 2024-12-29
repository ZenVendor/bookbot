def word_count(text):
    return len(text.split())


def character_count(text):
    chars = {}
    for char in text.lower():
        if char not in chars:
            chars[char] = 0

        chars[char] += 1

    return chars


def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()

    print(f"Words: {word_count(file_contents)}")
    chars = character_count(file_contents)
    for key in chars:
        print(f"{key}: {chars[key]}")



main()
