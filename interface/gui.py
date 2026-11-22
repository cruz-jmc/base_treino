from service.services import Services

class UI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):
        # Exibir opções
        # Receber escolha do usuário
        # Chamar os métodos do service
        while True:
            
            print("====================MENU====================")
            
            print("CADASTRAR -> 1")
            print("LISTAR -> 2")
            print("BUSCAR POR ID -> 3")
            print("ATUALIZAR -> 4")
            print("DELETAR -> 5")
            print("SAIR -> 6")
            
            escolha = input("O que deseja fazer? R:")
            
            if (escolha == "1"):
                nome = input("Nome do Docinho: ")
                sabor = input("Nome do Sabor: ")
                
                try:
                    docinho = self.repository.create(nome, sabor)
                    print(f"Docinho cadastrado com sucesso! ID: {docinho.id}")
                    
                except ValueError as error:
                    print(f"Erro: {erro}")
                    
            if (escolha == "2"):
                