
import click
from api.models import db, User, Games
import json

"""
In this file, you can add as many commands as you want using the @app.cli.command decorator
Flask commands are usefull to run cronjobs or tasks outside of the API but sill in integration 
with youy database, for example: Import the price of bitcoin every night as 12am
"""
def setup_commands(app):
    
    """ 
    This is an example command "insert-test-users" that you can run from the command line
    by typing: $ flask insert-test-users 5
    Note: 5 is the number of users to add
    """
    @app.cli.command("insert-test-users") # name of our command
    @click.argument("count") # argument of out command
    def insert_test_users(count):
        print("Creating test users")
        for x in range(1, int(count) + 1):
            user = User()
            user.email = "test_user" + str(x) + "@test.com"
            user.password = "123456"
            user.is_active = True
            db.session.add(user)
            db.session.commit()
            print("User: ", user.email, " created.")

        print("All test users created")

    # $ flask insert-game-data
    @app.cli.command("insert-game-data")
    def insert_game_data():
        counter = 0
        with open("src/api/scraping/matchedGames.json") as file:
            data = json.load(file)
            for game_data in data:
                game_name = game_data.get("name")

                existing_game = db.session.query(Games).filter_by(name=game_name).first()

                if existing_game:
                    print(f"Game '{game_name}' already exists, skipping.")
                    continue

                game = Games()
                game.name = game_name
                game.app_id = game_data.get("appId")
                game.release = game_data.get("release")
                game.image_id = game_data.get("imageID")
                game.score = game_data.get("score")
                game.g2a_price = game_data.get("g2aPrice")
                game.g2a_url = game_data.get("g2aUrl")
                game.steam_price = game_data.get("steamPrice")
                game.g2a_url = game_data.get("g2aUrl")
                # game.game_tags = game_data.get("tags")

                print(game)
                counter+=1
                db.session.add(game)
                db.session.commit()
            print(f"Added {counter} games to the database")
        pass
