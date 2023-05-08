from database import Database
from crud import MatchDatabase

db = Database("bolt://52.205.252.113:7687","neo4j","leggings-bump-alphabet")
db.drop_all()

game_db = MatchDatabase(db)

game_db.create_player("Pedro")
game_db.create_player("Mysterion")
game_db.create_player("Lureka")
game_db.create_player("Waltin")

game_db.create_match(["Pedro","Lureka"],"19x17")
game_db.create_match(["Pedro","Lureka","Waltin","Mysterion"],"09x16")
game_db.create_match(["Lureka","Waltin"],"14x16")
game_db.create_match(["Mysterion"],"16x14")

game_db.update_player("Pedro","Pcf87")
game_db.delete_player("Mysterion")
print(game_db.get_players())
print(game_db.get_hist("Pcf87"))
print(game_db.get_match("19x17"))
print(game_db.get_match("09x16"))