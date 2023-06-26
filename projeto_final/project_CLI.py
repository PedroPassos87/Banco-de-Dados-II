from player import Player
from game import Game
from score import Score


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class ProjectCLI(SimpleCLI):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.add_command("createPlayer", self.create_player)
        self.add_command("readPlayers", self.read_players)
        self.add_command("updatePlayer", self.update_player)
        self.add_command("deletePlayer", self.delete_player)
        self.add_command("createGame", self.create_game)
        self.add_command("readGames", self.read_games)
        self.add_command("updateGame", self.update_game)
        self.add_command("deleteGame", self.delete_game)
        self.add_command("createScore", self.create_score)
        self.add_command("readScores", self.read_scores)
        self.add_command("updateScore", self.update_score)
        self.add_command("deleteScore", self.delete_score)
        self.add_command("showRanking",self.show_rank)

    def create_player(self):
        name = input("Enter player name: ")
        country = input("Enter player country: ")
        age = input("Enter player age: ")
        player = Player(name,country,age)
        self.db.createPlayer(player)
        print("Player created successfully!")

    def read_players(self):
        players = self.db.get_players()
        for player in players:
         if player:
            name = player['p.name']
            country = player['p.country']
            age = player['p.age']
            print(f"Name: {name}\nCountry: {country}\nAge: {age}\n----------------------------------------------------")

        
    def update_player(self):
        name = input("Enter player name: ")
        new_name = input("Enter new name: ")
        self.db.updatePlayer(name, new_name)
        print("Player updated successfully!")

    def delete_player(self):
        name = input("Enter player name: ")
        self.db.deletePlayer(name)
        print("Player deleted successfully!")

    def create_game(self):
        title = input("Enter game title: ")
        genre = input("Enter game genre: ")
        debut = input("Enter game debut year: ")
        game = Game(title,genre,debut)
        self.db.createGame(game)
        print("Game created successfully!")

    def read_games(self):
        games = self.db.getGames()
        for game in games:
         if game:
            title = game['g.title']
            genre = game['g.genre']
            debut = game['g.debut']
            print(f"Title: {title}\nGenre: {genre}\nDebut Year: {debut}\n-----------------------------------------------")

    def update_game(self):
        title = input("Enter game title: ")
        new_genre = input("Enter new genre: ")
        self.db.updateGame(title, new_genre)
        print("Game updated successfully!")

    def delete_game(self):
        title = input("Enter game title: ")
        self.db.deleteGame(title)
        print("Game deleted successfully!")

    def create_score(self):
        player_name = input("Enter player name: ")
        game_name = input("Enter game name: ")
        score_value = float(input("Enter score value: "))
        score = Score(player_name,game_name,score_value)
        self.db.createScore(score)
        print("Score created successfully!")

    def read_scores(self):
      scores = self.db.readScores()
      
      for score in scores:
          if score:
              player = score['p.name']
              game = score['g.title']
              value = score['s.value']
              print(f"Player: {player}\nGame: {game}\nScore: {value}\n--------------------------------------------------")

        
    def update_score(self):
        player_name = input("Enter player name: ")
        game_name = input("Enter game name: ")
        new_score_value = float(input("Enter new score value: "))
        self.db.updateScore(player_name, game_name, new_score_value)
        print("Score updated successfully!")

    def delete_score(self):
        player_name = input("Enter player name: ")
        game_name = input("Enter game name: ")
        self.db.deleteScore(player_name, game_name)
        print("Score deleted successfully!")

    def show_rank(self):
        ranks = self.db.showRanking()

        for rank in ranks:
            if ranks:
                player = rank['p.name']
                Media = rank['average']
                print(f"Player:{player}\nMedia:{Media}\n------------------------------------------------")
