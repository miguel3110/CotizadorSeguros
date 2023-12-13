import flet as ft
from views.AppPage import AppPage

class FirstView(AppPage):
    def __init__(self, root, route):
        super().__init__(root=root, route=route)  
        self.title = "BIENVENIDOS"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.did_mount = self.did_mount

        
    def get_page(self) -> ft.View:
        self.page.controls = [
            ft.ResponsiveRow(
                controls=[
                    ft.Row([
                        ft.Text("BIENVENIDOS", style=ft.TextThemeStyle.DISPLAY_MEDIUM)
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([
                        ft.Image(src="https://www.uniseguros.net/hubfs/2021/LOGOS/logo_uniseguros.png")
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([
                        ft.ElevatedButton(text="Empezar a cotizar", on_click=lambda _: self.root.go('/Form'))
                    ], alignment=ft.MainAxisAlignment.CENTER)
                ]
            )
        ]
        return self.page
    
    def did_mount(self):
        pass