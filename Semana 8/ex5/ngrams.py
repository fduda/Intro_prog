import copy

def list_of_ngrams(text, n):
    lower_text = text.lower()
    lower_text = lower_text.strip()
    ngram_list = []
    characters_list = []

    for character in lower_text:
        characters_list.append(character)

    remove_unwanted_characters(characters_list)

    
    counter = 1
    while counter <= n:
        temp_list = []
        for i in range(len(characters_list)+1):
            temp_list.append(characters_list[i:i+counter])
        
        ngram_list.append(temp_list)
        counter += 1
    ngram_list = ngram_list[n-1]

    remove_unwanted_ngrams(ngram_list)
    return ngram_list



def remove_unwanted_characters(characters_list):
    unwanted_characters = [".", ",", "!", "?", "\n"]
    characters_list_copy = copy.deepcopy(characters_list)

    for character in characters_list_copy:
        if character in unwanted_characters:
            characters_list.remove(character)


    return characters_list

def remove_unwanted_ngrams(ngram_list):
    ngram_list_copy = copy.deepcopy(ngram_list)
    
    ngram_lenght = len(ngram_list[0])
    for ngram in ngram_list_copy:
        for character in ngram:
            try:
                if character == " ":
                    ngram_list.remove(ngram)
            except:
                pass
        if len(ngram) != ngram_lenght:
            try:
                ngram_list.remove(ngram)
            except:
                pass
    return ngram_list



def compute_ngram_frequency(text,n):

    ngram_counter = dict()
    ngram_frequency = dict()

    ngram_list = list_of_ngrams(text,n)
    
    for ngram in ngram_list:
        joint_ngram = "".join(ngram)
        if joint_ngram not in ngram_counter:
            ngram_counter[joint_ngram] = 1
        else:
            ngram_counter[joint_ngram] +=1

    for ngram in ngram_counter:
        ngram_frequency[ngram] = ngram_counter[ngram]/len(ngram_list)
    

    return ngram_frequency


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
        f.write(ngram_dict_to_string(element))
        f.write("\n")
    f.close()


def load_list_of_ngram_dicts(filename):
    f = open(filename, "r")
    lines = f.readlines()
    list_of_dicts = []

    for line in lines:
        list_of_dicts.append(string_to_ngram_dict(line))

    f.close()
    return list_of_dicts

