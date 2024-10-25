import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        

class MostVowels(WordGame):
    vowels = "aeiou"

    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        player1_vowels = 0
        player2_vowels = 0

        for letter in player1_word:
            if letter in MostVowels.vowels:
                player1_vowels += 1

        for letter in player2_word:
            if letter in MostVowels.vowels:
                player2_vowels += 1

        if player1_vowels > player2_vowels:
            return 1
        elif player2_vowels > player1_vowels:
            return 2


class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        words = ["rock", "paper", "scissors"]
        player1_wins = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]

        if player1_word not in words:
            if player2_word in words:
                return 2
            else:
                return
        elif player2_word not in words:
            return 1
        
        if player1_word == player2_word:
            return
        
        for play in player1_wins:
            if (player1_word, player2_word) == play:
                return 1
            
        return 2
    

if __name__ == "__main__":
    p = RockPaperScissors(4)
    p.play()

