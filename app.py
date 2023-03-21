import os
import flet
from flet import *
#import requests
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv("APIKEY")

class AppTitle(UserControl):
    def __init__(self):
        super().__init__()
        
    def InputContainer(self, width:int):
        return Container(
            width=width,
            height=40,
            bgcolor="white10",
            border_radius=8,
            padding=8,
            content=Row(
                spacing=10,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name=icons.SEARCH_ROUNDED,
                        size=17, opacity=0.8, color="white"
                    )
                ]
            )
        )
    def build(self):
        return Container(
            padding=padding.only(top=20, left=15, right=15),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Text(
                        "IMDb Movies & Shows",
                        size=15,
                        weight='bold',
                        color="white"
                        
                    ),
                    Divider(height=5, color="transparent"),
                    self.InputContainer(280),
                    Divider(height=20, color="white10")
                ]
            )
        )

def main(page:Page):
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.bgcolor = "white10"
    
    __main__ = Container(
        width=290,
        height=600,
        gradient=RadialGradient(
            center=Alignment(-0.5,-0.8),
            radius=3,
            colors=[
                "#33354a",
                "#2f3143",
                "#2f3143",
                "#292b3c",
                "#222331",
                "#222331",
                "#1a1a25",
                "#1a1b26",
                "#1a1b26",
                "#21222f",
                "#1d1e2a",
                "black",
            ]
        ),
        border_radius=30,
        border=border.all(2,"black"),
        padding=10,
        clip_behavior=ClipBehavior.HARD_EDGE,
        content=Column(
            scroll="none",
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                AppTitle(),
            ]
        )
    )
    page.add(__main__)    
    page.update()
    
    
if __name__ == "__main__":
    flet.app(target=main)
    