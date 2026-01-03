import nltk
from nltk.corpus import words 

def main():
    length=input("Especifica el número de letras que tiene la palabra:\n")
    
    while not length.isdigit() and length.lower()!="exit":

        length=input("Ha introducido algo que no es un número.\nPor favor Especifica el número de letras que tiene la palabra o introduzca la palabra exit para abortar:\n")

    if(length.lower()=="exit"):
        return 0
    
    else:
        length=int(length)
    
    list=[]
    final_list=[]

    for i in range(length):
        list_letters=input("Introduce todas las posibles letras que contiene la letra en la posición "+str(i)+" separadas por espacios, en caso de no saber que letras son posibles colocar .:").split(" ")
        if(list_letters==["."]):
            list_letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        list.append(list_letters)

    words_list=words.words()

    for word in words_list:
    
        if(len(word)==length):
            valid=True
            counter=0

            while valid and counter < length:

                if(word[counter] not in list[counter]):
                    valid=False

                counter+=1
            if valid and word not in final_list:
                final_list.append(word)

    print(final_list)


main()
