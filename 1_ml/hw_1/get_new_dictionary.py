def reverse_dict_func(my_dict):
    reversed_dict = {}
    for key, value_list in my_dict.items():
        for value in value_list:
            if value not in reversed_dict.keys():
                reversed_dict[value] = [key]
            else:
                reversed_dict[value].append(key)
    return dict(sorted(reversed_dict.items()))


def get_new_dictionary(input_dict_name, output_dict_name):
    with open(input_dict_name) as fl:
        my_dict = {}
        n_rows = int(fl.readline().strip())
        for _ in range(n_rows):
            row = fl.readline().strip().split(' - ')
            my_dict[row[0]] = row[1:][0].split(', ')

    reversed_dict = reverse_dict_func(my_dict)
    with open(output_dict_name, 'w') as f:
        print(len(reversed_dict.keys()), file=f)
        for key in reversed_dict.keys():
            print(key, '-', ', '.join(sorted(reversed_dict[key])), file=f)
