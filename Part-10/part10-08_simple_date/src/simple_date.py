class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __day_convertion(self):
        return self.year * 360 + (self.month - 1) * 30 + self.day

    def __gt__(self, date: "SimpleDate"):
        return self.__day_convertion() > date.__day_convertion()
    
    def __lt__(self, date: "SimpleDate"):
        return self.__day_convertion() < date.__day_convertion()
    
    def __eq__(self, date: "SimpleDate"):
        return self.__day_convertion() == date.__day_convertion()
    
    def __ne__(self, date: "SimpleDate"):
        return self.__day_convertion() != date.__day_convertion()
    
    def __add__(self, days: int):
        new_date = self.__day_convertion()
        new_date += days

        new_date_year = new_date // 360
        new_date_days = new_date % 360
        new_date_month = (new_date_days // 30) + 1
        new_date_day = new_date_days % 30

        return SimpleDate(new_date_day, new_date_month, new_date_year)
    
    def __sub__(self, date: "SimpleDate"):
        return abs(self.__day_convertion() - date.__day_convertion())
    

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)
        

        