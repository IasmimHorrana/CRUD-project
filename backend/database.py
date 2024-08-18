from sqlalchemy import create_engine  # Importa a função para criar a conexão com o banco de dados
from sqlalchemy.orm import declarative_base  # Importa a função para definir a base dos modelos
from sqlalchemy.orm import sessionmaker  # Importa a função para criar sessões de banco de dados

# Define a URL de conexão com o banco de dados PostgreSQL
POSTGRES_DATABASE_URL = "postgresql://user:password@postgres/mydatabase"

# Cria o mecanismo (engine) de conexão com o banco de dados usando a URL definida
engine = create_engine(POSTGRES_DATABASE_URL)

# Cria uma classe de sessão configurada com o engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria a classe base para os modelos ORM (Object-Relational Mapping)
Base = declarative_base()

# Função que fornece uma sessão de banco de dados para ser usada em operações
def get_db():
    db = SessionLocal()  # Cria uma nova sessão de banco de dados
    try:
        yield db  # Fornece a sessão para ser usada no contexto do código
    finally:
        db.close()  # Fecha a sessão para liberar os recursos, independentemente de erro ou sucesso
