N = int(input())    # 수의 개수
A = list(map(int, input().split())) # 숫자 입력(수열)
operator = list(map(int, input().split()))  # 연산자 입력

maximum = -1e9 # e나 E 뒤에 숫자는 10의 지수 (따라서 10의 9승인 10억)
minimum = 1e9

def backtrack(depth, total, plus, minus, multi, divide):
    global maximum, minimum

    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        backtrack(depth+1, total+A[depth], plus-1, minus, multi, divide)
    if minus:
        backtrack(depth + 1, total - A[depth], plus, minus-1, multi, divide)
    if multi:
        backtrack(depth + 1, total * A[depth], plus, minus, multi-1, divide)
    if divide:
        if total < 0:
            backtrack(depth + 1, -(-total // A[depth]), plus, minus, multi, divide - 1)
        backtrack(depth + 1, total // A[depth], plus, minus, multi, divide - 1)
        #else:
        #    backtrack(depth + 1, total // A[depth], plus, minus, multi, divide - 1)

backtrack(1, A[0], operator[0], operator[1], operator[2], operator[3])
print(maximum)
print(minimum)

