import flet as ft
import requests


def main(page: ft.Page):

    for foto in range(15):
        imagenes=ft.Image(f"https://picsum.photos/300?random={foto}",
                width=250,
                height=250
                    )

    page.scroll="auto"
    productos=requests.get("https://dummyjson.com/products").json()
    for producto in productos["products"][:30]:
       
        page.add(
            ft.Card(
                width=350,
                margin=10,
                elevation=10,
                content=ft.Container(
                    border_radius=15,
                    padding=15,
                    content=ft.Column(
                        [
                            ft.Image(producto["thumbnail"],width=350, height=180, fit=ft.BoxFit.CONTAIN),
                            ft.Text(producto["title"],size=20),
                            ft.Text(producto["description"],size=16), 
                            ft.Text(value=producto["price"],size=16, color=ft.Colors.GREEN),
                            ft.Text(producto["category"],size=16),
                            ft.CupertinoFilledButton("Comprar", icon=ft.Icons.SHOPPING_CART)

                        ]
                    )
                )
            ),

            #ft.Text(producto["title"],size=20),
            #ft.Image(producto["thumbnail"],width=300, height=300),
            #ft.Text(value=producto["price"],size=16),
            #ft.Text(producto["category"],size=16),
            #ft.Text(producto["description"],size=16)     
            # 
        #EXTRA
        imagenes
            
           

        )


ft.run(main)
