import flet as ft #Importacion del framework


def main(page: ft.Page): #Funcion principal 
    page.title="Mi App" 
    page.add( #Interfaz grafica
        #Botones
        ft.Button("Boton"),
        ft.FilledButton("Boton Prueba",bgcolor="brown"),
        ft.CupertinoButton("Boton 3"),
        ft.CupertinoFilledButton("Boton 4"),

        #Imagenes
        ft.Image(src="https://ellibrodepython.com/assets/images/el-libro-de-python.png", width=150),

        #Textos
        ft.Text("Componentes",size=45,color="red"),

        #iconos
        ft.IconButton(icon=ft.Icons.ADD_LOCATION_ALT_OUTLINED)
    )

    #Crear una interfaz grafica
    #TITULO: NOMBRE COMPLETO
    #IMAGEM
    #BOTONES


ft.run(main)
