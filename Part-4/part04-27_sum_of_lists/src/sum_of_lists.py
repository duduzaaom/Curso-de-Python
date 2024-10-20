def list_sum(list1, list2):
    item2 = 0
    sum = []

    for item1 in list1:
        sum.append(item1 + list2[item2])
        item2 += 1

    return sum


if __name__ == '__main__':
    a = [1, 4, 8]
    b = [-3, 9, 1]

    print(list_sum(a, b))
