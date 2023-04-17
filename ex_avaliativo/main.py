from database import Database
from MotoristaDAO import motoristaDAO
from cli import MotoristaCLI

db = Database(database="atlas-cluster", collection="motoristas")
MotoristaDAO = motoristaDAO(database=db)

MotoristaCLI = MotoristaCLI(MotoristaDAO)
MotoristaCLI.run()