def reverse(x: int) -> int:
    o = [i for i in list(str(x)) if i.isnumeric()]

    if x < 0:
        a = int('-' + ''.join(o[::-1]))
    else:
        a = int(''.join(o[::-1]))
    if -2 ** 31 <= a <= 2 ** 31:
        return a
    else:
        return 0