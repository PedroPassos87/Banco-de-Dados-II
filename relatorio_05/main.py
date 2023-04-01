from database import Database
from WriteAJson import writeAJson
from livroModel import LivroModel
from cli import LivroCLI

db = Database(database="database", collection="livros")
livroModel = LivroModel(database=db)


livroCLI = LivroCLI(livroModel)
livroCLI.run()