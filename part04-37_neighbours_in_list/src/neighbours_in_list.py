def longest_series_of_neighbours(list):
    result = []
    longest_series = 0

    for item in list:
        if result == []:
            result.append(item)
            continue
        
        if item - result[len(result) - 1] == 1 or item - result[len(result) - 1] == -1:
            result.append(item)

            if len(result) >= longest_series:
                longest_series = len(result)
        else:
            result = [item]

    return longest_series


if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25, 30]
    print(longest_series_of_neighbours(my_list))

        