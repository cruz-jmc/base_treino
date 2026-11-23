from database.connection import get_connection
from entities.docinhos import Docinhos

class DAOEntity:

    def create(self, docinho):
        # Inserir no banco
        connection = get_connection()
        
        try:
            cursor = connection.execute("""INSERT INTO docinho (nome, sabor, feito) VALUES (docinho.nome, docinho.sabor, docinho.feito)""")
            
            connection.commit()
            return cursor.lastrowid
            
            
            
        finally:
            connection.close()

    def find_all(self):
        # Consultar todas as entidades
        connection = get_connection()
        
        try:
            cursor = connection.execute("SELECT * FROM docinho")
            lista = cursor.fetchall
            
            registros = []
            
            for registro in lista:
                docinho = Docinho()
                docinho.id = registro[0]
                docinho.nome = registro[1]
                docinho.sabor = registro[2]
                docinho.feito = bool(registro[3])
                
                registros.append(docinho)
            return registros
            
        finally:
            connection.close()

    def find_by_id(self, docinho_id):
        # Consultar pelo ID
        connection = get_connection()
        
        try:
            cursor = connection.execute("SELECT * FROM docinho WHERE id =?" (bolo_id,))
            
            registro = cursor.fetchone()
            
            docinho = Docinho()
            docinho.id = registro[0]
            docinho.nome = registro[1]
            docinho.sabor = registro[2]
            docinho.feito = bool(registro[3])
            
            return docinho
            
            
        finally:
            connection.close()

    def update(self, docinho):
        # Atualizar
        connection = get_connection()
        
        try:
            connection.execute("""UPDATE docinho SET nome =?, sabor=?, feito=? WHERE id=?""", (docinho.nome, docinho.sabor, docinho.feito, docinho.id))
            connection.commit()            
            
        finally:
            connection.close()

    def delete(self, docinho_id):
        # Excluir
        connection = get_connection()
        
        try:
            
            
        finally:
            connection.close()