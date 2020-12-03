def compute_ngram_frequency(text, n):
    """
    docstring
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    lower_text = text.lower()
    ngram_dict = dict()
    text_in_list = []
    letter_counter = dict()


    for character in lower_text:
        if character in alphabet:
            text_in_list.append(character)
    
    for letter in text_in_list:
        if letter not in letter_counter:
            letter_counter[letter] = 1
        else:
            letter_counter[letter] += 1
    
    for letter in letter_counter:
        ngram_dict[letter] = letter_counter[letter]/len(text_in_list)


    return ngram_dict


print(compute_ngram_frequency("banana pack", n=1))