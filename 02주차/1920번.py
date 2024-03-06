def binary_search(array, elem):
    #left, right 값 초기화
    left, right = 0, len(array) - 1
    
    #왼쪽 인덱스가 오른쪽 인덱스보다 작거나 같을 동안 반복
    while left <= right:
        mid = (left + right) // 2
        #중간 값이 찾고자 하는 값과 같다면, 1 반환하고 종료
        if array[mid] == elem:
            return 1
        #만약 중간 값이 찾는 값보다 작다면, 왼쪽 범위를 중간 값의 오른쪽으로 1씩 조정
        elif array[mid] < elem:
            left = mid + 1
        #중간 값이 찾고자 하는 값보다 크다면, 오른쪽 범위를 중간 값의 왼쪽으로 1씩 조정
        else:
            right = mid - 1
    return 0

#입력으로부터 정수 n 받기
n = int(input())
a_list = list(map(int, input().split()))
#입력으로부터 정수 m 받기
m = int(input())
x_list = list(map(int, input().split()))

#리스트 정렬
a_list.sort()

for x in x_list:
    print(binary_search(a_list, x))
