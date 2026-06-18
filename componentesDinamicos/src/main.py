import flet as ft
#Conexion dinamica
from pantallas.pantalla1 import pantalla1Vista
from pantallas.pantalla2 import pantalla2Vista
from pantallas.pantalla3 import pantalla3Vista
from pantallas.pantalla4 import pantalla4Vista


def main(page: ft.Page):
    #cabecera principal
    page.appbar=ft.AppBar(
        title="Componentes Dinamicos",
        bgcolor="orange",
        center_title=True
    )

    contenido=ft.Container(expand=True)
    pantallas=[
        pantalla1Vista(),
        pantalla2Vista(),
        pantalla3Vista(),
        pantalla4Vista()
    ]
    def cambioPantalla(x):
        contenido.content=pantallas[x.control.selected_index]
        page.update()


    page.bottom_appbar=ft.NavigationBar(
        selected_index=0,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME,label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.STORE,label="Productos"),
            ft.NavigationBarDestination(icon=ft.Icons.GPS_FIXED,label="Ubicacion"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS,label="Ajustes")
        ],
        bgcolor="cyan",
        on_change=cambioPantalla
    )
    contenido.content=pantallas[0]
    
    
    page.add(
        contenido
    )


ft.run(main)
