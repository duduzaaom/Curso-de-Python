class Clock:
    def __init__(self, hour: int, min: int, sec: int) -> None:
        self.hours = hour
        self.min = min
        self.sec = sec

    def tick(self):
        self.sec += 1

        if self.sec == 60:
            self.sec = 0
            self.min += 1

            if self.min == 60:
                self.min = 0
                self.hours += 1

                if self.hours == 24:
                    self.hours = 0

    def set(self, hour, min):
        self.hours = hour
        self.min = min
        self.sec = 0

    def __str__(self) -> str:
        return f"{self.hours:02}:{self.min:02}:{self.sec:02}"
    

if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)