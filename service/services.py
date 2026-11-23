from repository.dao_entity import DAOEntity
from entities.docinho import Docinho

class Services:

    def __init__(self, repository):
        self.repository = repository

    def create(self, nome, sabor):
        # Validar dados (MUITO IMPORTANTE!!!!!)
        # Criar entidade
        # Solicitar persistência
        if not nome or not nome.strip():
            raise ValueError("Erro")
            
        if not sabor or not sabor.strip():
            raise ValueError("Erro")
        
        docinho = Docinho()
        docinho.nome = nome.strip()
        docinho.sabor = sabor.strip()
        docinho.feito = False
        docinho.id = self.repository.create(docinho)
        return docinho
        

    def list(self):
        return self.repository.find_all()

    def get(self, docinho_id):
        resultado = self.repository.find_by_id(docinho_id)
        if not resultado:
            print("Não foi encontrado")
        else:
            return resultado
        

    def update(self, docinho_id, nome, sabor):
        if not docinho_id:
            raise ValueError("id não informado.")
        if not nome or not nome.strip():
            raise ValueError("nome não informado.")
        if not sabor or not sabor.strip():
            raise ValueError("sabor não informado.")

        resultado = self.repository.find_by_id(docinho_id)
        
        if not resultado:
            print("Não foi encontrado")
            return None
        
        resultado.nome = nome.strip()
        resultado.sabor = sabor.strip()
        self.repository.update(resultado)
        return resultado
        
            
            
    def delete(self, docinho_id):
        if not docinho_id:
            raise ValueError("id não encontrado.")
        
        resultado = self.repository.find_by_id(docinho_id)
        if not resultado:
            print("Não foi encontrado")
        else:
            self.repository.delete(docinho_id)
            return resultado