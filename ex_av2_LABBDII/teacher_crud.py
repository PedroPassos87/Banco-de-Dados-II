class TeacherCRUD:
    def __init__(self,database):
        self.db = database

    def create_teacher(self,name,ano_nasc,cpf):
        query = "CREATE (:Teacher {name: $name,ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name,"ano_nasc": ano_nasc,"cpf": cpf}
        self.db.execute_query(query, parameters)

    def read_teacher(self,name):
        query = "MATCH (p:Teacher{name: $name}) RETURN p.name,p.ano_nasc,p.cpf"
        parameters = {"name": name}
        results = self.db.execute_query(query,parameters)
        return results
    
    def update_teacher(self,name,new_cpf):
        query = "Match (p:Teacher{name: $name}) SET p.cpf = $new_cpf"
        parameters = {"name": name,"new_cpf": new_cpf}
        self.db.execute_query(query,parameters)

    def delete_teacher(self,name):
        query = "Match (p:Teacher{name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
