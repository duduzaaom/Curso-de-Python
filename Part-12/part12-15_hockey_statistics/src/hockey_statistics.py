import json

class HockeyPlayer:
    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.points = self.goals + self.assists

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

        for player in filter(lambda player: player.name == name, self.players):
            print(player)
            
    def list_teams(self):
        teams = list(set(player.team for player in self.players))
        for team in sorted(teams):
            print(team)

    def list_countries(self):
        countries = list(set(player.nationality for player in self.players))
        for country in sorted(countries):
            print(country)

    def list_players_in_team(self):
        team = input("team: ")
        print()

        players = [player for player in self.players if player.team == team]
        for player in sorted(players, key=lambda player: player.points, reverse=True):
            print(player)

    def list_players_from_country(self):
        country = input("country: ")
        print()

        players = [player for player in self.players if player.nationality == country]
        for player in sorted(players, key=lambda player: player.points, reverse=True):
            print(player)

    def list_most_points(self):
        number = int(input("how many: "))
        print()

        for player in list(sorted(self.players, key=lambda player: (player.points, player.goals), reverse=True))[:number]:
            print(player)

    def list_most_goals(self):
        number = int(input("how many: "))
        print()

        for player in list(sorted(self.players, key=lambda player: (player.goals, -player.games), reverse=True))[:number]:
            print(player)

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
                self.search_player()
            elif command == 2:
                self.list_teams()
            elif command == 3:
                self.list_countries()
            elif command == 4:
                self.list_players_in_team()
            elif command == 5:
                self.list_players_from_country()
            elif command == 6:
                self.list_most_points()
            elif command == 7:
                self.list_most_goals()
    

def main():    
    program = HockeyPlayerApplication()
    program.execute()

main()

if __name__ == "__main__":
    program = HockeyPlayerApplication()
    program.execute()
    program.process_file("partial.json")
    program.list_most_goals()


