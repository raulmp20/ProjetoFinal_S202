from database import Database
from forum_database import ForumDatabase
from cli import ForumCLI

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://100.27.15.66:7687", "neo4j", "blackboard-splitters-cry")

forumModel = ForumDatabase(db)

forumCLI = ForumCLI(forumModel)
forumCLI.run()

