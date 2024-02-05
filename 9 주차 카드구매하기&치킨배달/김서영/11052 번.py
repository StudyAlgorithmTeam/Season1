import sys

num_items = int(sys.stdin.readline())
item_prices = [0]
item_prices += list(map(int, sys.stdin.readline().split()))

for idx in range(1, num_items + 1):
    temp = []
    for t in range(idx // 2 + 1):
        temp.append(item_prices[t] + item_prices[idx - t])
    item_prices[idx] = max(temp)

sys.stdout.write(str(item_prices[num_items]))
