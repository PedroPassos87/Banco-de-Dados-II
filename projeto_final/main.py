from database import Database
from projectCRUD import ProjectCRUD
from project_CLI import ProjectCLI


_db = Database("bolt://54.144.67.237:7687","neo4j","lighter-entrance-centers")
db = ProjectCRUD(_db)


client = ProjectCLI(db)
client.run()
