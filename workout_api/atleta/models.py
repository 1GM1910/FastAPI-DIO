from datetime import datetime
#  Importa módulos e classes do SQLAlchemy para definir tipos de dados e e funções de mapeamento ORM 
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.contrib.models import BaseModel


# Definição do modelo de dados 'AtletaModel' que herda de 'BaseModel'
class AtletaModel(BaseModel):
    # Nome da tabela no banco de dados 
    __tablename__ = 'atletas'
    
    # Definição das colunas da tabela
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    
    # Relacionamento com a tabela 'CategoriaModel', a tabela 'categoria' vai possuir uma coluna que referencia a tabela 'atleta'
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atleta', lazy='selectin')
    
    # Coluna de chave estrangeira que referencia a coluna 'pk_id' da tabela 'categoria'
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))
    
    # Relacionamento com a tabela 'CentroTreinamentoModel', a tabela 'centro_treinamento' vai possuir uma coluna que referencia a tabela 'atleta'
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atleta', lazy='selectin')
    
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey('centro_treinamento.pk_id'))
    # Coluna de chave estrangeira que referencia a coluna 'pk_id' da tabela 'centro_treinamento'