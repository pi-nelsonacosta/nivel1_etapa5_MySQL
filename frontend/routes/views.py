import httpx
from fasthtml.common import *  # Importa los elementos básicos de FastHTML
from fasthtml.components import AX, Div, H1, P, Titled, Container, Card, Button  # Importa los componentes necesarios
from frontend.components.forms import login_form  # Importa los formularios personalizados
from fastapi import APIRouter, Request

def setup_routes(frontend_app):

    @frontend_app.route("/login", methods=["GET"])
    def show_login():
        return Titled("Login", Div(
            login_form()
        ))

    @frontend_app.route("/user/token", methods=["POST"])
    async def process_login(request):
        form_data = await request.form()
        username = form_data.get("username")
        password = form_data.get("password")

        async with httpx.AsyncClient() as client:
            response = await client.post("http://localhost:8000/user/token", data={"username": username, "password": password})

            # Captura el mensaje del backend
            data = response.json()
            message = data.get("message", "Something went wrong.")

            # Si ocurre un error, muestra el mensaje de error devuelto por el backend
            if response.status_code != 200:
                print('Estoy dentro del response')
                return Titled("Login", Div(
                    P(message, style="color: red; text-align: center;"),
                    login_form()
                ))

            # Si la autenticación es exitosa, muestra el token y un mensaje de éxito
            token = data.get("access_token", "No se pudo obtener el token")
            success_message = data.get("message", "Login successful")

        # Mostrar el token en la pantalla dentro del frontend
        token_display = Card(
            Div(
                H1("Tu Token de Acceso", style="color: #4CAF50; text-align: center;"),
                P(success_message, style="font-weight: bold;"),
                P(token, style="word-wrap: break-word; background-color: #f4f4f4; padding: 15px; border-radius: 5px;"),
                style="padding: 20px; max-width: 600px; margin: auto; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);"
            )
        )

        # Botón para volver a la página de inicio o realizar otra acción
        return_button = Div(
            AX("Volver a Inicio", href="/frontend/login", cls="button", style="text-align: center; display: block; margin-top: 20px;")
        )

        # Retorna la página con el token mostrado en el frontend
        return Titled("Token de Acceso", Container(token_display, return_button))

