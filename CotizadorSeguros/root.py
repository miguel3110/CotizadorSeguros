import flet as ft
from views.AppPage import AppPage
from views.FormView import FormPage
from views.FirstView import FirstView
#from views.ComparisonView import ComparisonView

def main(page: ft.Page):
    pages: list[AppPage] = [
        FirstView(root=page, route='/'),
        FormPage(root=page, route='/Form'),
        #ComparisonView(root=page, route='/Comparison')
    ]
    page.title = "COTIZADOR - BETA/DUMMY/PRUEBA/COMO LE QUIERAS DECIR"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def route_change(_):
        page.views.clear()
        print(pages[0].page.route)

        sel = tuple(filter(lambda x: x.page.route == page.route, pages))
        if sel:
            page.views.append(sel[0].get_page())
            page.go(sel[0].page.route)
        else:
            print(f"No page founf dor route: {page.route}")
    
    page.on_route_change = route_change
    page.go(page.route)