# O(n log n)의 시간 복잡도를 위해 quick_sort 함수 사용
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # 피벗 원소를 선택
    pivot = arr[len(arr) // 2]

    # 피벗보다 작은 원소들 (왼쪽)
    left = [x for x in arr if x < pivot]

    # 피벗과 같은 원소들 (가운데)
    middle = [x for x in arr if x == pivot]

    # 피벗보다 큰 원소들 (오른쪽)
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# 사용자로부터 요소의 개수인 A를 입력받기
A = int(input())

# 사용자 입력을 저장할 빈 리스트를 초기화
A_list = []


# A개의 정수를 사용자로부터 입력받고 A_list에 저장
for i in range(A):
    num = int(input())
    A_list.append(num)

# quick_sort 함수를 사용하여 리스트를 정렬
A_list = quick_sort(A_list)

# 정렬된 리스트 출력
for i in A_list:
    print(i)


