def count_words(text):
    return len(text.split())
 
def count_letter_in_text(text):
    existing_letter = {}
    text_lower = text.lower()
    for letter in text_lower:
        if letter in existing_letter:
            existing_letter[letter] +=1
        else:
            existing_letter[letter] = 1
    return existing_letter
    #print(existing_letter)

def sort (input_dict):
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict
