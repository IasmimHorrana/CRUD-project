from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base  # Importa a classe base para modelos que define a conexão com o banco de dados

# Definindo o modelo ProductModel que representa a tabela "products" no banco de dados
class ProductModel(Base):
    __tablename__ = "products"  # Define o nome da tabela no banco de dados

    # Define as colunas da tabela "products"
    id = Column(Integer, primary_key=True)  # Coluna 'id' que é a chave primária, identificando de forma única cada produto
    name = Column(String)  # Coluna 'name' para armazenar o nome do produto
    description = Column(String)  # Coluna 'description' para armazenar a descrição do produto
    price = Column(Float)  # Coluna 'price' para armazenar o preço do produto (tipo numérico com ponto flutuante)
    categoria = Column(String)  # Coluna 'categoria' para armazenar a categoria do produto
    email_fornecedor = Column(String)  # Coluna 'email_fornecedor' para armazenar o e-mail do fornecedor
    created_at = Column(DateTime(timezone=True), default=func.now())  # Coluna 'created_at' para armazenar a data e hora de criação do registro

    # A função 'func.now()' define que o valor padrão para 'created_at' é a data e hora atuais
