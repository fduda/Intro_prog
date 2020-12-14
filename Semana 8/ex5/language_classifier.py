import ngrams as ng
import os

def build_language_model(language1_filename, language2_filename, k):

    final_list = []

    file1 = open(language1_filename, "r")
    text1 = file1.read()
    file1.close()
    final_list.append(ng.compute_ngrams_frequency(text1, k))

    file2 = open(language2_filename, "r")
    text2 = file2.read()
    file2.close()

    final_list.append(ng.compute_ngrams_frequency(text2, k))

    path_file1 = os.path.isfile(language1_filename)
    path_file2 = os.path.isfile(language2_filename)

    if path_file1 == False or path_file2 == False:
        return None

    if text1 == "" or text2 == "":
        return None  

    return final_list

def compute_ngram_distance(dict1, dict2):

    distance_between_ngram = []

    set_dict1 = set(key for key in dict1)
    set_dict2 = set(key for key in dict2)
    
    ngram_set = set_dict1.union(set_dict2)

    for element in ngram_set:
        if element in dict1 and element in dict2:
            distance_between_ngram.append(abs(dict1[element]-dict2[element]))
        elif element not in dict1:
            distance_between_ngram.append(dict2[element])
        elif element not in dict2:
            distance_between_ngram.append(dict1[element])
    
    distance = sum(distance_between_ngram)

    return distance

def classify_language(text_to_classify, list_of_dicts1, list_of_dicts2, threshold):
    pass