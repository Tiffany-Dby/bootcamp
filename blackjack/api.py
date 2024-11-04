from ninja import Router, ModelSchema, Schema
from blackjack.models import Game, Player
from blackjack import services

router = Router()

class PlayerSchema(ModelSchema):
  class Meta:
    model = Player
    fields = ["id", "name", "score"]

class GameSchema(ModelSchema):
  class Meta:
    model = Game
    fields = ["id", "name", "turn", "ended"]

  players: list[PlayerSchema]


class StartGameSchema(Schema):
  name: str
  players: list[str]

@router.post("/start_game", response=GameSchema)
def start_game(request, new_game: StartGameSchema):
  # game = Game.objects.create(
  #   name=new_game.name
  # )

  # for player in new_game.players:
  #   Player.objects.create(
  #     name=player,
  #     game=game
  #   )

  # return game
  return services.create_game(new_game.name, new_game.players)

@router.get("/game/{game_id}", response=GameSchema)
def get(request, game_id: int):
  return Game.objects.get(pk=game_id)