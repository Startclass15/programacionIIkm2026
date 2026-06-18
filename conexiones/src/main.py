import flet as ft
import requests

def main(page: ft.Page):
   page.scroll="auto"

   datos=requests.get("https://dummyjson.com/products").json()

   for producto in datos["products"][:30]:
     

    #for foto in range(20):
    page.add( #Interfaz
        ft.Text(producto["title"], size=22),
        ft.Image(producto["thumbnail"],
                 width=300,
                 height=300
                 ),
        ft.Text(value=producto["price"])
        
    )
ft.run(main)
