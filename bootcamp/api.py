from ninja import NinjaAPI
from blackjack.api import router as blackjack_router
from polls.api import router as polls_router

api = NinjaAPI()

api.add_router("/blackjack/", blackjack_router)
api.add_router("/polls/", polls_router)