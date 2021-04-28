import asyncio
from app.app import Server

server = Server()
asyncio.run(server.run())

