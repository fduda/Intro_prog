def func(a):
    lista =  [] 
    word = input ()
    while True:
        word = input()
        lista.append(word)
        if word == "":
            break
    
    counter = 0
    for i in lista:
        if a in i:
            counter += 1

    string=""
    for i in lista:
        string += i
    print (string)

func("a")
print("Hello world")
