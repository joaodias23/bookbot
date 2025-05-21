def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    characters = {}
    for character in text:
        char = character.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sorted_dict(text):
    old_dict = char_count(text)
    dict_sorting = []
    for line in old_dict:
        new_dict = {}
        new_dict["char"] = line
        new_dict["num"] = old_dict[line]
        dict_sorting.append(new_dict)
    return dict_sorting