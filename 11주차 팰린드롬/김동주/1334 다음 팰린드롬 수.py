import typing


def main(s: str) -> str:
    numbers = list(map(int, s))
    s = len(numbers) // 2
    e = len(numbers) - 1 - s
    if (answer := build_palindrome(numbers, s, e)) is None:
        numbers[0] += 1
        numbers[1:] = [0] * (len(numbers)-1)
        answer = build_palindrome(numbers, s, e, increased=True)
    return ''.join(map(str, answer))


def build_palindrome(numbers: typing.Tuple[int], s: int, e: int, stack: typing.List[int] = [], increased=False) -> typing.Optional[typing.Tuple[int]]:
    if s < 0:
        # 모든 자릿 수를 완성함.
        if not increased:
            # 처음 수 보다는 커야 하므로 오답.
            return None
        # 정답 후보의 사본을 생성하여 반환한다.
        answer = list(numbers)
        answer[:len(stack)] = reversed(stack)
        answer[-len(stack):] = stack
        return tuple(answer)

    if not increased:
        # e번째 보다 높은 자릿 수가 커진 적이 없을 경우이다.

        if numbers[s] < numbers[e]:
            # 팰린드롬이 되기 위해서는 e번째 숫자가 감소해야함.
            # 이대로 진행 할 경우, 만들어진 수는 처음에 비해 작아지는 것이 된다.
            # 즉, 오답이다.
            return None

        elif numbers[s] > numbers[e]:
            # 만약 낮은 자릿 수를 *증가*시켜서 펠린드롬을 만들 수 있으면 진행한다.
            increased = True

    # numbers[s]를 펠린드롬 수(스택)에 추가한 상태로 진행해보자
    stack.append(numbers[s])
    # 그냥 한 번 해보고,
    answer1 = build_palindrome(numbers, s-1, e+1, stack, increased)
    # 하나 증가시켜서도 해보자. (자릿수가 증가되는 경우는 정답이 아닌 것으로 계산한다.)
    stack[-1] += 1
    answer2 = build_palindrome(numbers, s-1, e+1, stack, True) if stack[-1] != 10 else None
    # 백트레킹 될 것을 염두해서 스택은 원상 복구.
    stack.pop()

    # 위에서 얻은 두 개의 정답을 비교해서 작은 쪽을 선택한다.
    if answer1 is None:
        return answer2
    if answer2 is None:
        return answer1
    for i in range(len(numbers)):
        if answer1[i] != answer2[i]:
            break
    return answer1 if answer1[i] < answer2[i] else answer2


if __name__ == "__main__":
    # print(main("12345"), 12421)
    # print(main("858"), 868)
    # print(main("1999"), 2002)
    # print(main("1"), 2)
    print(main(input()))
