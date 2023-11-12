from collections import defaultdict


def main():
    print(challenge(input().rstrip()))


def challenge(input_: str) -> str:
    positions = defaultdict(list)

    for i, word in enumerate(input_.split()):
        positions[word.lower()].append(i)

    # noinspection PyShadowingNames
    return ''.join(f'{word}{len(positions[word])}'
                   for word in sorted(positions, key=lambda word: positions[word][0]))


if __name__ == '__main__':
    main()
