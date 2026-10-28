import flet as ft
import flet_camera as fc


def main(page: ft.Page):
    camara=fc.Camera()
    imagen=ft.Container()
   
    estado=ft.Text("Iniciando la camara...")

    async def iniciar(e):
        try:
            camaras=await camara.get_available_cameras()
            if not camaras:
                estado.value="No se encontro ninguna camara"
                page.update()
                return
            await camara.initialize(
                description=camaras[0],
                resolution_preset=fc.ResolutionPreset.MEDIUM,
                enable_audio=False,
            )
            estado.value="Camara lista"
            page.update()
        except Exception as error:
            estado.value=f"Error: {error}"
            page.update()
    async def tomar_foto(e):
        try:
            datos=await camara.take_picture()
            imagen.content=ft.Image(
                width=300,
                height=300,
                fit=ft.BoxFit.CONTAIN,
                src=datos
                    
            )
            estado.value="Fotografia cargada"
            page.update()
        except Exception as error:
            estado.value=f"Error: {error}"
            page.update()

    
    page.add(
        ft.Text("Camara",size=30),
        ft.Container(
            content=camara,
            width=350,
            height=300

        ),
        ft.Row(
            controls=[
                ft.Button("Iniciar Camara", on_click=iniciar),
                ft.Button("Tomar Foto",on_click=tomar_foto)
            ],
            wrap=True,
        ),
       estado,
       imagen
    )


if __name__ == "__main__":
    ft.run(main)
