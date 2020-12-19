import copy

def list_of_ngrams(text, n):
    """
    This function creates a list of ngrams based on a text.
    """

    lower_text = text.lower()  # Converts the text to lower case.
    lower_text = lower_text.strip()  # Removes any inconvenient spaces or extra lines.
    ngram_list = []
    characters_list = []

    for character in lower_text:
        characters_list.append(character)  # Makes a list with every character on the text.

    remove_unwanted_characters(characters_list)  # Remove specific punctuation.

    
    counter = 1 

    # The next block creates a list of ngrams by forming groups of three characters and 
    # adding to a list.
    while counter <= n:
        temp_list = []
        for i in range(len(characters_list)+1):
            temp_list.append(characters_list[i:i+counter])
        
        ngram_list.append(temp_list)
        counter += 1
    ngram_list = ngram_list[n-1]  # Creates a variable that contais n-sized list of characters.

    remove_unwanted_ngrams(ngram_list)  # Removes lists that contain spaces (" ") as elements.
    return ngram_list



def remove_unwanted_characters(characters_list):
    """
    This function receives a list of characters as elements and removes
    unwanted punctuation characters.
    """

    unwanted_characters = [".", ",", "!", "?", "\n"]  # List of unwanted punctuation characters.
    characters_list_copy = copy.deepcopy(characters_list)

    # The next block removes the unwanted characters from the list.
    for character in characters_list_copy:
        if character in unwanted_characters:
            characters_list.remove(character)

    return characters_list

def remove_unwanted_ngrams(ngram_list):
    """
    This function removes ngrams that contain spaces as one of the characters
    and ngrams that have a different size than the rest.
    """
    ngram_list_copy = copy.deepcopy(ngram_list)
    
    ngram_lenght = len(ngram_list[0])  # Sets the size of the ngrams. The first one is always on the right size.

    # The next block removes ngrams with spaces and with different sizes.
    for ngram in ngram_list_copy:
        for character in ngram:
                if character == " ":
                    if ngram in ngram_list:
                        ngram_list.remove(ngram)
                    else:
                        break
        if len(ngram) != ngram_lenght:
                ngram_list.remove(ngram)
    return ngram_list



def compute_ngram_frequency(text,n):
    """
    This function receives a text and returns a dictionary with ngrams as keys
    and its frequencies as values.
    """

    ngram_counter = dict()  # Counts how many times an ngram appears in the text.
    ngram_frequency = dict()  # Calculates the frequency of ngrams in the text.

    ngram_list = list_of_ngrams(text,n)  # List of ngrams already without spaces and without punctuation characters.
    
    for ngram in ngram_list:
        joint_ngram = "".join(ngram)  # Converts each list of ngrams into a string.
        if joint_ngram not in ngram_counter:
            ngram_counter[joint_ngram] = 1  # If the ngram is new to the dictionary, creates a key as ngram and 1 as its value.
        else:
            ngram_counter[joint_ngram] +=1  # If the ngram already exists in the dictionary, adds 1 to its value. 

    for ngram in ngram_counter:
        ngram_frequency[ngram] = ngram_counter[ngram]/len(ngram_list)  # Calculates the frequency based on how many ngrams and how many times each one appears.
    

    return ngram_frequency


def compute_ngrams_frequency(text,k):
    """
    This function receives a text and a number and returns a list of dictionaries of ngrams up to k.
    """
    list_of_frequencies = []
    # The next block appends the dictionaries of ngrams frequency up to n=k.
    for i in range(1,k+1):
        list_of_frequencies.append(compute_ngram_frequency(text,i))
    return list_of_frequencies

def ngram_dict_to_string(ngram_dict):
    """
    This function converts a dictionary into string.
    """
    list_from_dict = []
    # The next block converts a dictionary into a string, keeping its keys and values.
    for key, value in ngram_dict.items():
        string = "{}:{}".format(key,value)
        list_from_dict.append(string)
    string_from_dict = " ".join(list_from_dict)

    return string_from_dict

def string_to_ngram_dict(string):
    """
    This functions converts a string into a dictionary.
    """
    string_to_list = string.split(" ")
    ngram_dict = dict()
    for element in string_to_list:
        element_list = element.split(":")
        ngram_dict[element_list[0]]=float(element_list[1])
    return ngram_dict

def write_list_of_ngram_dicts(list_of_dicts, filename):
    """
    This function writes a converted dictionary (dictionary into string) in a file.
    Each dictionary is written in a line.
    """
    f = open(filename, "w")  # Opens the file in "write" mode.

    for element in list_of_dicts:  
        f.write(ngram_dict_to_string(element))  # Writes every dictionary in its string form into the file.
        f.write("\n")
    f.close()  # Closes the file.


def load_list_of_ngram_dicts(filename):
    """
    This function reads the strings in a file and converts them into dictionaries.
    """
    f = open(filename, "r")  # Opens the file in "read" mode.
    lines = f.readlines()  # Reads every line in the file.
    list_of_dicts = []

    for line in lines:
        list_of_dicts.append(string_to_ngram_dict(line))  # Converts the strings in the file into dictionaries, appends to a list.

    f.close()  # Closes the file.
    return list_of_dicts

