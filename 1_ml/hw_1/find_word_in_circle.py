def right_circle(str_1, i, length):
    return (str_1 * 8)[i:i + length]


def left_circle(str_1, i, length):
    ls = len(str_1)
    return (str_1 * 8)[ls + i:ls + i - length:-1]


def find_word_in_circle(str_1, str_2):
    length = len(str_2)
    for i in range(len(str_1) + 1):
        if str_2 == right_circle(str_1, i, length):
            res = (i, 1)
            return res
        elif str_2 == left_circle(str_1, i, length):
            res = (i, -1)
            return res
    return -1
