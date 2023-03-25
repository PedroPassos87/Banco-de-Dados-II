from database import Database
from WriteAJson import writeAJson
from exercicio import ProductAnalyzer

Db = Database(database="mercado", collection="compras")
#db.resetDatabase()

# 1.Média de gasto total:
result = Db.collection.aggregate([
     {"$unwind": "$produtos"},
     {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}, #por cliente
     {"$group": {"_id": None, "media": {"$avg": "$total"}}} #total
 ])

writeAJson(result, "Média de gasto total")

 # Cliente que mais comprou em cada dia:
result2 = Db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    {"$sort": {"_id.data": 1, "total": -1}},
    {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
 ])

writeAJson(result2, "Cliente que mais comprou em cada dia")

 # Produto mais vendido:
result3 = Db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
    {"$sort": {"total": -1}},
    {"$limit": 1}
])

writeAJson(result3, "Produto mais vendido")

aux = ProductAnalyzer(Db)

q1 = aux.VendasNoDia()
writeAJson(q1, "Vendas por dia")

q2 = aux.MaisVendidoDia()
writeAJson(q2, "Produto mais vendido no dia")

q3 = aux.ClienteMaisGastou()
writeAJson(q3, "Cliente que mais gastou em uma compra")

q4 = aux.ProdutoMaisDeUmVendido()
writeAJson(q4, "Produto que vendeu mais que um")