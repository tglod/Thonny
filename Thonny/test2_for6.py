#potrójny apostrof pozwala na zapis na kilku liniach z rzędu w ten sposób
seq="""C-
CACCCGAGAGCGCacggtGTTAGTCGTGTTAATGGCAGGAAGCAGAATGGAGACCTG
GCCCC
TGCCTCTGAA-CCGTGGGTGCT"""
lst=[]
# zamiana liter na wielkie
seq=seq.upper()
# \n to znak specjalny sygnalizujący łamanie tekstu do kolejnego wiersza, zamiana na puste miejsce niweluje łamanie
seq=seq.replace("\n","")
seq=seq.replace("-","")
#print(seq)
for x in range(0,len(seq)//3):
    
    lst.append(seq[:3])
    seq=seq[3:]
print(lst)
    
    