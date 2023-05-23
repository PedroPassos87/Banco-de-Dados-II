from database import Database 

db = Database("bolt://54.174.209.136:7687","neo4j","experts-instances-limp")

# Escreva a consulta para buscar o professor "Renzo" e retornar o ano de nascimento e CPF
query = "MATCH (p:Teacher {name: 'Renzo'}) RETURN p.ano_nasc, p.cpf"
results = db.execute_query(query)
for result in results:
    ano_nasc = result["p.ano_nasc"]
    cpf = result["p.cpf"]
    print("Ano de nascimento: {ano_nasc}, CPF: {cpf}")


# Busque pelos professores “Teacher” cujo nome comece com a letra “M”, retorne o name e o cpf.
query2 = "MATCH (p:Teacher) WHERE p.name STARTS WITH 'M' RETURN p.name, p.cpf"
results2 = db.execute_query(query2)

for result in results2:
    name = result["p.name"]
    cpf = result["p.cpf"]
    print(f"Name: {name}, CPF: {cpf}")

#Busque pelos nomes de todas as cidades “City” e retorne-os.
query3 = "MATCH (p:City) RETURN p.name"
results3 = db.execute_query(query3)

for result in results3:
    name = result["p.name"]
    print(f"Name: {name}")

#Busque pelas escolas “School”, onde o number seja maior ou igual a 150 e menor ou igual a 550, retorne o nome da escola, o endereço e o número
query4 = "MATCH (p:School) WHERE p.number>=150 and p.number<=550 RETURN p.name, p.address, p.number"
results4 = db.execute_query(query4)

for result in results4:
    name = result["p.name"]
    endereco = result["p.address"]
    num = result["p.number"]
    print(f"Name: {name}, Endereco: {endereco}, Numero: {num}")

#Encontre o ano de nascimento do professor mais jovem e do professor mais velho
query5 = "MATCH (p:Teacher) RETURN MAX(p.ano_nasc) as novo,MIN(p.ano_nasc) as velho"
result5 = db.execute_query(query5)

for result in result5:
    j = result["novo"]
    v = result["velho"]
    print(f"Mais novo nasceu em: {j}, mais velho nasceu em: {v}")

#Encontre a média aritmética para os habitantes de todas as cidades, use a propriedade “population”.
query6 = "MATCH (p:City) RETURN AVG(p.population) AS media, p.name as nome"
result6 = db.execute_query(query6)

for result in result6:
    media = result["media"]
    nome = result["nome"]
    print(f"Cidade:{nome}, Media aritmetica:{media}")

#Encontre a cidade cujo CEP seja igual a “37540-000” e retorne o nome com todas as letras “a” substituídas por “A” .
query7 = "MATCH (p:City {cep: '37540-000'}) RETURN REPLACE(p.name, 'a', 'A') AS ans"
result7 = db.execute_query(query7)

for result in result7:
    cidade = result["ans"]
    print(f"Cidade:{cidade}")

#Para todos os professores, retorne um caractere, iniciando a partir da 3ª letra do nome.
query8 = "MATCH (p:Teacher) RETURN SUBSTRING(p.name, 3, 1) AS letra"
result8 = db.execute_query(query8)

for result in result8:
    caracter = result["letra"]
    print(f"Caractere:{caracter}")