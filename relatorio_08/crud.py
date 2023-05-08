class MatchDatabase:
    def __init__(self,database):
        self.db = database

    def create_player(self,name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name as name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]
    
    def update_player(self,old_name,new_name):
        query = "Match (p:Player{name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name,"new_name": new_name}
        self.db.execute_query(query,parameters)

    def delete_player(self,name):
        query = "Match (p:Player{name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_match(self,names,result):
        query = "CREATE (:Match {result: $result})"
        parameters = {"result": result}
        self.db.execute_query(query, parameters)

        for name in names:
            query = "MATCH (m:Match{result: $result}),(p:Player{name: $name}) CREATE(p)-[:JOGOU]->(m)"
            parameters = {"result": result,"name":name}
            self.db.execute_query(query,parameters)

    def get_match(self,result):
    
        query = "MATCH (m:Match{result: $result})<-[:JOGOU]-(p:Player) return p.name as nick"
        parameters = {"result": result}
        results = self.db.execute_query(query, parameters)
        return results

    def get_hist(self,name):
        query = "MATCH (:Player{name: $name})--(m:Match) return m.result as resultado"
        parameters = {"name": name}
        results = self.db.execute_query(query,parameters)
        
        return results

    