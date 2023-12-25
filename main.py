def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    all_lower = set_all_to_lower(text)
    char_count = dict_count_all_chars(all_lower)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    
    char_count_list = list(char_count)
    char_count_list.sort()
    for i in range(0, len(char_count_list)):
       if char_count_list[i].isalpha():
           print(f"The {char_count_list[i]} character ws found {char_count[char_count_list[i]]} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def set_all_to_lower(the_string):
    return the_string.lower()

def dict_count_all_chars(the_string):
    char_count = dict()
    for i in range(0, len(the_string)):
        if the_string[i] in char_count:
            char_count[the_string[i]] += 1
        else:
            char_count[the_string[i]] = 1
    return char_count
    

def nice_print_char_count(char_count):
    char_count_list = list(char_count)
    char_count_list.sort()
    for i in range(0, len(char_count_list)):
       if char_count_list[i].isalpha():
           print(f"The {char_count_list[i]} character ws found {char_count[char_count_list[i]]} times")
    

main()