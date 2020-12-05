def compute_ngram_frequency(text,n):
    """
    docstring
    """

    lower_text = text.lower()
    ngram_dict = dict()
    ngram_list = []
    letter_counter = dict()

    counter1 = 1
    counter2 = 0
    print(lower_text[0:1])
    while counter1 <= n:
        for i in range(len(lower_text)+1):
            ngram_list.append(lower_text[i:i+counter1])

        for not_wanted in ngram_list:
            if not_wanted == "" or not_wanted == " ":
                ngram_list.remove(not_wanted)
            
        counter1 += 1
            

        
    
    print(ngram_list)


compute_ngram_frequency("banana pack", 3)
