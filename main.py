
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    char_stats = letter_count(text)
    print_report(char_stats, book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    return len(text.split())

def sort_on(dict):
    return dict["count"]

def letter_count(text):
    stats = {}
    list_stats = []
    for c in text.lower():
        if c in stats:
            stats[c] += 1
        else:
            stats[c] = 1
    for key in stats:
        if key >= 'a' and key <= 'z':
            list_stats.append({"char": key, "count": stats[key]})
    list_stats.sort(reverse=True,key=sort_on)
    return list_stats

def print_report(char_stats, book_path):
    sum = 0
    for s in char_stats:
        sum += s["count"] 
    print(f"--- Begin report of {book_path} ---")
    print(f"{sum} words found in the document")
    print("")
    for s in char_stats:
        print(f"The '{s["char"]}' character was found {s["count"]} times")
    print("--- End report ---")

main()