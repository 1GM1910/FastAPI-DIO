from uuid import uuid4 # é usado para gerar um identificador único (UUID) de forma aleatória.
from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUD

# Definição da classe base 'BaseModel' usando SQLAlchemy ORM
class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUD(as_uuid=True), default=uuid4, nullable=False)