import reflex as rx


def header() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.heading(
                    "La educación de calidad es la clave para el éxito de tu futuro.",
                    font_size="73px",
                    weight="bold",
                    line_height="1.2",
                    margin_top="146px"
                ),

                rx.text(
                    """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.""",
                    color="#000000",
                    font_size="14px",
                    weight="regular",
                ),
                rx.link(
                    rx.button(
                        "Consulta gratis.",
                        width="300px",
                        height="52px",
                        border_radius="62px",
                        bg="#000",
                        color="#FFF",
                        font_size="22px",
                        margin_top="40px"
                    ),
                    href="#"
                ),
                max_height="275px",
                max_width="769px",
                margin_left="72px",
                spacing="7"
            ),
            # CARDS
            rx.vstack(
                rx.hstack(
                    rx.flex(
                        rx.card(
                            rx.vstack(
                                rx.image(
                                    src="/logo_card1.png",
                                    height="auto",
                                    widht="auto"
                                ),
                                rx.text(
                                    "10000+",
                                    color="white",
                                    font_size="22px"
                                ),
                                rx.text(
                                    "Estudiantes que finalizaron el curso este anio.",
                                    color="white",
                                    font_size="10px"
                                ),
                                rx.image(
                                    src="/assets/img_card1.png",
                                    height="13px",
                                    width="36px"
                                ),
                                rx.hstack(
                                    rx.text("40.000", color="white",
                                            font_size="10px"),
                                    rx.text("60.000", color="white",
                                            font_size="10px"),
                                    rx.text("1.000.000", color="white",
                                            font_size="10px")
                                ),
                            ),
                            bg="#000",
                            height="213px",
                            width="213px",
                            border_radius="31px",
                            padding="20px",
                            box_shadow="10px 5px 20px rgba(0, 0, 0, 0.5)"
                        ),

                    ),
                    rx.flex(
                        rx.card(
                            rx.vstack(
                                rx.image(
                                    src="/logo_card1.png",
                                    height="auto",
                                    widht="auto"
                                ),
                                rx.text(
                                    "Projectos Reales",
                                    color="#000",
                                    font_size="22px"
                                ),
                                rx.text(
                                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ",
                                    color="#000",
                                    font_size="10px"
                                ),


                            ),
                            bg="transparent",
                            height="213px",
                            width="213px",
                            border_radius="31px",
                            padding="20px",
                            box_shadow="10px 5px 20px rgba(0, 0, 0, 0.5)"
                        ),
                        margin_top="56px"
                    ),
                ),
                rx.vstack(
                    rx.hstack(
                        rx.flex(
                            rx.card(
                                rx.vstack(
                                    rx.image(
                                        src="/logo_card1.png",
                                        height="auto",
                                        widht="auto"
                                    ),
                                    rx.text(
                                        "Intership",
                                        color="#000",
                                        font_size="22px"
                                    ),
                                    rx.text(
                                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.",
                                        color="#000",
                                        font_size="10px"
                                    ),


                                ),
                                bg="transparent",
                                height="213px",
                                width="213px",
                                border_radius="31px",
                                padding="20px",
                                box_shadow="10px 5px 20px rgba(0, 0, 0, 0.5)"
                            ),

                        ),
                        rx.flex(
                            rx.card(
                                rx.vstack(
                                    rx.image(
                                        src="/logo_card1.png",
                                        height="auto",
                                        widht="auto"
                                    ),
                                    rx.text(
                                        "Nuevos Cursos",
                                        color="white",
                                        font_size="22px"
                                    ),
                                    rx.text(
                                        "Disenio Grafico",
                                        color="white",
                                        font_size="10px"
                                    ),


                                    rx.text("Disenio Web", color="white",
                                            font_size="10px"),
                                    rx.text("Ui/Ux Disenio", color="white",
                                            font_size="10px"),
                                    rx.text("Web devlopement", color="white",
                                            font_size="10px")

                                ),
                                bg="#000",
                                height="213px",
                                width="213px",
                                border_radius="31px",
                                padding="20px"
                            ),
                            margin_top="56px"
                        ),
                    ),
                    margin_top="-40px"

                ),
                margin_left="429px",
                margin_top="146px"

            )
        )
    )
