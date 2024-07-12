import flet as ft
import asyncio


async def main(page: ft.Page) -> None:
    page.title = 'Mandarin Clicker'
    page.theme_color = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    async def increase_score(e: ft.ContainerTapEvent) -> None:
        score.data += 1
        score.value = str(score.data)

        progress_bar.value += .01

        if score.data % 100 == 0:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value="+100 🧃",
                    size=20,
                    color='#ff8b1f',
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor='#25223a'
            )

            page.snack_bar.open = True
            progress_bar.value = 0

        image.scale = .90
        await page.update_async()
        await asyncio.sleep(0.1)
        image.scale = 1.0
        await page.update_async()        

    score = ft.Text(value='0', size=100, data=0)
    score_counter = ft.Text(size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN))
    image = ft.Image(
        src='/orange-juice.png',
        fit=ft.ImageFit.CONTAIN,
        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE)
    )
    progress_bar = ft.ProgressBar(
        value=0,
        width=page.width - 100,
        bar_height=20,
        color='#ff8b1f',
        bgcolor='#bf6524'
    )

    await page.add_async(
        score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_click=increase_score,
            margin=ft.Margin(0, 0, 0, 30)
        ),
        ft.Container(
            content=progress_bar,
            border_radius=ft.BorderRadius(10, 10, 10, 10)
        )
    )

if __name__ == '__main__':
    ft.app(target=main, view=None, assets_dir='assets', port=8000)