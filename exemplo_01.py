from datetime import datetime

from pydantic import BaseModel, PositiveInt

class User(BaseModel):
    id: int
    nome: str = 'Carlos'
    assinatura_time: datetime | None
    tastes: dict[str, PositiveInt]

external_data = {
    'id': 123,
    'assinatura_time': '2019-06-01 12:22',
    'sabores': {
        'chocolate': 9,
        'morango': 7,
        'creme': '1',
    },
}

