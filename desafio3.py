def count_anagram(string):
    my_list = []
    if type(string) != str:
        return False
    for index_i, i in enumerate(string):
        for index_j, j in enumerate(string):
            anagrama = string[index_i: index_j + 1]
            if anagrama != "":
                my_list.append(string[index_i: index_j + 1])
    ordered_anagrams = [sorted(item) for item in my_list]
    my_anagram = ["".join(element) for element in ordered_anagrams]
    my_dict = dict()
    for item in my_anagram:
        if item not in my_dict:
            my_dict[item] = 1
        else:
            my_dict[item] += 1
    count = 0
    for key, value in my_dict.items():
        if value >= 2:
            count += 1

    return count
