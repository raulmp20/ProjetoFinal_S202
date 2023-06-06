class ForumDatabase:
    def __init__(self, database):
        self.db = database

    def create_user(self, name, email, password):
        query = "CREATE (:Usuario {name: $name, email: $email, senha: $password})"
        parameters = {"name": name, "email": email, "password": password}
        self.db.execute_query(query, parameters)

    def create_post(self, title, content, autor):
        query = "MATCH (u:Usuario {name: $autor}) CREATE (:Postagem {titulo: $title, conteudo: $content})<-[:POSTA]-(u)"
        parameters = {"title": title, "content": content, "autor": autor}
        self.db.execute_query(query, parameters)

    def create_forum(self, name, description, post):
        query = "MATCH (p:Postagem {titulo: $post}) CREATE (:Forum {nome: $name, descricao: $description)<-[:SOBRE]-(p)"
        parameters = {"name": name, "description": description, "post": post}
        self.db.execute_query(query, parameters)

    def get_users(self):
        query = "MATCH (u:Usuario) RETURN u.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_posts(self, autor):
        query = "MATCH (p:Postagem)<-[:POSTA]-(u:Usuario{name: $autor}) RETURN p.titulo AS titulo"
        parameters = {"autor": autor}
        results = self.db.execute_query(query, parameters)
        return [result["titulo"] for result in results]

    def get_foruns(self):
        query = "MATCH (f:Forum) RETURN f.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def update_user(self, name, newPassword):
        query = "MATCH (u:Usuario {name: $name}) SET u.senha = $newPassword"
        parameters = {"name": name, "newPassword": newPassword}
        self.db.execute_query(query, parameters)

    def update_post(self, titulo, newContent):
        query = "MATCH (p:Postagem {titulo: $titulo}) SET p.conteudo = $newContent"
        parameters = {"titulo": titulo, "newContent": newContent}
        self.db.execute_query(query, parameters)

    def update_forum(self, name, newDescription):
        query = "MATCH (f:Forum {nome: $name}) SET f.descricao = $newDescription"
        parameters = {"name": name, "newDescription": newDescription}
        self.db.execute_query(query, parameters)

    def delete_user(self, name):
        query = "MATCH (u:Usuario {nome: $name}) DETACH DELETE u"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_post(self, title):
        query = "MATCH (p:Postagem {titulo: $title}) DETACH DELETE p"
        parameters = {"title": title}
        self.db.execute_query(query, parameters)

    def delete_forum(self, name):
        query = "MATCH (f:Forum {name: $name}) DETACH DELETE f"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)