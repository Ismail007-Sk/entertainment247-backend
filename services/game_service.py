from models.game_model import Product
from sqlalchemy import func


def add_game(db, data):

    new_game = Product(
        game_name=data.game_name,
        price=data.price,
        story=data.story
    )

    db.add(new_game)
    db.commit()

    return new_game


def get_all_games(db):
    return db.query(Product).all()


def get_game_by_id(db, game_id):
    return db.query(Product).filter(Product.game_id == game_id).first()


def get_game_by_name(db, game_name):
    return db.query(Product).filter(Product.game_name.ilike(f"%{game_name}%")).all()


def get_games_less_price(db, price):
    return db.query(Product).filter(Product.price < price).all()


def get_games_below_price(db, price):
    return db.query(Product).filter(Product.price < price).all()


def sort_price_ascending(db):
    return db.query(Product).order_by(Product.price.asc()).all()


def sort_price_descending(db):
    return db.query(Product).order_by(Product.price.desc()).all()



def group_by_price(db):

    result = (
        db.query(Product.price,func.count(Product.game_id)).group_by(Product.price).all()
    )

    return [
        {
            "price": row[0],
            "count": row[1]
        }
        for row in result
    ]


def update_game(db, game_id, data):

    game = get_game_by_id(db, game_id)

    if game:

        game.game_name = data.game_name
        game.price = data.price
        game.story = data.story

        db.commit()

    return game


def patch_game(db, game_id, data):

    game = get_game_by_id(db, game_id)

    if game:

        if data.game_name is not None:
            game.game_name = data.game_name

        if data.price is not None:
            game.price = data.price

        if data.story is not None:
            game.story = data.story

        db.commit()
        db.refresh(game)

    return game


def delete_game(db, user_id):

    game = get_game_by_id(db, user_id)

    if game:
        db.delete(game)
        db.commit()

    return game