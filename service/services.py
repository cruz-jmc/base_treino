from repository.dao_entity import DAOEntity
from entities.docinhos import Docinhos

class Services:

    def __init__(self, repository):
        self.repository = repository

    def create(self, nome, sabor):
        # Validar dados (MUITO IMPORTANTE!!!!!)
        # Criar entidade
        # Solicitar persistência
        if not nome or not nome.strip():
            reaise ValueError("Erro")
            
        if not sabor or not sabor.strip():
            raise ValueError("Erro")
        
        docinho = Docinhos()
        docinho.nome = nome.strip()
        docinho.sabor = sabor.strip()
        docinho.feito = False
        docinho.id = self.repository.create(bolo)
        return docinho
        

    def list(self):
        pass

    def get(self, task_id):
        pass

    def update(self, task_id, title, description):
        pass

    def delete(self, task_id):
        pass