# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        if self.__cents >= 10:
            return f"{self.__euros}.{self.__cents} eur"
        else:
            return f"{self.__euros}.0{self.__cents} eur"
        
    def __eq__(self, Money: "Money"):
        return self.__euros + self.__cents / 100 == Money.__euros + Money.__cents / 100
    
    def __gt__(self, Money: "Money"):
        return self.__euros + self.__cents / 100 > Money.__euros + Money.__cents / 100
    
    def __lt__(self, Money: "Money"):
        return self.__euros + self.__cents / 100 < Money.__euros + Money.__cents / 100

    def __ne__(self, Money: "Money"):
        return self.__euros + self.__cents / 100 != Money.__euros + Money.__cents / 100
    
    def __add__(self, money: "Money"):
        total_cents = (self.__euros * 100 + self.__cents) + (money.__euros * 100 + money.__cents)
        new_euros = total_cents // 100
        new_cents = total_cents % 100   

        return Money(new_euros, new_cents)
    
    def __sub__(self, money: "Money"):
        if self < money:
            raise ValueError("a negative result is not allowed")
        
        total_cents = (self.__euros * 100 + self.__cents) - (money.__euros * 100 + money.__cents)
        new_euros = total_cents // 100
        new_cents = total_cents % 100   

        return Money(new_euros, new_cents)
        

if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1