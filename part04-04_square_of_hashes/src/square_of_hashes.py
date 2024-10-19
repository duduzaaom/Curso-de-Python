def line(length, string):
    if string != '':
        print(string[0] * length)
    else:
        print('*' * length)

def square_of_hashes(size):
    size_copy = size
    while size_copy > 0:
        line(size, "#")
        
        size_copy -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
