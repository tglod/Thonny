seq = ("AGCTTTCGCCTCAAAGA")

#konwertowanie sekwencji na listę, w której każda litera ma swój indeks od 0 do n-1
lst=list(seq)
t1=lst[0]
t2=lst[1]
nxt=lst[2]
print(lst)
for x in  range( 0,len(lst)):
    
    
        
    if(lst[x]=="G"):
        if(x==0):
            lst[x+1]='C'
        elif(x==len(lst)-1)
            lst[x-1]='C'
        else:
            lst[x-1]='C'
            lst[x+1]='C'
print(lst)
