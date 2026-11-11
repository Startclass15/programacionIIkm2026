
import flet as ft
import flet_map as map
from flet_geolocator import Geolocator


async def main(page: ft.Page):

    page.title = "Ubicación GPS - OpenStreetMap"
    page.padding = 10

    # Textos para mostrar las coordenadas
    latitud = ft.Text("Latitud: Sin obtener")
    longitud = ft.Text("Longitud: Sin obtener")

    # Coordenadas iniciales de Oruro
    latitudInicial = -17.969500
    longitudInicial = -67.114457

    # Crear marcador inicial
    marcador = map.MarkerLayer(
        markers=[
            map.Marker(
                coordinates=map.MapLatitudeLongitude(
                    latitudInicial,
                    longitudInicial
                ),
                content=ft.Icon(
                    ft.Icons.LOCATION_ON,
                    color=ft.Colors.RED,
                    size=40
                )
            )
        ]
    )

    # Crear mapa
    mapa = map.Map(
        expand=True,
        initial_center=map.MapLatitudeLongitude(
            latitudInicial,
            longitudInicial
        ),
        initial_zoom=15,
        layers=[
            map.TileLayer(
                url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png"
            ),
            marcador
        ]
    )

    # Crear servicio GPS
    ubicacion = Geolocator()

    page.services.append(ubicacion)

    # Función para obtener ubicación
    async def obtenerUbicacion(e):

        try:

            posicion = await ubicacion.get_current_position()

            lat = posicion.latitude
            lon = posicion.longitude

            # Mostrar coordenadas
            latitud.value = f"Latitud: {lat}"
            longitud.value = f"Longitud: {lon}"

            # Centrar mapa en la ubicación actual
            mapa.center = map.MapLatitudeLongitude(lat, lon)

            # Actualizar marcador
            marcador.markers = [
                map.Marker(
                    coordinates=map.MapLatitudeLongitude(lat, lon),
                    content=ft.Icon(
                        ft.Icons.LOCATION_ON,
                        color=ft.Colors.RED,
                        size=40
                    )
                )
            ]

            page.update()

        except Exception as error:

            latitud.value = f"Error: {error}"
            page.update()

    # Interfaz
    page.add(
        ft.Button(
            "Obtener ubicación GPS",
            icon=ft.Icons.MY_LOCATION,
            on_click=obtenerUbicacion
        ),

        latitud,
        longitud,

        ft.Container(
            content=mapa,
            expand=True
        )
    )


if __name__ == "__main__":
    ft.run(main)
