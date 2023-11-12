from collections.abc import Generator


def main():
    print(*challenge(input().rstrip()), sep='')


def challenge(input_: str) -> Generator[int]:
    n = 0

    for char in input_:
        match char:
            case '#':
                n += 1
            case '@':
                n -= 1
            case '*':
                n *= n
            case '&':
                yield n
            case _:
                raise NotImplementedError


if __name__ == '__main__':
    main()
