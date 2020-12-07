def compute_ngram_frequency(text,n):
    """
    docstring
    """

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text_in_list = []

    lower_text = text.lower()
    ngram_frequency = dict()
    ngram_list = []
    ngram_counter = dict()

    for character in lower_text:
        if character in alphabet:
            text_in_list.append(character)

    counter = 1
    while counter <= n:
        temp_list = []
        for i in range(len(lower_text)+1):
            temp_list.append(lower_text[i:i+counter])

        ngram_list.append(temp_list)
        counter += 1
    
    for i in range(n):
        remove_unwanted_elements(ngram_list) 

    ngram_list_for_n = ngram_list[n-1]

    for element in ngram_list_for_n:
        if element not in ngram_counter:
            ngram_counter[element] = 1
        else:
            ngram_counter[element] += 1

    for ngram in ngram_counter:
        ngram_frequency[ngram] = ngram_counter[ngram]/len(ngram_list_for_n)

    return ngram_frequency


def remove_unwanted_elements(ngram_list):
    for lst in ngram_list:
        lenght_element = len(lst[0])
        for element in lst:
            if element == " " or " " in element:
                lst.remove(element)
            if len(element) != lenght_element:
                lst.remove(element)
    return ngram_list


