import sys

if len(sys.argv) < 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
from stats import get_num_words, get_chars_dict, sorted_list

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words()} total words")
    print("--------- Character Count -------")
    
    for item in sorted_list():
        print(f"{item["char"]}: {item["count"]}")

    print("============= END ===============")
main()