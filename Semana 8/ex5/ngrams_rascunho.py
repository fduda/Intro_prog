def compute_ngram_frequency(text,n):
    """
    docstring
    """

    lower_text = text.lower()
    lower_text = lower_text.strip()
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



def remove_unwanted_characters2(ngram_list):
    unwanted_characters = [".", ",", "!", "?", " ", "\n"]
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


def remove_unwanted_characters(ngram_list):
    unwanted_characters = [".", ",", "!", "?", " ", "\n"]
    
    for unwanted in unwanted_characters:
        remove_character_from_ngram(ngram_list, unwanted)
    

    return ngram_list



def remove_character_from_ngram(ngram_list, unwanted_character):
   return [ngram for ngram in ngram_list if ngram != unwanted_character]



f = open("english_1.txt", "r")
text = f.read()
f.close()
text = "banana pack"
print(compute_ngram_frequency(text, 1))

# lista_texto = []
# g = open("texto_em_lista.txt", "w")
# for character in text:
#     lista_texto.append(character)

# g.write(str(lista_texto))
# g.close()
