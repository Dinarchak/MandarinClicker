import flet as ft

async def main(page: ft.Page) -> None:
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()

ft.app(target=main)