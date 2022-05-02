from ninja import NinjaAPI
from database.api import router as database_router

api = NinjaAPI()

api.add_router("/" ,database_router)

