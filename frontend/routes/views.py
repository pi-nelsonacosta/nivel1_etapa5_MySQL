# frontend/routes/views.py

from fasthtml.common import *  # Importa los elementos básicos de FastHTML
from fasthtml.components import AX, Div, H1, H2, Ul, Script  # Importa los componentes necesarios
from frontend.components.forms import login_form, character_form  # Importa los formularios personalizados

def setup_routes(frontend_app):
    @frontend_app.route("/login")
    def index():
        return Titled("Character Management", Div(
            H1("Character Management"),
            AX("Load Characters", "/characters", "character-list"),
            Div(id="character-list")
        ))

    @frontend_app.route("/characters")
    async def show_characters():
        return Div(
            H2("Character List"),
            Ul(id="character-items"),
            Script("""
                document.addEventListener('DOMContentLoaded', () => {
                    fetch('/api/characters/getAll')
                        .then(response => response.json())
                        .then(data => {
                            const list = document.getElementById('character-items');
                            data.forEach(item => {
                                const li = document.createElement('li');
                                li.textContent = item['name'];
                                list.appendChild(li);
                            });
                        });
                });
            """, type="module")
        )
