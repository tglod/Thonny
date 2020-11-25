rna = "AGCUUUCGCCUCAAAGA"
#rna = "AGCUUUCGCCUCAAGCAGCAGCAGCAAGA" przykładowa sekwencja z wykrywaną mutacją
rna="AUG"+rna+"UAG"
pprev=""
prev=""
temp=""
for x in range(0,len(rna)//3):
    pprev=prev
    prev=temp
    temp=rna[x*3:(x+1)*3]
    #print("pprev: "+pprev+" prev: "+prev+ " temp: " +temp) drukowanie każdej kolejnej trójki trójek (Dla wglądu działania algorytmu)
    if(pprev == prev and prev == temp):
        #drukowanie indeksów znalezionych mutacji - to str(`operacje`) jest wymagane dla takiego wypisywania tekstu i liczb
        print("Mutacja znaleziona na indeksach "+str((x-2)*3)+" i "+str((x+1)*3))
    
    