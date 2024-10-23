class ListHelper:
    @classmethod
    def items_occurence(cls, my_list: list):
        items = {}
        
        for item in my_list:
            if item not in items:
                items[item] = 0
            items[item] += 1

        return items

    @classmethod
    def greatest_frequency(cls, my_list: list):
        items = ListHelper.items_occurence(my_list)
        biggest_occurence_amount = 0

        for item, occurence in items.items():
            if occurence > biggest_occurence_amount:
                biggest_occurence_amount = occurence
                biggest_occurence_item = item

        return biggest_occurence_item
    
    @classmethod
    def doubles(cls, my_list: list):
        items = ListHelper.items_occurence(my_list)
        unique_items = 0

        for item, occurence in items.items():
            if occurence >= 2:
                unique_items += 1

        return unique_items
            

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))