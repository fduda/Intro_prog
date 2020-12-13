def compute_ngram_frequency(text, n):

    # list_of_ngrams(text, n) # input text, output ngram_list
    # remove_unwanted_characters(list_of_ngrams) 





    lower_text = text.lower()
    lower_text = lower_text.strip()
    ngram_list = []

    counter = 1
    while counter <= n:
        temp_list = []
        for i in range(len(lower_text)+1):
            temp_list.append(lower_text[i:i+counter])

        ngram_list.append(temp_list)
        counter += 1

    ngram_list = ngram_list[n-1]
    return ngram_list

# def remove_unwanted_characters(ngram_list):
#     unwanted_characters = [".", ",", "!", "?", " ", "\n"]
#     for ngram in ngram_list:
#         for character in ngram:
#             if character in unwanted_characters:
#                 ngram_list.remove(ngram)
#     return ngram_list

print(list_of_ngrams("banana pack", 2))