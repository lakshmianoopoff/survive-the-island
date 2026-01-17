with open("input.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]

capacity = int(lines[-1])

items = []
for line in lines[:-1]:
    w, v = map(int, line.split())
    items.append((w, v))

n = len(items)

dp = [[0] * (capacity + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    weight = items[i - 1][0]
    value = items[i - 1][1]

    for c in range(capacity + 1):
        if weight <= c:
            dp[i][c] = max(
                dp[i - 1][c],             
                dp[i - 1][c - weight] + value 
            )
        else:
            dp[i][c] = dp[i - 1][c]

print(dp[n][capacity])