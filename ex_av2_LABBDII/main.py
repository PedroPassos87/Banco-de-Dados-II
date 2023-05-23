from database import Database
from cli import TeacherCLI
from teacher_crud import TeacherCRUD

_db = Database("bolt://54.174.209.136:7687","neo4j","experts-instances-limp")
db = TeacherCRUD(_db)

#QUESTAO 3
db.create_teacher('Chris Lima',1956,'189.052.396-66')
print(db.read_teacher('Chris Lima'))
db.update_teacher('Chris Lima','162.052.777-77')

#client = TeacherCLI(db)
#client.run()
