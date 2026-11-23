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
                    docinho = self.services.create(nome, sabor)
                    print(f"Docinho cadastrado com sucesso! ID: {docinho.id}")

                except ValueError as error:
                    print(f"Erro: {error}")

            elif (escolha == "2"):
                try:
                    lista = self.services.list()
                    if not lista:
                        print("Sem registro")

                    else:
                        print("------Lista de registros------")
                        for i in lista:
                            if not i.feito:
                                feito = "Nenhum docinho feito"

                            else:
                                feito = "Existem docinhos feitos"

                            print(f"id: {i.id}// nome: {i.nome}// sabor: {i.sabor}// feito: {i.feito}")

                except ValueError as error:
                    print(f"Erro: {error}")

            elif (escolha == "3"):
                resposta = int(input("Digite o id do docinho a ser procurado: "))
                try:
                    resultado = self.services.get(resposta)
                    if not resultado:
                        print("Docinho não encontrado.")
                    else:
                        print(f"id: {resultado.id}// nome: {resultado.nome}// sabor: {resultado.sabor}// feito: {resultado.feito}")
                except ValueError as error:
                    print(f"Erro: {error}")

            elif (escolha == "4"):
                docinho_id = int(input("Digite o id do docinho a ser atualizado: "))
                nome_novo = input("Digite o novo nome: ")
                sabor_novo = input("Digite o novo sabor: ")
                try:
                    self.services.update(docinho_id, nome_novo, sabor_novo)
                    print("Atualizado com sucesso.")

                except ValueError as error:
                    print(f"Erro: {error}")

            elif (escolha == "5"):
                resposta = int(input("digite o id do docinho para ser deletado: "))
                try:
                    resultado = self.services.get(resposta)
                    if not resultado:
                        print("id não encontrado.")
                    else:
                        self.services.delete(resposta)
                        print(f"Docinho deletado. id = {resultado.id}")

                except ValueError as error:
                    print(f"Erro: {error}")

            elif (escolha == "6"):
                print("Encerrando programa...")
                break