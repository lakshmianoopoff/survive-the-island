with open("input.txt","r") as file:
    lines=file.read().strip().split("\n")
    
k = int(lines[-1])

totals={}
for line in lines[:-1]:
    F,N=line.split()
    N=int(N)
    if F in totals:
        totals[F]+=N
    else:
        totals[F]=N
        
values=list(totals.values())
values.sort(reverse=True)
print(sum(values[:k]))
         
    
       
    

    
    