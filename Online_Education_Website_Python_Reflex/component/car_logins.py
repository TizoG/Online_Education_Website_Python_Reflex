import reflex as rx

# Faltan validaciones y toda la logica del login


def car_logins() -> rx.Component:
    return rx.center(
        rx.box(
            rx.vstack(
                rx.text("Login",
                        color="#262626",
                        size="9",
                        margin_top="50px",
                        weight="medium"
                        ),
                rx.text(
                    "¡Bienvenido! Por favor, inicie sesión para acceder a su cuenta.",
                    color="#262626",
                    font_size="18px",
                    weight="regular"
                ),

                rx.text(
                    "Email",
                    color="#262626",
                    align_self="flex-start",
                    font_size="18px",
                    padding_x="50px",
                    weight="medium"
                ),
                rx.input(
                    max_length=50,
                    width="1003px",
                    height="75px",
                    bg="#FCFCFD",
                    color="#656567",
                    font_size="18px",
                    border_radius="10px",
                    type="email",
                    required=True
                ),
                rx.text(
                    "Password",
                    color="#262626",
                    align_self="flex-start",
                    font_size="18px",
                    padding_x="50px",
                    weight="medium"
                ),
                rx.input(
                    max_length=50,
                    width="1003px",
                    height="75px",
                    bg="#FCFCFD",
                    color="#656567",
                    font_size="18px",
                    border_radius="10px",
                    type="password",
                    required=True
                ),
                rx.button(
                    "Login",
                    color="white",
                    bg="#000000",
                    height="63px",
                    width="1003px",
                    font_size="18px",
                    weight="medium",
                    border_radius="10px",
                    margin_top="10px",
                    transition="background 0.5s ease",  # Transición suave para el color de fondo
                    _hover={
                        "cursor": "pointer",
                        "background_color": "#666",
                        # Transición suave para el color de fondo
                        "transition": "background-color 0.5s ease"
                    }
                ),
                rx.text(
                    "OR",
                    color="#98989A"
                ),
                rx.link(
                    rx.button(
                        rx.hstack(
                            rx.image(  # No me funciona intentar cambiar si no por un icon
                                src="/assets/logo_google.png"

                            ),
                            rx.text(
                                "Login con Google",
                                font_size="18px",
                                color="#262626",
                                weight="medium"
                            )
                        ),
                        height="70px",
                        width="1003px",
                        bg="#F7F7F8",
                        border_radius="10px",
                        _hover={
                            "cursor": "pointer"
                        }
                    ),
                    href="/#",

                ),
                rx.hstack(
                    rx.text(
                        "No tienes cuenta?",
                        font_size="18px",
                        color="#262626"
                    ),
                    rx.hstack(
                        rx.link(
                            "Registrate",
                            color="#262626",
                            font_size="18px",
                        ),
                        _hover={
                            "cursor": "pointer"
                        }
                    ),
                    rx.flex(
                        rx.icon("arrow-up-right", color="#262626"),

                    )
                ),

                justify_content="center",  # Centra el texto verticalmente en el vstack
                align_items="center",       # Centra el texto horizontalmente en el vstack

            ),
            background_color="#E9E9E9",
            height="700px",
            width="1103px",
            align_items="center",  # Centra el contenido horizontalmente dentro del box
            justify_content="center",  # Centra el contenido verticalmente dentro del box
            border_radius="12px",
            box_shadow="-10px 5px 20px rgba(0, 0, 0, 0.5)"
        ),
        width="95vw",  # Para asegurarnos de que el centro abarque el ancho total de la pantalla
        height="100vh"  # Para asegurarnos de que el centro abarque el alto total de la pantalla
    )
