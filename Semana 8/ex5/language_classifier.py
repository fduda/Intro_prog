import ngrams as ng
import os

def build_language_model(language1_filename, language2_filename, k):

    final_list = []

    file1_path = os.path.isfile(language1_filename)
    file2_path = os.path.isfile(language2_filename)

    if file1_path == False or file2_path == False:
        return None
    
    file1 = open(language1_filename, "r")
    file2 = open(language2_filename, "r")
    text1 = file1.read()
    text2 = file2.read()
    
    if text1 == "" or text2 == "":
        return None

    final_list.append(ng.compute_ngrams_frequency(text1, k))
    final_list.append(ng.compute_ngrams_frequency(text2, k))

    return final_list


# print(build_language_model("dutch_1.txt", "dutch_2.txt", 2))