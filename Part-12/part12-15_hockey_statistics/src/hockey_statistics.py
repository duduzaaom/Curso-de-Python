import json

def process_file(file: str):
    with open(file) as f:
        data = f.read()

    return json.loads(data)


class HockeyPlayer:
    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games

    def __str__(self):
        return f"{self.name:21}{self.team}{self.goals:>4} +{self.assists:>3} ={self.goals + self.assists:>4}"
    

class HockeyPlayerApplication:
    def __init__(self):
        self.players = []

    def process_file(self, file: str):
        with open(file) as f:
            data = f.read()

        players = json.loads(data)

        for player in players:
            hockey_player = HockeyPlayer(player["name"], player["nationality"], player["assists"], player["goals"], player["penalties"], player["team"], player["games"])
            self.players.append(hockey_player)

    def search_player(self):
        name = input("name: ")

        for player in self.players:
            if player.name == name:
                print(player)
                return
            
    def list_teams(self):
        pass

    def execute(self):
        file_name = input("file name: ")
        self.process_file(file_name)

        print(f"read the data of {len(self.players)} players")

        print()

        print("commands:")
        print("0 quit\n1 search for player\n2 teams\n3 countries\n4 players in team\n5 players from country\n6 most points\n7 most goals")
        while True:
            print()
            command = int(input("command: "))

            if command == 0:
                break
            elif command == 1:
                self.seach_player()
            elif command == 2:
                self.list_teams()
    

if __name__ == "__main__":
    program = HockeyPlayerApplication()
    # program.execute()
    program.process_file("partial.json")
    program.search_player()

