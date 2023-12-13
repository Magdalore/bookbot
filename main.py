def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    print(f"{word_count} words found in the document")
    print()
    letter_results = list(letter_count.items())
    letter_results.sort()
    for l in letter_results:
        if l[0].isalpha():
            print(f"The letter '{l[0]}' appears {l[1]} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()    

def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letters = text.lower()
    letter_count = {}
    for letter in letters:
        letter_count[letter] = letter_count.get(letter, 0) + 1 # .get will return the value of the key, if the key does not exist it will return the default value .get(key, default)
    return letter_count
   

    

main()