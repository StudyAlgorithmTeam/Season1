# O(N^2)의 시간복잡도를 하기 위해 선택정렬 코드

# A개의 정수를 입력
A = int(input())

# 입력된 정수를 저장할 빈 리스트 A_list를 초기화시키기
A_list = []

# A번 반복하여 정수를 사용자로부터 입력받고 A_list 리스트에 저장
for i in range(A):
    num = int(input())
    A_list.append(num)

# 선택 정렬을 이용하여 리스트를 정렬
for i in range(A):
    # 현재 위치부터 나머지 원소 중에서 최솟값의 인덱스 찾기
    min_index = i
    for j in range(i + 1, A):
        if A_list[j] < A_list[min_index]:
            min_index = j

    # 현재 위치의 원소와 최솟값의 원소를 교환
    A_list[i], A_list[min_index] = A_list[min_index], A_list[i]

# 정렬된 리스트를 출력
for i in A_list:
    print(i)
