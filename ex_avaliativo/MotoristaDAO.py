from pymongo import MongoClient
from bson.objectid import ObjectId

class motoristaDAO:
    def __init__(self, database):
        self.db = database

    def create(self,motorista):
        try:
            motor = {
            "nome": motorista.nome,
            "documento": motorista.documento,
            "nota": motorista.nota,
            "corridas": [
                {
                    "nota": aux.nota,
                    "distancia": aux.distancia,
                    "valor": aux.valor,
                    "passageiro": {
                        "nome": aux.passageiro.nome,
                        "documento": aux.passageiro.documento
                    }
                } for aux in motorista.corridas
            ],
        }
            res = self.db.collection.insert_one(motor)
            print(f"Motorista criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating motorista: {e}")
            return None
        
      
    def read_motorista_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista encontrado: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading Motorista: {e}")
            return None

    def update_Motorista(self, id: str,nome:str,documento:str,nota: int):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nome":nome,"documento":documento,"nota":nota}})
            print(f"Motorista updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating Motorista: {e}")
            return None

    def delete_Motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting Motorista: {e}")
            return None