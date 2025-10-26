import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_content = f.read()
        return book_content

path_to_file = sys.argv[1]

def get_num_words():
    text = get_book_text(path_to_file)
    words_count = text.split()
    return len(words_count)

def get_chars_dict():
    text = get_book_text(path_to_file).lower()
    chars_dict = {}
    
    for t in text:
        if t in chars_dict:
            chars_dict[t] += 1
        else:
            chars_dict[t] = 1
    return chars_dict

def sorted_list():
    list_of_dicts = []
    chars_dict = get_chars_dict()

    for g in chars_dict:
        temp_dict = {}
        temp_dict["char"] = g
        temp_dict["count"] = chars_dict[g]
        list_of_dicts.append(temp_dict)
    
    def sort_on(list_of_dicts):
        return list_of_dicts["count"]
    
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts