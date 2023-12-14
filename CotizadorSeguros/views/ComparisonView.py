import flet as ft
from views.AppPage import AppPage


class ComparisonView (AppPage):
    def __init__(self, root, route):
        super().__init__(root=root, route=route)        
        self.title = "COMPARACION"

    def get_page(self) -> ft.View:
        
        return self.page