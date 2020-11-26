dna=["","",""]
rna=["","",""]
x=0

while x <3:
    #wprowadzenie trzykrotne kodonu do trzech pól listy dna, po jednym
    dna[x]=input("Wprowadź kodon: ")
    x=x+1
#
for i in range(0,len(dna)):
    temp=""
    for x in dna[i]:
        if x=="G":
            temp+="T"
        elif x=="C":
            temp+="A"
        elif x=="A":
            temp+="C"
        elif x=="T":
            temp+="G"
        #print(x, temp)
    rna[i]=temp
    
print(rna)
