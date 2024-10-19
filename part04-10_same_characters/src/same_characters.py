def same_chars(string, index1, index2):
    if index1 > len(string) - 1 or index2 > len(string) - 1 or string[index1] != string[index2]:
        return False
    else:
        return True


if __name__ == "__main__":
    print(same_chars("programmer", 12, 7))