from database import Database
from crud import MatchDatabase
from cli import MatchDatabaseClient

db = Database("bolt://54.89.135.189:7687","neo4j","canals-magazines-alcoholism")
familydb = MatchDatabase(db)
client = MatchDatabaseClient(familydb)
client.run()

