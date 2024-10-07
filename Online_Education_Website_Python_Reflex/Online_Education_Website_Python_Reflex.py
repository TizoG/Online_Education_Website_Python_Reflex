"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from Online_Education_Website_Python_Reflex.component.navbar import navbar

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return navbar()


app = rx.App()
app.add_page(index)
