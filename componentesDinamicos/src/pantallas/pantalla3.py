import flet as ft

def click():
    print("click")

def pantalla3Vista():
    return ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.CupertinoFilledButton("Prueba",on_click=click)
        ],
        expand=True
    )