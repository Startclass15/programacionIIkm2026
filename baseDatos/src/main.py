import flet as ft
import requests

projectId="tiendakhanamarka"

url=f"https://firestore.googleapis.com/v1/projects/{projectId}/databases/(default)/documents/estudiantes"


def main(page: ft.Page):
    page.scroll=ft.ScrollMode.AUTO

    nombre=ft.TextField(label="Ingrese su nombre")
    carrera=ft.TextField(label="Ingrese su carrera")
    celular=ft.TextField(label="Ingrese su celular")
    correo=ft.TextField(label="Ingrese su correo")
    lista=ft.GridView(
        expand=True,
        runs_count=3,
        max_extent=300,
        spacing=10,
        run_spacing=10,
        child_aspect_ratio=0.85
    )

    #funcion para guardar los datos
    def guardar(e):
        datos={
            "fields":{
                "nombre":{"stringValue":nombre.value},
                "carrera":{"stringValue":carrera.value},
                "celular":{"integerValue":int(celular.value)},
                "correo":{"stringValue":correo.value}
            }
        }
        requests.post(url,json=datos)
        nombre.value=""
        carrera.value=""
        celular.value=""
        correo.value=""

        mostrar()
        page.update()

    def mostrar():
        lista.controls.clear()
        respuesta=requests.get(url)
        if respuesta.status_code==200:
            documentos=respuesta.json().get("documents",[])
            for documento in documentos:
                campos=documento["fields"]
                nombreDocumento=documento["name"].split("/")[-1]
                nombreObtenido=campos["nombre"]["stringValue"]
                carreraObtenida=campos["carrera"]["stringValue"]
                celularObtenido=campos["celular"]["integerValue"]
                correoObtenido=campos["correo"]["stringValue"]
                tarjeta=ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Icon(ft.Icons.PERSON, size=35),
                                        ft.Column(
                                            controls=[
                                                ft.Text(nombreObtenido,size=18,weight=ft.FontWeight.BOLD),
                                                ft.Text(carreraObtenida,size=16)
                                            ],
                                            spacing=3,
                                            expand=True
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.START
                                ),
                                ft.Divider(),
                                ft.Row(
                                    controls=[
                                        ft.Icon(ft.Icons.PHONE),
                                        ft.Text(f"Celular: {celularObtenido}")
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Icon(ft.Icons.EMAIL),
                                        ft.Text(f"Correo: {correoObtenido}")
                                    ]
                                ),
                                ft.Row(
                                    controls=[
                                        ft.FilledButton(
                                            "Eliminar",
                                            icon=ft.Icons.DELETE,
                                            on_click=lambda e, id=nombreDocumento: eliminar(id)
                                        )
                                    ]
                                )

                            ],
                            spacing=10
                        ),
                        padding=15,
                        
                    ),
                    elevation=4,
                    margin=10

                    
                )

                lista.controls.append(tarjeta)
            page.update()
    
    def eliminar(nombreDocumento):
        urlEliminar=f"{url}/{nombreDocumento}"
        respuesta=requests.delete(urlEliminar)
        if respuesta.status_code==200:
            print("Estudiante eliminado")
            mostrar()
        else:
            print("Error no se pudo eliminar")
        page.update()

    page.add(
       ft.Text("Registro de Estudiantes",size=25),
       nombre,carrera,celular,correo,
       ft.FilledButton("Registrar",on_click=guardar),
       ft.Divider(),
       lista
    )
    mostrar()


if __name__ == "__main__":
    ft.run(main)
