def read_book(file_name: str) -> str:
    with open(file=file_name) as f:
        content = f.read()
        f.close()
    return content


def counter(content: str) -> int:
    return len(content.split())


def count_letters(content: str) -> dict:
    count_dict = {}
    for char in content:
        try:
            save = char.lower()
        except:
            save = char
        if save not in count_dict:
            count_dict[save] = 0
        count_dict[save] += 1
    return count_dict


def takeSecond(elem: tuple) -> int:
    return elem[1]


def main():
    file_name = "./frankenstein.txt"
    content = read_book(file_name=file_name)
    num_of_words = counter(content)

    print(f"--- Begin report of books/{file_name} ---")
    print(f"{num_of_words} words found in the document\n")

    count_list = list(count_letters(content=content).items())
    count_list.sort(key=takeSecond, reverse=True)

    for item in count_list:
        if item[0].isalpha():
            print(f"The '{item[0]}' character was found {item[1]} times")
    print("--- End report ---")


main()
