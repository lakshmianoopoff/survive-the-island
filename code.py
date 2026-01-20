
with open("input.txt","r") as file:
    lines=file.read().strip().split("\n")

locations=[]
for line in lines[:-1]:
    f,w,t=map(int,line.split())
    locations.append((f,w,t))   
F,W=map(int,lines[-1].split())
n=len(locations)
left=0
total_food=0
total_water=0
total_time=0

min_time=float('inf')
for right in range (n):
    f,w,t=locations[right]
    total_food+=f
    total_water+=w
    total_time+=t
    while total_food>=F and total_water>=W:
        min_time=min(min_time,total_time)
        lf,lw,lt=locations[left]
        total_food-=lf
        total_water-=lw
        total_time-=lt
        left+=1
        
if min_time==float('inf'):
    print(-1)
else:
    print(min_time)
        
        
