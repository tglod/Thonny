seq = ("AGCTTTCGCCTCAAAGA");
lst=list(seq)
t1=seq[0];
t2=seq[1];
nxt=seq[2];
print(lst)
for x in  range( 0,len(lst)):
    
    
        
    if(lst[x]=="G"):
        if(x==0):
             lst[x+1]='C';
        elif(x==len(lst)-1):
             lst[x-1]='C';
        else:
             lst[x-1]='C';
             lst[x+1]='C';
print(lst)