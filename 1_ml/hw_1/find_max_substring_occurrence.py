def find_max_substring_occurrence(str_1):
    tmp = 0
    for i in range(1, len(str_1) + 1):
        sub_str = str_1[:i]
        k = len(str_1) // len(sub_str)
        if str_1 == sub_str * k:
            tmp = max(k, tmp)
    return tmp
