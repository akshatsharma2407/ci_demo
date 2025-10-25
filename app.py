def add(a, b):
    return a + b


def sub(a, b):
    return a - b


if __name__ == '__main__':
    result1 = add(1, 2)
    result2 = sub(2, 4)

    print(result1(1, 23), result2(4, 2))
