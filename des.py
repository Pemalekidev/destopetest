from time import sleep
import flet as ft

def destro(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.window_width = 600
    page.window_height = 350
    page.window_min_width = 600
    page.window_min_height = 350
    page.window_max_width = 600
    page.window_max_height = 350
    page.window_always_on_top = True
    page.window_top = 230
    page.window_left = 440
    
    #page.bgcolor = ft.colors.YELLOW_600
    
    pb = ft.ProgressBar(width=550)
    page.add(
        ft.Row(
            [
               ft.Image(src=f"./assets/logo.png", width=200,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),),
               ft.Text("Petema M. 2023...", weight=ft.FontWeight.BOLD,),
               ft.Text(
                    spans=[
                        ft.TextSpan(
                            "B-Power",
                            ft.TextStyle(
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                foreground=ft.Paint(
                                    gradient=ft.PaintLinearGradient(
                                        (0, 20), (150, 20), [ft.colors.RED, ft.colors.YELLOW]
                                    )
                                ),
                            ),
                        ),
                    ],
                )

            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        
        ft.Column([ ft.Text("Chargement en cours..."), pb]),
)
    for i in range(0, 101):
        pb.value = i * 0.01
        sleep(0.25)
        page.update()
    page.window_destroy()
    
    

ft.app(target=destro, assets_dir="assets")