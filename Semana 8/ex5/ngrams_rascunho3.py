import copy

def list_of_ngrams(text, n):
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

def remove_unwanted_characters(ngram_list):
    unwanted_characters = [".", ",", "!", "?", " ", "\n"]
    ngram_list_copy = copy.deepcopy(ngram_list)
    ngram_lenght = len(ngram_list_copy[0])
    for ngram in ngram_list_copy:
        if len(ngram) != ngram_lenght:
            ngram_list.remove(ngram)
        for character in ngram:
            if character in unwanted_characters:
                ngram_list.remove(ngram)
                break
            
    return ngram_list

 

f = open("english_1.txt", "r")
text = f.read()
f.close()

ngrams_text = list_of_ngrams(text,2)

print(remove_unwanted_characters(ngrams_text))