from workout.contrib.schemas import BaseSchema
from pydantic import Field
from typing import Annotated

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Scale', max_length=10)]