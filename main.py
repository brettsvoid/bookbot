def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    counts = {}
    for c in text.lower():
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts


def character_dict_to_list(dict):
    characters = []
    for char in dict:
        if char.isalpha():
            num = dict[char]
            characters.append({"name": char, "num": num})
    return characters


def sort_on(dict):
    return dict["num"]


def read_file(path):
    with open(path) as f:
        return f.read()


def main():
    path_to_book = "books/frankenstein.txt"
    file_contents = read_file(path_to_book)
    num_words = count_words(file_contents)
    char_dict = count_characters(file_contents)
    char_list = character_dict_to_list(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {path_to_book} ---")
    print(f"{num_words} words found in the document\n")
    for item in char_list:
        name = item["name"]
        num = item["num"]
        print(f"The '{name}' character was found {num} times")
    print(f"--- End report ---")


main()
