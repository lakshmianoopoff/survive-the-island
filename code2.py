with open("input2.txt","r") as file:
    lines = file.read().strip().split("\n")
c = int(lines[-1])

attempts = []
for line in lines[:-1]: 
    a, b = map(int, line.split())
    attempts.append((a, b))

dp = [0]*(c+1)

for a, b in attempts:
    new_dp = dp[:]
    for strain in range(c+1):
        if strain + a <= c:
            new_dp[strain + a] = max(new_dp[strain + a], dp[strain] + 1)
        if strain + b <= c:
            new_dp[strain + b] = max(new_dp[strain + b], dp[strain] + 1)
    dp = new_dp  

print(max(dp))
