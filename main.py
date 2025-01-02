
def read_book(filepath: str) -> str:

    with open(filepath) as file_object:
        book_text = file_object.read()
        
        return book_text

def word_count(text: str) -> int:

    words_list = text.split()

    return len(words_list)     

def char_frequency(text: str) -> dict:

    frequency_dict = {}

    lowercase_string = text.lower()
    no_white_space_string = lowercase_string.replace(" ", "")

    for char in no_white_space_string:
        if char not in frequency_dict:
            frequency_dict[char] = 1
        else:
            frequency_dict[char] += 1
    
    return frequency_dict


def main():

    print(char_frequency(read_book("books/frankenstein.txt")))

main()