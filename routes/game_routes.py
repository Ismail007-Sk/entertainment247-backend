from services import game_service
from database.database import SessionLocal
from fastapi import APIRouter
from schemas.game_shema import AddGame,AddGamePatch
from fastapi import Depends
from utils.role_checker import check_role

router = APIRouter()

# CREATE POST
@router.post("/game_info")
def add_game(data: AddGame):

    db = SessionLocal()

    game_service.add_game(db, data)
    return {"message":"new game added successfully"}



# GET ALL GET
@router.get("/game_info")
def get_all_games(user=Depends(check_role("user","admin"))):
    # print(user)
    db = SessionLocal()

    return game_service.get_all_games(db)


# GET BY ID
@router.get("/game_info/id/{game_id}")
def get_game_by_id(game_id: int):

    db = SessionLocal()

    return game_service.get_game_by_id(db, game_id)


# GET BY NAME
@router.get("/game_info/name/{name}")
def get_game_by_name(name: str):

    db = SessionLocal()

    return game_service.get_game_by_name(db, name)


# GAMES LESS PRICE
@router.get("/game_info/price_less/{price}")
def price_above(price: int):

    db = SessionLocal()

    return game_service.get_games_less_price(db, price)


# SORT ASC
@router.get("/game_info/sort/asc")
def sort_asc():

    db = SessionLocal()

    return game_service.sort_price_ascending(db)


# SORT DESC
@router.get("/game_info/sort/desc")
def sort_desc():

    db = SessionLocal()

    return game_service.sort_price_descending(db)



# GROUP BY PRICE
@router.get("/game_info/group/price")
def price_group():

    db = SessionLocal()

    return game_service.group_by_price(db)


# PUT 
@router.put("/game_info/{game_id}")
def update_game(game_id: int, data: AddGame):

    db = SessionLocal()

    game_service.update_game(db, game_id, data)
    return {"message":"game updated successfully"}


# PATCH
@router.patch("/game_info/{game_id}")
def patch_game(game_id: int, data: AddGamePatch):

    db = SessionLocal()

    game_service.patch_game(db, game_id, data)
    return {"message":"game edited successfully"}


# DELETE
@router.delete("/game_info/{game_id}")
def delete_game(game_id: int):

    db = SessionLocal()

    game_service.delete_game(db, game_id)
    return {"message":"game deleted successfully"}