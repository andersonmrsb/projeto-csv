from pydantic import BaseModel, ValidationError


class Netflix(BaseModel):  # VALIDAÇÃO DE DADOS COM PYDANTIC
    show_id: str
    type: str
    title: str
    director: str | None
    cast: str | None
    country: str | None
    date_added: str | None
    release_year: int
    rating: str | None
    duration: str | None
    listed_in: str | None
    description: str | None
