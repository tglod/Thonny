seq = input("Wprowadź sekwencję: ")
seq=seq.upper()
#Tworzenie listy o nieokreślonym rozmiarze do zapełnienia
lst = [];
# wykona się n/3 całkowicie, gdzie n to liczba elementów seq
for x in range((len(seq)//3)):
    
    
    #dopisywanie trójki jako pojedynczego elementu listy
    lst.append(seq[:3]);
    print(lst);
    #przycięcie sekwencji o już zapisaną trójkę
    seq=seq[3:];
else:
    print(lst);
    #print("W efekcie trójek jest: ",len(lst))