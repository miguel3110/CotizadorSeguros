from typing import List
import flet as ft

from model.Client import Client
from model.Dependent import Dependent
from model.Spouse import Spouse

class FormController:
    def __init__(self):
        self.clients = []

    def caputre_client(self, data: dict, root: ft.Page=None):
        client = Client(**data)
        self.clients.append(client)
        return "Informacion del cliente capturada"
    
    def capture_spouse_data(self, data: dict, root: ft.Page=None):
        if not self.clients:
            return "Necesita llenar la informacion del cliente primero"

        client = self.clients[-1]  # Assume capturing spouse data for the latest client
        spouse = Spouse(**data)
        client.spouse = spouse
        return "Informacion del conyuge capturada"

    def capture_dependent_data(self, data_list: List[dict], root: ft.Page=None):
        if not self.clients:
            return "Necesita llenar la informacion del cliente primero"

        client = self.clients[-1]
        dependents = [Dependent(**data) for data in data_list]
        client.dependents = dependents
        return "Informacion de los dependientes capturada"
