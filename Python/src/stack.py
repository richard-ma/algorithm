def top(S: list) -> int:
    return len(S)


def stack_empty(S: list) -> bool:
    if top(S) == 0:
        return True
    else:
        return False


def push(S: list, x) -> None:
    S.append(x)


def pop(S: list) -> int:
    if stack_empty(S):
        raise OverflowError()
    else:
        return S.pop()


if __name__ == "__main__":
    S = list()

    print(stack_empty(S))
    push(S, 1)
    print(stack_empty(S))

    push(S, 2)
    push(S, 33)

    print(pop(S))
    print(pop(S))
    print(pop(S))
