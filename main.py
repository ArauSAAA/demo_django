import flet as ft

def main(page: ft.Page):
    
    boton = ft.Button(text="Click Me")

    page.add(ft.Text("Hello, World!"),
             boton)


ft.app(target=main)