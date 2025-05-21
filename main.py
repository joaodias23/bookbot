import sys
from stats import word_count
from stats import char_count
from stats import sorted_dict

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    sys.argv[1]

file_path = sys.argv[1]

def get_book_text(file_path):
    with open(file_path, 'r') as f:
        file_contents = f.read()
    return file_contents

def main():
    relative_path = file_path
    entire_contents = get_book_text(relative_path)
    return entire_contents

with open(file_path, "r") as f:
    book_text = f.read()

num_words = word_count(book_text)
num_char = char_count(book_text)
sort_dict = sorted_dict(book_text)
def sort_on(dict):
    return dict["num"]

sort_dict.sort(reverse=True, key=sort_on)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {file_path}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
for char_dict in sort_dict:
    if char_dict["char"].isalpha():
        print(f"{char_dict['char']}: {char_dict['num']}")
print("============= END ===============")