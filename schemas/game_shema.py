from pydantic import BaseModel ,Field


class AddGame(BaseModel):
    game_name: str
    price: int = Field(gt=298)
    story: str


class AddGamePatch(BaseModel):
    game_name: str | None = None
    price: int | None = Field(default=None, gt=298)
    story: str | None = None