import flet as ft

def pantalla1Vista():
    def enviarDatos():
            contenidoFormulario=nombre.value,"-",numero.value,"-",contraseña.value,"-",celular.value
            print(contenido)
    


    return ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text("Pantalla 1", size=30, color="green"),
            #Formularios
            nombre=ft.TextField(label="Ingrese su nombre: "),
            numero=ft.TextField(label="Numero"),
            contraseña=ft.TextField(label="Contraseña", password=True,can_reveal_password=True),
            celular=ft.TextField(label="Celular",keyboard_type=ft.KeyboardType.PHONE),
            botonEnviar=ft.Button("Enviar", on_click=enviarDatos)

        ],
        expand=True
       

    )

 