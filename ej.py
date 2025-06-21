from kivy.app import App
from kivy.uix.button import Button
#Interfaz que al hacer click cammbia el texto
class MiApp(App):
    def build(self):
        self.boton = Button(text="Haz click aquí")
        self.boton.bind(on_press=self.cambiar_texto)
        return self.boton

    def cambiar_texto(self, instance):
        self.boton.text = "¡Gracias por hacer click!"

MiApp().run()
