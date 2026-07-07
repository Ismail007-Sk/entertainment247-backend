from pydantic import BaseModel
from typing import Literal


# For getting problem description from user.
class Message(BaseModel):
    subject:str
    description:str


# For Admin only
class Resolve_Message(BaseModel):
    status:Literal["Open", "In Progress", "Resolved", "Closed"]
    # This prevents invalid values like: "status": "abcd"

