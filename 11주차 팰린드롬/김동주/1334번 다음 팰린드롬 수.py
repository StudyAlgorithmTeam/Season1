import typing


def main(s: str) -> str:
    number = str(int(s)+1)
    numbers = list(map(int, number))
    make_palindrome(numbers)
    return ''.join(map(str, numbers))


def make_palindrome(numbers: typing.List[int], s: int = 0, e: int = None, increased_at: int = None):
    if e is None:
        e = len(numbers) - 1
    if increased_at is None:
        increased_at = len(numbers)

    if s > e:
        # 모든 수를 완성했다는 뜻.
        return

    if numbers[s] < numbers[e]:
        if increased_at >= e:
            # e번째 자리 수 이전에 증가된 숫자가 없을 경우에는 숫자를 낮출 수 없다.
            # 따라서, 앞자리 수에서 값을 증가시킨 뒤, e번째 숫자를 낮춘다.
            increased_at = increase_a_bit(numbers, s, e)
    numbers[e] = numbers[s]

    make_palindrome(numbers, s+1, e-1, increased_at)


def increase_a_bit(numbers: typing.List[int], s: int, e: int) -> int:
    """펠린드롬을 만들어 가면서 증가 시킬 수 있는 수 중 가장 작은 숫자를 증가시킴.

    증가시킨 수의 인덱스를 반환한다.
    """
    # 펠린드롬의 양 끝단에서 부터 탐색 시작
    while s < e:
        if numbers[s] > numbers[e]:
            # 증가 시켜야 할 낮은 자리 수를 발견하면 해당 숫자를 증가시키고 종료.
            numbers[e] = numbers[s]
            return e
        s += 1
        e -= 1
    # 여기까지 왔다는 건, 중간에 증가시킬 숫자가 없어서 s와 e가 가운데 까지 왔다는 뜻.
    # e보다 높은 자릿 수 중, 9가 아닌 가장 낮은 자릿 수를 찾아 1 증가시키자.
    while numbers[e] == 9:
        e -= 1
        s += 1
    numbers[e] += 1
    # 증가시킨 숫자보다 낮은 자리 수들은 0으로 바꿔준다.
    for i in range(e+1, s):
        numbers[i] = 0
    return e


if __name__ == "__main__":
    # print(main("12345"), 12421)
    # print(main("858"), 868)
    # print(main("1999"), 2002)
    # print(main("1"), 2)
    # print(main("9999"), 10001)
    # print(main("4995"), 5005)
    # print(main("498"), 505)
    # print(main("10001"), 10101)
    # print(main("5749201"), 5749475)
    # print(main("12012"), 12021)
    # print(main("110101"), 111111)
    # print(main("4651354631683213233486146513546316832132334861"), "시간 초과 검사용")
    print(main(input()))
