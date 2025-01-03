
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

    book_path = "books/frankenstein.txt"
    book_text = read_book(book_path)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count(book_text)} words found in the document")

    # Getting dict of character frequency
    char_frequency_dict = char_frequency(book_text)

    # Building list of lists where inner lists are list[char, frequency]
    char_frequency_list = []
    for key in char_frequency_dict:
        if key.isalpha():
            temp_list = []
            temp_list.append(key)
            temp_list.append(char_frequency_dict[key])
        
            char_frequency_list.append(temp_list)

    # Sorting inner lists by frequency in descending order
    char_frequency_list.sort(key=lambda k : k[1], reverse=True)
    print()
    print()

    # Printing ordered frequency to console
    for char_count in char_frequency_list:
        print(f"The '{char_count[0]}' character was found {char_count[1]} times")
    
    print("--- End report ---")


main()