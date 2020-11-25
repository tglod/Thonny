
#Zbieranie zmiennych
seq = "AGCGATTGAUGUTUTGUTUGAUGTUGCGACGUACUGUAUA";
#Zaczynamy od indeksu 0
t1=seq[0];
t2=seq[1];
nxt=seq[2];
#Ilość tabulatorów dyktuje 'warstwę' wykonywania - od lewej do prawej
for x in range(3, len(seq)): #Wykonuje się n-3 razy
    if (t1=="A" and t2=="U" and nxt=="G"):
        print ("Sekwencja zaczyna się na indeksie: ", x-2);
    #przesunięcie kolejki w prawo
    nxt=seq[x];
    t2=seq[x-1];
    t1=seq[x-2];
else:
            #przecięcie całkowite seq w pół 
            half=(len(seq))//2;
            #przypisanie lewej połowy, kombinacji AUG i prawej połowy do seq
            seq=seq[:half]+"|AUG|"+seq[half:];
            print(seq);
        
            