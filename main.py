
def main():
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        num_words = word_count(text)
        lowercase_book = lowercase_words(text)
        lowercase_dict = letter_count(lowercase_book)
        sorted_dict = sort_dict(lowercase_dict)
        book_report(sorted_dict, num_words, book_path)

#needed to change something
def get_book_text(path):
        try:
                with open(path) as f:
                        return f.read()
        except FileNotFoundError:
                print(f"Error: The file at {path} was not found.")
        return ""
def word_count(book):
        words = book.split()
        return len(words)

def lowercase_words(book):
        lower_book = book.lower()
        return lower_book

def letter_count(book):
        letter_dict = {}
        for letter in book:
                if letter.isalpha():
                        if letter in letter_dict:
                                letter_dict[letter] += 1
                        else:
                                letter_dict[letter] = 1
        return letter_dict

def sort_dict(dict):
        sorted_letters = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        return sorted_letters

def book_report(bdict , num_words, path):
        print(f"--- Begin report of {path} ---")
        print(f"{num_words} words found in the document")
        for char , count in bdict:
                print(f"The character '{char}' was found {count} times")
        print("--- End report ---")
main()
