from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
#Interfaz con varias opciones para elegir
class MiApp3(App):
    def build(self):
        layout = GridLayout(cols=2)
        
        self.label = Label(text="Selecciona una opción:")
        
        boton1 = Button(text="Opción 1")
        boton2 = Button(text="Opción 2")
        boton3 = Button(text="Opción 3")
        boton4 = Button(text="Opción 4")
        
        boton1.bind(on_press=lambda x: self.cambiar_texto("Elegiste la opción 1"))
        boton2.bind(on_press=lambda x: self.cambiar_texto("Elegiste la opción 2"))
        boton3.bind(on_press=lambda x: self.cambiar_texto("Elegiste la opción 3"))
        boton4.bind(on_press=lambda x: self.cambiar_texto("Elegiste la opción 4"))
        
        layout.add_widget(self.label)
        layout.add_widget(Label())  # Espacio vacío
        layout.add_widget(boton1)
        layout.add_widget(boton2)
        layout.add_widget(boton3)
        layout.add_widget(boton4)
        
        return layout
    
    def cambiar_texto(self, texto):
        self.label.text = texto

MiApp3().run()
