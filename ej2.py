from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
#Interfaz q te devuelve lo que el usuario escribio
class MiApp2(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.entrada = TextInput(hint_text="Escribe algo aquí")
        self.boton = Button(text="Mostrar mensaje")
        self.etiqueta = Label(text="")
        
        self.boton.bind(on_press=self.mostrar_mensaje)
        
        layout.add_widget(self.entrada)
        layout.add_widget(self.boton)
        layout.add_widget(self.etiqueta)
        
        return layout
    
    def mostrar_mensaje(self, instance):
        texto_usuario = self.entrada.text
        self.etiqueta.text = f"Escribiste: {texto_usuario}"

MiApp2().run()
