from database import Database
from helper.WriteAJson import writeAJson
from pokedex import Pokedex


#exercicio exemplo
Db = Database(database="pokedex", collection="pokemons")
pokemon = Db.collection.find_one({"name": "Bulbasaur"})
writeAJson(pokemon,"pokemon")


aux = Pokedex(Db)

q1 = aux.acharPokemonNome('Mew')
writeAJson(q1,"acharPorNome")

fraquezas = ["Fire", "Flying"]
q2 = aux.acharFraqueza(fraquezas)
writeAJson(q2,"acharPorFraqueza")

tipos = ["Fire","Water"]
q3 = aux.acharPokemonsTipos(tipos)
writeAJson(q3,"acharPorTipo")

q4 = aux.distanciaOvo("2 km")
writeAJson(q4,"ovo2km")

q5 = aux.distanciaOvo("5 km")
writeAJson(q5,"ovo5km")

q6 = aux.numeroPokedex("012")
writeAJson(q6,"acharPorNumero")