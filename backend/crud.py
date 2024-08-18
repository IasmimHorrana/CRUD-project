from sqlalchemy.orm import Session  # Importa a classe Session do SQLAlchemy para gerenciar a comunicação com o banco de dados
from schemas import ProductUpdate, ProductCreate  # Importa os schemas de criação e atualização de produtos
from models import ProductModel  # Importa o modelo ProductModel que representa a tabela de produtos no banco de dados


def get_product(db: Session, product_id: int): #Função que recebe um ID de produto e retorna o produto correspondente do banco de dados.
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()
    # Realiza uma consulta na tabela ProductModel, filtra pelo ID, e retorna o primeiro resultado encontrado.

def get_products(db: Session): #Função que retorna todos os produtos da tabela.
    return db.query(ProductModel).all()
    # Realiza uma consulta na tabela ProductModel e retorna todos os produtos como uma lista.

def create_product(db: Session, product: ProductCreate):
    db_product = ProductModel(**product.model_dump()) # Cria uma instância do ProductModel com os dados fornecidos.
    db.add(db_product) # Adiciona o novo produto à sessão de banco de dados.
    db.commit() # Confirma a transação, salvando o novo produto no banco de dados.
    db.refresh(db_product) # Atualiza a instância db_product com os dados recém-salvos, como o ID gerado.
    return db_product # Retorna o produto criado.


def delete_product(db: Session, product_id: int): # Função que exclui um produto do banco de dados com base no seu ID.
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first() # Realiza uma consulta para encontrar o produto com o ID fornecido.
    db.delete(db_product) # Remove o produto encontrado da sessão de banco de dados.
    db.commit() # Confirma a transação, efetivamente excluindo o produto do banco de dados.
    return db_product # Retorna o produto criado.


def update_product(db: Session, product_id: int, product: ProductUpdate): # Função que atualiza as informações de um produto no banco de dados com base no seu ID.
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()  # Realiza uma consulta para encontrar o produto com o ID fornecido.
# Atualiza os campos do produto somente se os novos valores forem fornecidos.
    if db_product is None:
        return None # Retorna None se o produto não for encontrado.

    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    if product.categoria is not None:
        db_product.categoria = product.categoria
    if product.email_fornecedor is not None:
        db_product.email_fornecedor = product.email_fornecedor

    db.commit() # Confirma a transação, salvando as mudanças no banco de dados.
    return db_product # Retorna o produto atualizado.