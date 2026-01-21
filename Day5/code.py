import bisect
with open("input.txt","r") as file:
    lines=file.read().strip().split("\n")
    
T=int(lines[-1])

intervels=[]
for line in lines[:-1]:
    s,e,v=map(int,line.split())
    intervels.append((s,e,v))
intervels.sort(key=lambda x:x[1])
end_times=[x[1] for x in intervels]
n=len(intervels)
dp=[0]*(n+1)
for i in range(1,n+1):
    s,e,v=intervels[i-1]
    idx=bisect.bisect_right(end_times,s)-1
    take=v+(dp[idx+1]if idx>=0 else 0)
    skip =dp[i-1]
    dp[i]=max(take,skip)
print(dp[n])
