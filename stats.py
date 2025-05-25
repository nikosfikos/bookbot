def count_words(text):
    counter = 0
    list_of_words = text.split()
    for i in list_of_words:
        counter += 1
    return f"Found {counter} total words"

def count_char(text):
    chars = {}
    for i in text:
        i = i.lower()
        if i not in chars:
            chars[i] = 1
        else:
            chars[i] +=1
    return chars

def sorted_list_of_dict(chars):
    list = []
    for i in chars:
        list.append({"char" : i, "num": chars[i]})

    def sort_on(dict):
        return dict["num"]

    list.sort(reverse=True, key=sort_on)

    return list
