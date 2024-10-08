import reflex as rx


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(
                src="/logo.png",
                width="124px",
                height="77px",
                margin_x="77px",

            ),
            rx.hstack(
                rx.link(
                    rx.button(
                        "Inicio",
                        color="black",
                        font_size="22px",
                        weight="medium",
                        bg="transparent",
                        _hover={
                            "bg": "black",
                            "color": "#FFF",
                            "text_decoration": "none",
                            "cursor": "pointer"
                        }
                    ),
                    href="#",
                ),
                rx.link(
                    rx.button(
                        "Conocenos",
                        color="black",
                        font_size="22px",
                        weight="medium",
                        bg="transparent",
                        _hover={
                            "bg": "black",
                            "color": "#FFF",
                            "text_decoration": "none",
                            "cursor": "pointer"
                        }
                    ),
                    href="#",
                ),
                rx.link(
                    rx.button(
                        "Cursos",
                        color="black",
                        font_size="22px",
                        weight="medium",
                        bg="transparent",
                        _hover={
                            "bg": "black",
                            "color": "#FFF",
                            "text_decoration": "none",
                            "cursor": "pointer"
                        }
                    ),
                    href="#",
                ),
                rx.link(
                    rx.button(
                        "Contacto",
                        color="black",
                        font_size="22px",
                        weight="medium",
                        bg="transparent",
                        _hover={
                            "bg": "black",
                            "color": "#FFF",
                            "text_decoration": "none",
                            "cursor": "pointer"
                        }
                    ),
                    href="#",
                ),
                spacing="59px",
                margin_left="300px",

            ),
            rx.hstack(
                rx.flex(
                    rx.link(
                        rx.button(
                            "Log in",
                            border_radius="43px",
                            width="101px",
                            height="39px",
                            bg="black",
                            color="white",
                            weight="medium",
                            _hover={
                                "color": "black",
                                "bg": "white",
                                "border": "1px solid black",
                                "cursor": "pointer"
                            }
                        ),
                    ),
                    rx.button(
                        "Join For Free",
                        border_radius="43px",
                        width="177px",
                        height="39px",
                        bg="black",
                        color="white",
                        weight="medium",
                        _hover={
                            "color": "black",
                            "bg": "white",
                            "border": "1px solid black",
                            "cursor": "pointer"
                        }
                    ),
                    spacing="15px"
                ),
                margin_left="auto",
                margin_right="78px"
            ),

            align_items="center",

        ),
        bg="#FFF",
        align_items="center",
        width="100%",
        height="77px",
        margin_top="43px",

    )
