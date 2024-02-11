import sys
input = sys.stdin.readline

T = int(input())    # 테스트 케이스
case_index = []     # P(N)의 N을 담을 리스트
P = [0, 1, 1, 1]    # 파도반 수열 P
#차례로 P(0), 1, 2, 3

# 각 테스트 케이스 N 입력
for t in range(T) :
    case_index.append(int(input()))


# dynamic programing
for t in range(T):
    if case_index[t] < 4:   # P(1)~P(3) 값이 1
        print(1)
        continue
    elif len(P) >= case_index[t] and P[case_index[t]] != 1: # P(N)의 값이 리스트에 존재하면 출력
        print(P[case_index[t]])
        continue
    for N in range(4, max(case_index)+1): # 입력된 N 중에 최대값부터 점화식 이용
        P.append(P[N-2] + P[N-3])
    print(P[case_index[t]])