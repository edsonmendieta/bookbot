
def read_book(filepath: str) -> str:

    with open("books/frankenstein.txt") as file_object:
        book_text = file_object.read()
        
        return book_text

def word_count(text: str) -> int:

    words_list = text.split()

    return len(words_list)     





def main():

    print(word_count(read_book("books/frankenstein.txt")))

main()