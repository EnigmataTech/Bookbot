def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    #print(text)
    print(chars_dict)
    

def get_chars_dict(text):
    chars = {}
    for char in text:
        lower = char.lower()
        if lower in chars:
            chars[lower] += 1
        else:
            chars[lower] = 1
    return chars   
    
def get_num_words(text):
    words = text.split()
    return len(words)
    
def get_book_text(path):    
    with open(path) as f:
        return f.read()
    
main()