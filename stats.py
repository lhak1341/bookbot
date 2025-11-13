def get_num_words(text):
    return len(text.split())

def count_chars(text):
    result = {}
    for char in text:
        char = char.lower()
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    # sorted_result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
    return result

def sort_on(items):
    return items["num"]
