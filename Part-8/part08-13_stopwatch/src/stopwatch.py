class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        self.seconds += 1
        
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

            if self.minutes == 60:
                self.minutes = 0

    def __str__(self) -> str:
        line = ''
        if self.minutes < 10:
            line += f'0{self.minutes}:'
        else:
            line += f'{self.minutes}:'

        if self.seconds < 10:
            line += f'0{self.seconds}'
        else:
            line += f'{self.seconds}'

        return line
    

if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()

