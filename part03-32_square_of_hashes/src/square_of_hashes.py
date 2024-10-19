def hash_square(length):
    length_copy = length
    
    while length_copy > 0:
        print('#' * length)

        length_copy -= 1

if __name__ == "__main__":
    hash_square(5)