import reflex as rx


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(
                src="/assets/logo.png",
                width="124px",
                height="77px",
                margin_x="77px",
                margin_y="43px"
            ),
            rx.hstack(
                rx.link(
                    "Inicio",
                    href="#",
                    color="black",
                    size="5",
                    weight="medium"
                ),
                rx.link(
                    "Sobre mi",
                    href="#",
                    color="black",
                    size="5",
                    weight="medium"
                ),
                rx.link(
                    "Cursos",
                    href="#",
                    color="black",
                    size="5",
                    weight="medium"
                ),
                rx.link(
                    "Contacto",
                    href="#",
                    color="black",
                    size="5",
                    weight="medium"
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
                margin_left="263px"
            ),

            align_items="center",
            padding="10px 20px"
        ),
        bg="#FFF",
        align_items="center"
    )
