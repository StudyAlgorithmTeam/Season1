T = int(input())
arr = [0]*101
arr[1]=1
arr[2]=1
arr[3]=1

for j in range(4, 101):
    arr[j] = arr[j-2]+arr[j-3]

for i in range(T):
    n = int(input())
    print(arr[n])


