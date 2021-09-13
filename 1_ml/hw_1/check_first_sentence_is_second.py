def get_dict(lst):
    res = {}
    for elem in lst:
        try:
            res[elem] += 1
        except KeyError:
            res[elem] = 1
    return dict(sorted(res.items()))


def check_first_sentence_is_second(str_1, str_2):
    if len(str_2) == 0:
        return True
    if len(str_2) > len(str_1):
        return False
    lst_str_1 = str_1.split(' ')
    lst_str_2 = str_2.split(' ')
    dict_str_1 = get_dict(lst_str_1)
    dict_str_2 = get_dict(lst_str_2)
    for word, count_w_2 in dict_str_2.items():
        try:
            count_w_1 = dict_str_1[word]
        except KeyError:
            return False
        if count_w_2 > count_w_1:
            return False
    return True
