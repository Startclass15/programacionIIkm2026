import flet as ft

def pantalla2Vista():
    return ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Image(src="https://cei.es/wp-content/uploads/python-detalle.png")
        ],
        expand=True
    )