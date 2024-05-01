def ContLetters(text):
    type={"Uppercase":0, "Lowercase":0}
    for Letter in text:
        if Letter.isupper():
           type["Uppercase"]+=1
        elif Letter.islower():
           type["Lowercase"]+=1
    print ("Texto original: ", text)
    print ("Número de letras maiúsculas: ", type["Uppercase"])
    print ("Número de letras minúsculas: ", type["Lowercase"])

#string_test('The quick Brown Fox')
ContLetters("A melhor forma de prever o futuro é Criá-Lo")