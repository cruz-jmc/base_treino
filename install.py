from database.connection import get_connection

def install():
    connection = get_connection()

    try:
        # Criar tabela no banco de dados
        connection.execute("""CREATE TABLE IF NOT EXISTS docinhos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100) NOT NULL,
        sabor VARCHAR(100) NOT NULL, feito BOOLEAN NOT NULL DEFAULT 0""")
        
        cursor = connection.execute("""SELECT COUNT(*) FROM docinhos""")
        total = cursor.fetchone()[0]
        
        if (total == 0):
            connection.execute("""INSERT INTO docinhos (nome, sabor, feito) VALUES ("Brigadeiro", "Chocolate", False)""")
            
        
            
        
        # Inserir dados iniciais (OBRIGATÓRIO!!!!)
        
        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")