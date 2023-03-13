class Database:
    pass

class Pokedex:
    def __init__(self, db: Database ):
        self.db = db

    
    def acharPokemonNome(self,nome: str):
        return self.db.collection.find_one({"name": nome})
       
    def acharPokemonsTipos(self, tipos: list):
        return self.db.collection.find({"type":{"$in": tipos}})
        
    def acharFraqueza(self,fraquezas: list):
        return self.db.collection.find({"weaknesses": {"$all": fraquezas}})

    def numeroPokedex(self, numero: str):
        return self.db.collection.find({"num": numero})
    
    def distanciaOvo(self, dist: str):
        return self.db.collection.find({"egg": dist})         
 


