import flet as ft
import flet_video as ftv
import flet_audio as fa

def main(page: ft.Page):

    #componentes Interfaz
    reproductorVideo=ftv.Video(autoplay=True, expand=True,show_controls=True,
            playlist=[
        ftv.VideoMedia("https://user-images.githubusercontent.com/28951144/229373720-14d69157-1a56-4a78-a2f4-d7a134d7c3e9.mp4"),
               
    ])

    reproductorAudio=fa.Audio(
        
        src="audio.mp3",
        autoplay=True,
        volume=1.0


                               )

    page.add(
        reproductorVideo

        
    )

ft.run(main)
