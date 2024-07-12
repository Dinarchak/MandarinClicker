import flet as ft

async def main(page: ft.Page) -> None:
    page.title = 'Mandarin Clicker'
    page.theme_color = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    score = ft.Text(value='0', size=100, data=0)
    score_counter = ft.Text(size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN))
    image = ft.Image()

    page.update()

ft.app(target=main)

if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER)