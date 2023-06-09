from database import Database
from forum_database import ForumDatabase
from cli import ForumCLI

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.202.192.227:7687", "neo4j", "stoppers-sheds-administrations")

forumModel = ForumDatabase(db)

forumCLI = ForumCLI(forumModel)
forumCLI.run()

