from fastapi import FastAPI
from database import engine
import models
from router import router

# Criar todas as tabelas do banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir as rotas do router
app.include_router(router)

@app.get("/")
def read_root():
    return {"Hello": "World"}