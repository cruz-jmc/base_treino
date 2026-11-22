from database.connection import get_connection

class DAOEntity:

    def create(self, docinhos):
        # Inserir no banco
        connection = get_connection()
        
        try:
            cursor = connection.execute("""INSERT INTO docinhos (nome, sabor, feito) VALUES (docinho.nome, docinho.sabor, docinho.feito)""")
            
            connection.commit()
            return cursor.lastrowid
            
            
            
        finally:
            connection.close()

    def find_all(self):
        # Consultar todas as entidades
        connection = get_connection()
        
        try:
            
            
        finally:
            connection.close()

    def find_by_id(self, docinhos_id):
        # Consultar pelo ID
        connection = get_connection()
        
        try:
            
            
        finally:
            connection.close()

    def update(self, docinhos):
        # Atualizar
        connection = get_connection()
        
        try:
            
            
        finally:
            connection.close()

    def delete(self, docinhos_id):
        # Excluir
        connection = get_connection()
        
        try:
            
            
        finally:
            connection.close()