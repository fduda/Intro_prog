def compute_ngram_frequency(text,n):
    """
    docstring
    """

    alphabet_with_space= "abcdefghijklmnopqrstuvwxyz"

    lower_text = text.lower()
    ngram_frequency = dict()
    ngram_list = []
    ngram_counter = dict()

    counter = 1
    while counter <= n:
        temp_list = []
        for i in range(len(lower_text)+1):
            temp_list.append(lower_text[i:i+counter])

        ngram_list.append(temp_list)
        counter += 1
    
    for i in range(n+1):
        remove_unwanted_characters(ngram_list) 

    ngram_list_for_n = ngram_list[n-1]

    for element in ngram_list_for_n:
        if element not in ngram_counter:
            ngram_counter[element] = 1
        else:
            ngram_counter[element] += 1

    for ngram in ngram_counter:
        ngram_frequency[ngram] = ngram_counter[ngram]/len(ngram_list_for_n)

    return ngram_frequency



def remove_unwanted_characters(ngram_list):
    unwanted_characters = [".", ",", "!", "?", " "]
    for lst in ngram_list:
        element_lenght = len(lst[0])
        for element in lst:
            for character in unwanted_characters:
                if character in element:
                    lst.remove(element)
                    break
                elif element == "":
                    lst.remove(element)
                    break
                elif len(element) != element_lenght:
                    lst.remove(element)
                    break

    return ngram_list

def compute_ngrams_frequency(text,k):
    list_of_frequencies = []
    for i in range(1,k+1):
        list_of_frequencies.append(compute_ngram_frequency(text,i))
    return list_of_frequencies

def ngram_dict_to_string(ngram_dict):
    list_from_dict = []
    for key, value in ngram_dict.items():
        string = "{}:{}".format(key,value)
        list_from_dict.append(string)
    string_from_dict = " ".join(list_from_dict)

    return string_from_dict

def string_to_ngram_dict(string):
    string_to_list = string.split(" ")
    ngram_dict = dict()
    for element in string_to_list:
        element_list = element.split(":")
        ngram_dict[element_list[0]]=float(element_list[1])
    return ngram_dict

def write_list_of_ngram_dicts(list_of_dicts, filename):
    f = open(filename, "w")
    for element in list_of_dicts:
        f.write(str(element))
        f.write("\n")
    f.close()
        
# write_list_of_ngram_dicts([{'a': 1, 'b': 2}, {'aa': 2, 'bb': 3}], "check.txt")

    