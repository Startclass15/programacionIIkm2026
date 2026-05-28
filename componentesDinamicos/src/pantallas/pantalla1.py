import flet as ft

def pantalla1Vista():
    return ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text("Pantalla 1", size=30)
        ],
        expand=True
    )