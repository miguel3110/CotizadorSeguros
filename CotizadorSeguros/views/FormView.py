import flet as ft
from flet import *
from views.AppPage import AppPage
from model.Client import Client

from Controllers.FormController import FormController

class FormPage (AppPage):
    def __init__(self, root, route):
        super().__init__(root=root, route=route)        
        self.title = "FORMULARIO"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.auto_scroll = True
        self.page.scroll = ft.ScrollMode.ADAPTIVE
        self.count = 1
        self.dependent_controls = ListView()
    
    def spouse_info(self, e: ControlEvent):
        if self.has_spouse.value == True:  
            self.spouse_firstname = ft.TextField(label="Primer Nombre", helper_text="Ejemplo: Juan", border=ft.InputBorder.UNDERLINE, filled=True)
            self.spouse_middlename = ft.TextField(label="Segundo Nombre - Optional", helper_text=" ", border=ft.InputBorder.UNDERLINE, filled=True)
            self.spouse_lastname = ft.TextField(label="Primer Apellido", helper_text="Ejemplo: Carrillo", border=ft.InputBorder.UNDERLINE, filled=True)
            self.spouse_dob  = ft.TextField(label="Fecha de nacimiento", helper_text="DD/MM/AAAA", border=ft.InputBorder.UNDERLINE, filled=True)
            self.spouse_idnumber = ft.TextField(label="Numero de identificaicon", helper_text="Ejemplo: 3-453-5555", border=ft.InputBorder.UNDERLINE, filled=True)
            self.spouse_idtype = ft.Dropdown(label="Tipo de documento", helper_text=" ", options=[
                                ft.dropdown.Option("Cedula"),
                                ft.dropdown.Option("Pasaporte")
                            ])
            self.spouse_age = ft.TextField(label="Edad", helper_text=" ", border=ft.InputBorder.UNDERLINE, filled=True, disabled= True)
            self.spouse_text = ft.Text("Informacion del conyugue", ft.TextStyle(weight=ft.FontWeight.BOLD), size=20)
            self.spouseinfo1 = ft.ResponsiveRow()
            self.spouseinfo1.controls.append(
                ft.Row([
                    self.spouse_text
                ])
            )
            self.spouseinfo2 = ft.ResponsiveRow()
            self.spouseinfo2.controls.append(
                ft.Row([
                    self.spouse_firstname,
                    self.spouse_middlename,
                    self.spouse_lastname
                ])
            )
            self.spouseinfo3 = ft.ResponsiveRow()
            self.spouseinfo3.controls.append(
                ft.Row([
                    self.spouse_dob,
                    self.spouse_age,
                    self.spouse_idtype,
                    self.spouse_idnumber,
                ])
            )
           
            self.page.controls.insert(3, self.spouseinfo1)
            self.page.controls.insert(4, self.spouseinfo2)
            self.page.controls.insert(5, self.spouseinfo3)
            self.page.update()
        else:
            self.page.controls.remove(self.spouseinfo1)
            self.page.controls.remove(self.spouseinfo2)
            self.page.controls.remove(self.spouseinfo3)
            self.page.update()

    def add_dependent_button(self, e: ControlEvent):
        if self.has_children.value == True:
            self.add_dependent.disabled = False
            self.dependent_controls.controls.clear()
            self.page.update()
        elif self.has_children.value == False:
            self.add_dependent.disabled = True
            self.add_dependent.value = 0
            self.count = 1
            self.dependent_controls.controls.clear()
            
            self.page.controls.remove(self.dependent_controls)
            self.page.update()
            
        

    def dependent_info(self, e: ControlEvent):
        self.add_dependent.disabled = True  
        self.dependent_firstname = ft.TextField(label="Primer Nombre", helper_text="Ejemplo: Juan", border=ft.InputBorder.UNDERLINE, filled=True)
        self.dependent_middlename = ft.TextField(label="Segundo Nombre - Optional", helper_text=" ", border=ft.InputBorder.UNDERLINE, filled=True)
        self.dependent_lastname = ft.TextField(label="Primer Apellido", helper_text="Ejemplo: Carrillo", border=ft.InputBorder.UNDERLINE, filled=True)
        self.dependent_dob  = ft.TextField(label="Fecha de nacimiento", helper_text="DD/MM/AAAA", border=ft.InputBorder.UNDERLINE, filled=True)
        self.dependent_idnumber = ft.TextField(label="Numero de identificaicon", helper_text="Ejemplo: 3-453-5555", border=ft.InputBorder.UNDERLINE, filled=True)
        self.dependent_idtype = ft.Dropdown(label="Tipo de documento", helper_text=" ", options=[
                        ft.dropdown.Option("Cedula"),
                            ft.dropdown.Option("Pasaporte")
                        ])
        self.dependent_age = ft.TextField(label="Edad", helper_text=" ", border=ft.InputBorder.UNDERLINE, filled=True, disabled= True)
        self.dependent_text = ft.Text(f"Informacion del dependiente {self.count}", ft.TextStyle(weight=ft.FontWeight.BOLD), size=20)
        self.dependentinfo1 = ft.ResponsiveRow()
        self.dependentinfo1.controls.append(
            ft.Row([
                self.dependent_text
            ])
        )
        self.dependentinfo2 = ft.ResponsiveRow()
        self.dependentinfo2.controls.append(
            ft.Row([
                self.dependent_firstname,
                self.dependent_middlename,
                self.dependent_lastname,
            ])
        )
        self.dependentinfo3 = ft.ResponsiveRow()
        self.dependentinfo3.controls.append(
            ft.Row([
                self.dependent_dob,
                self.dependent_age,
                self.dependent_idtype,
                self.dependent_idnumber
            ])
        )
        
        for x in range (int(self.add_dependent.value)):
            self.dependent_controls.controls.append(ft.Text(f"Informacion del dependiente {x+1}", ft.TextStyle(weight=ft.FontWeight.BOLD), size=20))
            self.dependent_controls.controls.append(self.dependentinfo2)
            self.dependent_controls.controls.append(self.dependentinfo3)

        self.page.controls.append(self.dependent_controls)

        self.count += 1
        self.page.update()
        
    
    def get_page(self) -> ft.View:
        self.first_name = ft.TextField(label="Primer Nombre", helper_text="Ejemplo: Juan", border=ft.InputBorder.UNDERLINE, filled=True)
        self.middle_name = ft.TextField(label="Segundo Nombre - Optional", helper_text=" ", border=ft.InputBorder.UNDERLINE, filled=True)
        self.last_name = ft.TextField(label="Primer Apellido", helper_text="Ejemplo: Carrillo", border=ft.InputBorder.UNDERLINE, filled=True)
        self.last_name2 = ft.TextField(label="Segundo Apellido - Optional", helper_text=" ", border=ft.InputBorder.UNDERLINE, filled=True)
        
        self.dob = ft.TextField(label="Fecha de nacimiento", helper_text="DD/MM/AAAA", border=ft.InputBorder.UNDERLINE, filled=True) #this should be a date picker
        self.client_age = ft.TextField(label="Edad", helper_text=" ", border=ft.InputBorder.UNDERLINE, filled=True, disabled= True)
        self.gender = ft.Dropdown(label="Sexo", helper_text=" ", options=[
            ft.dropdown.Option("Hombre"),
            ft.dropdown.Option("Mujer"),
            ft.dropdown.Option("Prefiero no especificar")
        ])
        self.id_type = ft.Dropdown(label="Tipo de documento", helper_text=" ", options=[
            ft.dropdown.Option("Cedula"),
            ft.dropdown.Option("Pasaporte")
        ])
        self.id_number = ft.TextField(label="Numero de identificacion", helper_text="Ejemplo: 3-453-5555", border=ft.InputBorder.UNDERLINE, filled=True)
        
        self.email = ft.TextField(label="Correo Electronico", helper_text="Ejemplo: Juan@email.com", border=ft.InputBorder.UNDERLINE, filled=True)
        self.company = ft.TextField(label="Lugar de Trabajo", helper_text="Ejemplo: ACP", border=ft.InputBorder.UNDERLINE, filled=True)
        self.location = ft.Dropdown(label="Dirreccion de residencia", helper_text=" ", border=ft.InputBorder.UNDERLINE, filled=True, options=[
            ft.dropdown.Option("Solo Panama"),
            ft.dropdown.Option("Panama, Centro America y Colombia"),
            ft.dropdown.Option("Internacional")
        ])
        
        self.AccountExecutive = ft.Dropdown(label="Ejecutivo de cuenta", helper_text=" ", options=[
            ft.dropdown.Option("Maria Jimenez"),
            ft.dropdown.Option("Jose Martinez"),
            ft.dropdown.Option("Lili Rojas"),
            ft.dropdown.Option("Saul Abrego"),
            ft.dropdown.Option("Andres Gutierrez")
        ])
        
        self.has_spouse = ft.Checkbox(label="Incluye conyuge", on_change=self.spouse_info)
        
        self.has_children = ft.Checkbox(label="Incluye dependiente", on_change=self.add_dependent_button)
        self.add_dependent = ft.TextField(label="Cantidad de dependientes", on_submit=self.dependent_info, disabled=True)

        self.page.controls = [
            ft.ResponsiveRow(
                controls=[
                    ft.Row([
                        self.AccountExecutive
                    ])
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.ResponsiveRow(
                controls=[
                    ft.Row([
                        ft.Text("Informacion del cliente:", ft.TextStyle(weight=ft.FontWeight.BOLD), size=20)
                    ]),
                    ft.Row([
                        self.first_name,
                        self.middle_name,
                        self.last_name,
                        self.last_name2,
                    ]),
                    ft.Row([
                        self.dob,
                        self.client_age,
                        self.gender,
                        
                    ]),
                    ft.Row([
                        self.id_type,
                        self.id_number
                    ]),
                    ft.Row([
                        self.email,
                        self.location,
                        self.company
                    ])
                ]
            ),
            ft.ResponsiveRow(
                controls=[
                    ft.Row([
                        self.has_spouse,
                    ])
                ]
            ),
            ft.ResponsiveRow(
                controls=[
                    ft.Row([
                        self.has_children,
                        self.add_dependent
                    ])
                ]
            )
        ]
        
        return self.page
    
    