import flet as ft

def main(page: ft.Page):

 
    def updateColor(e):
        r = int(red.value)
        g = int(green.value)
        b = int(blue.value)

        page.bgcolor = f"#{r:02x}{g:02x}{b:02x}"
        colorText.value = f"RGB({r}, {g}, {b})"

        page.update()


    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

   
    colorText = ft.Text("RGB(0, 0, 0)")

    red = ft.Slider(min=0, max=255, divisions=255, value=0, on_change=updateColor)
    green = ft.Slider(min=0, max=255, divisions=255, value=0, on_change=updateColor)
    blue = ft.Slider(min=0, max=255, divisions=255, value=0, on_change=updateColor)

    page.add(
        ft.Text("Red"), red,
        ft.Text("Green"), green,
        ft.Text("Blue"), blue,
        colorText
    )
    

ft.run(main=main)