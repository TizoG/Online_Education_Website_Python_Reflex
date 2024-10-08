"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from Online_Education_Website_Python_Reflex.component.navbar import navbar
# from Online_Education_Website_Python_Reflex.component.car_logins import car_logins
from Online_Education_Website_Python_Reflex.view.header.header import header

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.vstack(
            navbar(),
            header()
        ),
        bg="#FFFFFF",  # Fondo blanco para el contenedor principal
        color="#000000",  # Color del texto en negro
        width="100vw",  # Asegúrate de que el ancho abarque toda la ventana
        height="100vh",  # Asegúrate de que la altura abarque toda la ventana
        padding="0",  # Sin padding para que el contenido esté ajustado

    )


app = rx.App()
app.add_page(index)
