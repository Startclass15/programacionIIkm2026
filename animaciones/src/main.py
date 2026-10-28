import flet as ft
import flet_lottie as ftl

def main(page: ft.Page):

    animacion=ftl.Lottie(
        src="https://lottie.host/0183ac3e-6179-40d1-804f-259c74be2640/0KwrdAcHuH.json",
        width=350,
        height=350,
        animate=True
    )
    
    page.add(
        ft.Row(
            controls=[
                animacion, ft.Button("Enviar")
            ]
        ) 
        
    )


if __name__ == "__main__":
    ft.run(main)
