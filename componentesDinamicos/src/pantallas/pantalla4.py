import flet as ft

def pantalla4Vista():
    return ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text("Pantalla 4", size=80, color="green")
        ],
        expand=True
    )