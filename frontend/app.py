# frontend/app.py

from fasthtml.common import fast_app, serve
from frontend.routes import views

# Inicializa la aplicación FastHTML y extrae solo la instancia de la aplicación
frontend_app, _ = fast_app()  # Extrae solo la instancia de FastHTML, ignorando el método route

# Depuración para ver qué devuelve fast_app()
print(f"Tipo de frontend_app después de la inicialización: {type(frontend_app)}, Valor: {frontend_app}")

# No es necesario verificar ya que sabemos que es correcto
# Configura las rutas
views.setup_routes(frontend_app)

if __name__ == "__main__":
    serve(frontend_app)
