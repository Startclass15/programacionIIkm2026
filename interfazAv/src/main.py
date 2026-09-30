import flet as ft
import requests
from conexion import conectar



#Firebase
firebaseConfig = {
  
}

apiKey=""


def main(page: ft.Page):
    page.scroll=ft.ScrollMode.AUTO
    conexion=conectar()
    ejecucion=conexion.cursor()
    ejecucion.execute("SELECT * FROM estudiante")
    estudiantes=ejecucion.fetchall()
    print(estudiantes)

    #Interfaz para los datos de Mysql
    tabla=ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("CodEstudiante")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Carrera")),
            ft.DataColumn(ft.Text("Celular"))
        ],
        rows=[],
        
    )
    for estudiante in estudiantes:
        tabla.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(estudiante[0]))),
                    ft.DataCell(ft.Text(str(estudiante[1]))),
                    ft.DataCell(ft.Text(str(estudiante[2]))),
                    ft.DataCell(ft.Text(str(estudiante[3]))),
                ]
            )
        )


    page.bottom_appbar=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(label="Inicio",icon=ft.Icons.HOME_MAX_ROUNDED),
            ft.NavigationBarDestination(label="Productos",icon=ft.Icons.STORE),
            ft.NavigationBarDestination(label="Servicios",icon=ft.Icons.ROOM_SERVICE),
            ft.NavigationBarDestination(label="Ajustes",icon=ft.Icons.SETTINGS),

        ],
        bgcolor=ft.Colors.GREEN_900,
        indicator_color="white",
        


    )

    correo=ft.TextField(label="Correo")
    password=ft.TextField(label="Contraseña" ,password=True)
    mensaje=ft.Text()
    

    def registrar(e):
        url=("https://identitytoolkit.googleapis.com/v1/"+"accounts:signUp?key="+firebaseConfig["apiKey"])
        datos={
            "email":correo.value,
            "password":password.value,
            "returnSecureToken":True
        }
        respuesta=requests.post(url,json=datos)

        if respuesta.status_code==200:
            mensaje.value="Usuario Registrado Correctamente"
            mensaje.color="green"
            correo.value=""
            password.value=""
        else:
            mensaje.value="Error al registrar"
            mensaje.color="red"
            correo.value=""
            password.value=""
        page.update()
    boton=ft.CupertinoFilledButton("Iniciar Sesion",icon=ft.Icons.MAIL, on_click=registrar)
    page.add(
        correo,password,mensaje,boton,
        ft.Divider(),
        ft.Row(
            [
                tabla
            ],
            scroll=ft.ScrollMode.AUTO
        ),
        ft.Divider(),
        ft.Text("Registro de Estudiantes",size=30,weight=ft.FontWeight.BOLD)

    )


if __name__ == "__main__":
    ft.run(main)
