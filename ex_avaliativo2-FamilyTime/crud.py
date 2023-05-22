class MatchDatabase:
    def __init__(self,database):
        self.db = database

    def getPais(self,nome:str):
        query = "MATCH (n:Pessoa{nome: $nome})<-[:PAI_DE]-(p:Pessoa) return p.nome as nome"
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        return [result["nome"] for result in results]

    def getFilhos(self,nome:str):
        query = "match (n:Pessoa{nome: $nome})-[:PAI_DE]->(p:Pessoa) return p.nome as nome"
        parameters = {"nome": nome}
        results = self.db.execute_query(query,parameters)
        return [result["nome"] for result in results]
    
    def getirmao(self,nome:str):
        query = "MATCH (p1{nome: $nome})-[:IRMAO_DE]-(p2) RETURN p2.nome as nome"
        parameters = {"nome": nome}
        results = self.db.execute_query(query,parameters)
        return [result["nome"] for result in results]

    def getPets(self):
        query = "MATCH (p:Pet) return p.nome as nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]
    
    def getDono(self,nome:str):
        query = "MATCH (n:Pet{nome: $nome})<-[:DONO_DE]-(p:Pessoa) return p.nome as nome"
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        return [result["nome"] for result in results]

    def getCasamentoTempo(self,nome:str):
        query = "MATCH (p1{nome: $nome})-[r:CASADO_COM]-(p2) RETURN r.tempo as tempo"
        parameters = {"nome": nome}
        results = self.db.execute_query(query,parameters)
        return [result["tempo"] for result in results]
    
    def getCasamento(self,nome:str):
        query = "MATCH (p1{nome: $nome})-[r:CASADO_COM]-(p2) RETURN p2.nome as nome"
        parameters = {"nome": nome}
        results = self.db.execute_query(query,parameters)
        return [result["nome"] for result in results]
    
    def getProfissao(self,nome:str):
        try:
            query = "MATCH (p:Pessoa{nome: $nome}) WITH p, labels(p) AS allLabels RETURN allLabels[1] AS profissao"
            parameters = {"nome": nome}
            results = self.db.execute_query(query,parameters)
            return [result["profissao"] for result in results]
        except Exception as e:
            print(f"An error occurred while creating livro: {e}")
            return None
    
    def getIdade(self,nome:str):
        query = "MATCH (p{nome: $nome}) return p.idade as idade"
        parameters = {"nome": nome}
        results = self.db.execute_query(query,parameters)
        return [result["idade"] for result in results]

    def getSexo(self,nome:str):
        query = "MATCH (p{nome: $nome}) return p.sexo as sexo"
        parameters = {"nome": nome}
        results = self.db.execute_query(query,parameters)
        return [result["sexo"] for result in results]