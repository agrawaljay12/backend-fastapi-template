from server import create_server
from routes_register import register_routes

app = create_server()
register_routes(app)
