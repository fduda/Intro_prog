def recognize_language(lst, dct):
    french_words = []
    english_words = []

    for word in lst:
        if word in dct.keys():
            english_words.append(word)
        elif word in dct.values():
            french_words.append(word)

    if len(english_words)/len(lst) >= 0.7:
        return "English"
    elif len(french_words)/len(lst) >= 0.7:
        return "French"

    return "Unknown"


text1 = ["good", "night", "to", "you"]
text2 = ["oui", "oui", "oui", "you"]
text3 = ["oui", "toi", "xyz", "you"]
dct1 = {"yes": "oui", "good": "bien", "night": "nuit", "you": "toi"}
print(recognize_language(text3, dct1))
