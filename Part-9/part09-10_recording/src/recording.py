class Recording:
    def __init__(self, length: int) -> None:
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("The length of the recording should be a positive number.") 

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, length):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("The length of the recording should be a positive number.")
        

if __name__ == "__main__":
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)