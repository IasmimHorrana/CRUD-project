from pydantic import BaseModel, PositiveFloat, EmailStr, validator, Field
from enum import Enum
from datetime import datetime
from typing import Optional

# Definindo uma enumeração para as categorias de produtos
class CategoriaBase(Enum):
    categoria1 = "Eletrônico"
    categoria2 = "Eletrodoméstico"
    categoria3 = "Móveis"
    categoria4 = "Roupas"
    categoria5 = "Calçados"

# Definindo um modelo base para produtos, que inclui atributos comuns a todos os produtos
class ProductBase(BaseModel):
    name: str  # Nome do produto
    description: Optional[str] = None  # Descrição do produto (opcional)
    price: PositiveFloat  # Preço do produto (deve ser um número positivo)
    categoria: str  # Categoria do produto (deve ser uma das categorias definidas em CategoriaBase)
    email_fornecedor: EmailStr  # E-mail do fornecedor (verifica se o formato é válido)

    # Validando se a categoria fornecida é válida (uma das definidas em CategoriaBase)
    @validator("categoria")
    def check_categoria(cls, v):
        if v in [item.value for item in CategoriaBase]:  # Verifica se a categoria está na lista de categorias válidas
            return v
        raise ValueError("Categoria inválida")  # Se não estiver, lança um erro

# Modelo para criar um novo produto, herda de ProductBase
class ProductCreate(ProductBase):
    pass  # Não adiciona novos atributos, apenas reutiliza os do modelo base

# Modelo para a resposta ao consultar um produto, inclui informações adicionais como ID e data de criação
class ProductResponse(ProductBase):
    id: int  # ID único do produto
    created_at: datetime  # Data e hora de criação do produto

    # Configuração que permite que este modelo trabalhe com objetos de banco de dados
    class Config:
        orm_mode = True

# Modelo para atualizar um produto, permite que qualquer campo seja opcional
class ProductUpdate(BaseModel):
    name: Optional[str] = None  # Nome do produto, opcional
    description: Optional[str] = None  # Descrição do produto, opcional
    price: Optional[PositiveFloat] = None  # Preço do produto, opcional
    categoria: Optional[str] = None  # Categoria do produto, opcional
    email_fornecedor: Optional[EmailStr] = None  # E-mail do fornecedor, opcional

    # Validação da categoria, similar à do modelo base, mas permite que seja None
    @validator("categoria", pre=True, always=True)
    def check_categoria(cls, v):
        if v is None:  # Se a categoria não for fornecida, permite seguir
            return v
        if v in [item.value for item in CategoriaBase]:  # Verifica se a categoria é válida
            return v
        raise ValueError("Categoria inválida")  # Lança erro se a categoria for inválida
