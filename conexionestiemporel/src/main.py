import flet as ft
import requests


def main(page: ft.Page):
    page.title = "Precio del Bitcoin"

    precio = ft.Text(
        "Presiona el botón",
        size=22,
        weight=ft.FontWeight.BOLD,
        color="green"
    )

    # Función para obtener el precio
    def obtener_precio(e):
        url = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd"

        try:
            respuesta = requests.get(url)

            if respuesta.status_code == 200:
                datos = respuesta.json()
                precio.value = f"BNB: $ {datos['solana']['usd']}"
            else:
                precio.value = "Error al obtener los datos"

        except Exception as ex:
            precio.value = f"Error: {ex}"

        page.update()

    # Agregar controles a la página
    page.add(
        ft.ElevatedButton(
            "Obtener precio",
            on_click=obtener_precio
        ),
        precio
    )


ft.app(target=main)