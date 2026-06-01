from kivy.app import App
from kivy.uix.button import Button
from plyer import camera
from pathlib import Path


class CameraApp(App):

    def tirar_foto(self, instance):
        arquivo = str(Path.home() / "foto_teste.jpg")

        camera.take_picture(
            filename=arquivo,
            on_complete=self.foto_salva
        )

    def foto_salva(self, caminho):
        if caminho:
            print(f"Foto salva em: {caminho}")
        else:
            print("Foto cancelada.")

    def build(self):
        return Button(
            text="Abrir Câmera",
            on_press=self.tirar_foto
        )


CameraApp().run()