from blackjack.models import Game, Player

def create_game(game_name: str, players: list[str]):
  game = Game(name=game_name)
  game.save()
  # Other method (but can't overwrite save())
  # game = Game.objects.create(name=game_name)
  
  for name in players:
    Player.objects.create(name=name, game=game)

def get_game_players(game_id: int):
  game = Game.objects.get(pk=game_id)
  players = game.players.all()
  return players

def get_winners(game_id: int):
  # Should return  all winners, closest to 21
  # Can have more than 1 winner
  game = Game.objects.get(pk=game_id)
  players = game.players.all()

  # Longer version
  # valid_players = []
  # for player in players:
  #   if player.score <= 21:
  #     valid_players.append(player)
  # Shorther version
  valid_players = [player for player in players if player.score <= 21]

  if not valid_players:
    return []
  
  max_score = max(player.score for player in valid_players)
  winners = [player for player in valid_players if player.score == max_score]

  return winners

def update_player_score(player_id: int, score: int):
  player = Player.objects.get(pk=player_id);
  player.score = score
  player.save()
  return player