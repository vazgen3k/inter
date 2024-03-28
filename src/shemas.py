from pydantic import BaseModel
from uuid import UUID


class UUID4Model(BaseModel):
    uuid: UUID