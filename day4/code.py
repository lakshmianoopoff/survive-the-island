with open("input.txt","r") as file:
    lines=file.read().strip().split("\n")
    
tasks=[]
for line in lines[:-1]:
    t,r=map(int,line.split())
    tasks.append((t,r))
    
T,I=map(int,lines[-1].split())
dp=[0]*(T+1)
for time_needed,reduce in tasks:
    for t in range(T,time_needed-1,-1):
        dp[t]=max(dp[t],dp[t-time_needed]+reduce)
        
max_reduction=max(dp)

remaining_instability=I-max_reduction
if remaining_instability<0:
    print(0)
else:
    print(remaining_instability)
    
    
