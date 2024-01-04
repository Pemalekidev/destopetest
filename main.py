import sys, os
import flet as ft
from des import destro 

def main(page: ft.Page):
    #maine()
    page.window_width = 600
    page.window_maximizable = False
    page.window_height = 350
    page.window_min_width = 600
    page.window_min_height = 350
    page.window_max_width = 600
    page.window_max_height = 350
    page.window_always_on_top = True
    page.window_top = 230
    page.window_left = 440
    page.title = "Aplication Petema"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER,text_size= 20, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        if int(txt_number.value) < 0:
            txt_number.value = 0

        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main, assets_dir="assets")