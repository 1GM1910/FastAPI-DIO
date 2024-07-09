from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel


class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50),unique=True, nullable=False)
    
    # Relacionamento com a tabela 'AtletaModel', a tabela 'atleta' vai possuir uma coluna que referencia a tabela 'categorias'
    atleta: Mapped['AtletaModel'] = relationship(back_populates='categoria')