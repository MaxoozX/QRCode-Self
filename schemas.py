from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel

class TableMember(BaseModel):
    firstname: str
    lastname: str
    classID: str
    time: Optional[str] = None
    ID: Optional[UUID] = None

class ClassicResponseModel(BaseModel):
    status: str
    message: Optional[str] = None
    content: Optional[str] = None

class TableMembersModel(BaseModel):
    __root__: List[TableMember]

class SettleTableModel(BaseModel):
    location: str