class Database:
    pass

class WriteAJson:
    pass

class ProductAnalyzer:
    def __init__(self, db: Database ):
        self.db = db

    #retorna o total de vendas por dia
    def VendasNoDia(self):
     result = self.db.collection.aggregate([
        {'$unwind': '$produtos'},
        {'$group': {'_id': {'data_compra': '$data_compra'},'total_vendas': {'$sum': {'$multiply': ['$produtos.quantidade', '$produtos.preco']}}}}
    ])

     return result
    
    #retorna o produto mais vendido em todas as compras
    def MaisVendidoDia(self):
     result = self.db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": {"data": "$data_compra", "descricao": "$produtos.descricao"}, "quantidade": {"$sum": "$produtos.quantidade"}}},
        {"$sort": {"quantidade": -1}},
        {"$group": {"_id": "$_id.data", "produto": {"$first": "$_id.descricao"}}},
    ])
   
     return result

    def ClienteMaisGastou(self):
     result = self.db.collection.aggregate([
     {"$unwind": "$produtos"},
     {"$group": {"_id": "$cliente_id", "total": {'$sum': {'$multiply': ['$produtos.quantidade', '$produtos.preco']}}}},
     {"$sort": {"total": -1}},
     {"$limit": 1}
     ])
      
     return result
    
    def ProdutoMaisDeUmVendido(self):
     result = self.db.collection.aggregate([
        { '$unwind': '$produtos' },  
        {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
        { '$match': { 'total': { '$gt': 1 } } },  
        
    ])
     return result