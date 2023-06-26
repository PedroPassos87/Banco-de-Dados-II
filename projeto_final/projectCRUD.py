class ProjectCRUD:
    def __init__(self,database):
        self.db = database

    #players crud
    def createPlayer(self, player):
        query = "CREATE (:Player {name: $name, country: $country, age: $age})"
        parameters = {
        "name": player.name,
        "country": player.country,
        "age": player.age}
        self.db.execute_query(query, parameters)

    def updatePlayer(self,name,new_name):
        query = "MATCH (p:Player{name: $name}) SET p.name = $new_name"
        parameters = {"name": name,"new_name": new_name}
        self.db.execute_query(query,parameters)
    
    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name,p.age,p.country"
        results = self.db.execute_query(query)
        return results
    
    def deletePlayer(self,name):
        query = "Match (p:Player{name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)


    #game crud
    def createGame(self,game):
        query = "CREATE (:Game {title: $title, genre: $genre, debut: $debut})"
        parameters = {
            "title": game.title,
            "genre": game.genre,
            "debut": game.debut}
        self.db.execute_query(query, parameters)

    def updateGame(self,title,new_genre):
        query = "MATCH (g:Game {title: $title}) SET g.genre = $new_genre"
        parameters = {
            "title": title,
            "new_genre": new_genre
        }
        self.db.execute_query(query,parameters)

    def getGames(self):
        query = "MATCH (g:Game) return g.title,g.genre,g.debut"
        results = self.db.execute_query(query)
        return results
    
    def deleteGame(self,title):
        query = "Match (g:Game{title: $title}) DETACH DELETE g"
        parameters = {"title": title}
        self.db.execute_query(query, parameters)


    #CRUD SCORES

    def createScore(self, score):
       query = (
        "MATCH (p:Player {name: $player_name}), (g:Game {title: $game_name}) "
        "CREATE (p)-[:HAS_SCORE{value: $score_value}]->(g)"
       )
       parameters = {
        "player_name": score.player,
        "game_name": score.game,
        "score_value": score.score
       }
       self.db.execute_query(query, parameters)

    def readScores(self):
      query = (
        "MATCH (p:Player)-[s:HAS_SCORE]->(g:Game)"
        "RETURN p.name , g.title , s.value "

       )
      result = self.db.execute_query(query)
      return result

    def updateScore(self, player_name, game_name, new_score_value):
      query = (
        "MATCH (p:Player {name: $player_name})-[s:HAS_SCORE]->(g:Game {title: $game_name})"
        "SET s.value = $new_score_value"
      )
      parameters = {
        "player_name": player_name,
        "game_name": game_name,
        "new_score_value": new_score_value
      }
      self.db.execute_query(query, parameters)
      print("Score updated successfully!")


    def deleteScore(self, player_name, game_name):
      query = (
        "MATCH (p:Player {name: player_name})-[s:HAS_SCORE]->(g:Game {title: game_name})"
        "DELETE s"
       )
      parameters = {
        "player_name": player_name,
        "game_name": game_name
      }
      self.db.execute_query(query, parameters)
      print("Score deleted successfully!")

    def showRanking(self):
        query = (
           "MATCH (p:Player)-[s:HAS_SCORE]->(g:Game) "
           "WITH p, AVG(s.value) AS average "
           "RETURN p.name, average "
           "ORDER BY average DESC "
        )
        result = self.db.execute_query(query)
        return result