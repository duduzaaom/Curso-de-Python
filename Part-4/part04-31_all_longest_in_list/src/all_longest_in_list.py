def all_the_longest(list):
    longest = ''
    longest_list = []

    for string in list:
        if len(string) >= len(longest):

            longest = string
            
    for string in list:
        if len(string) == len(longest):
            longest_list.append(string)

    return longest_list


if __name__ == '__main__':
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
