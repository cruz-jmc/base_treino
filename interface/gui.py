from service.services import Services

class UI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):
        # Exibir opções
        # Receber escolha do usuário
        # Chamar os métodos do service
        while True:
            
            print("====================MENU DE DOCINHOS====================")
            
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
                    
            elif (escolha == "2"):
                try:
                    lista = self.service.find_all
                    if not lista:
                        print("Sem registro")
                        
                    else:
                        print("------Lista de registros------")
                        for i in lista:
                            if i.closed:
                                feito = "Nenhum docinho feito"
                                
                            else:
                                feito = "Existem docinhos feitos"
                                
                            print(f"nome: {docinho.nome}// sabor: {docinho.sabor}// feito: {docinho.feito}")
                            
                except ValueError as error:
                    print(f"Erro: {error}")
                
            elif (escolha == "3"):
                respota = int(input("Digite o id do docinho a ser procurado: "))
                try:
                    resultado = self.services.get(resposta)
                    if not resultado:
                        print("Docinho não encontrado.")
                    print(f"id: {resultado.id}// nome: {docinho.nome}// sabor: {docinho.sabor}// feito: {docinho.feito}")
                except ValueError as error:
                    print(f"Erro: {error}")
                    
            elif (escolha == "4"):
                 
                    
                
                
                
                
                
                
                
                
                