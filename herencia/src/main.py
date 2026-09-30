import flet as ft

class Persona:
    #atributos
    def __init__(self,nombre,edad,ci):
        self.nombre=nombre
        self.edad=edad
        self.ci=ci
    #acciones
    def comer(self,comida):
        return f"Esta comiendo {comida}"

    def dormir(self):
        return f"Esta durmiendo"

class Estudiante(Persona):
    def __init__(self,nombre,edad,ci,carrera,semestre):
        super().__init__(nombre,edad,ci)
        self.carrera=carrera
        self.semestre=semestre
def main(page:ft.Page):
    page.title="POO - HERENCIA"
    page.scroll=ft.Scrollbar()

    estudiantes=[
        Estudiante("Kevin Arroyo",30,1234567,"Sistemas Informaticos",6),
        Estudiante("aaa",30,1234567,"Sistemas Informaticos",6),
        Estudiante("bbb",30,1234567,"Sistemas Informaticos",6),
        Estudiante("ccc",30,1234567,"Sistemas Informaticos",6),
        Estudiante("ddd",30,1234567,"Sistemas Informaticos",6),
        Estudiante("eee",30,1234567,"Sistemas Informaticos",6),
        Estudiante("fff",30,1234567,"Sistemas Informaticos",6),
        Estudiante("gggg",30,1234567,"Sistemas Informaticos",6),
        Estudiante("hhhh",30,1234567,"Sistemas Informaticos",6),
        Estudiante("iiii",30,1234567,"Sistemas Informaticos",6)
    ]

    def notificar(estudiante):
        page.show_dialog(ft.SnackBar(content=ft.Text(estudiante)))
        print(estudiante)

    listaEstudiante=ft.ListView(
        spacing=10,
        expand=True,
        
        width=200
        
    )

    for estudiante in estudiantes:
        card=ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    "Datos Estudiante",
                                    size=25,
                                    weight=ft.FontWeight.BOLD
                                    ),
                                ft.Divider(),
                                ft.Text(f"Nombre: {estudiante.nombre}",size=18),
                                ft.Text(f"Edad: {estudiante.edad}",size=18),
                                ft.Text(f"Ci: {estudiante.ci}",size=18),
                                ft.Text(f"Carrera: {estudiante.carrera}",size=18),
                                ft.FilledButton("Comer", on_click=notificar(estudiante.comer("Pan")))
                
                                ],
                                spacing=10
                            ),
                            padding=15,
                            width=300
                                )
                    )
            
        listaEstudiante.controls.append(card)

    page.add(
        ft.Column(
            controls=[
                ft.Text("LISTA DE ESTUDIANTES", size=25, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                ft.Container(
                    content=listaEstudiante,
                    expand=True,
                    
                ),
                
            ],
            expand=True
        )
    )

ft.app(target=main)
