from ast import List
from model.Client import Client
import datetime

class ClientService:
    def __init__(self):
        # In a real scenario, you might connect to a database here
        # For simplicity, we'll use a list to store clients
        self.clients: List[Client] = []

    