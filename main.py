import flet as ft

def main(page: ft.Page):
    
    def sumar(e):
        numero = int(number.value)
        number.value = str(numero + 1)
        number.update()

    def restar(e):
        numero = int(number.value)
        number.value = str(numero - 1)
        number.update()

    boton_sumar = ft.IconButton(icon=ft.Icons.ADD, on_click=sumar)
    boton_restar = ft.IconButton(icon=ft.Icons.REMOVE, on_click=restar)
    number = ft.TextField(label="Number", value="0")
    texto = ft.Text("Contador")

    page.add(ft.Row([
             boton_sumar,
             number,
             boton_restar,
             texto
         ]))


ft.app(target=main)