
1. Clona el repositorio:

```sh
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
```

2. Crea y activa un entorno virtual:

```sh
python -m venv env
source env/bin/activate   # En Linux/MacOS
env\Scripts\activate      # En Windows
```

3. Instala las dependencias:

```sh
pip install -r requirements.txt
```

4. Configura las variables de entorno en el archivo `.env`.

## Uso con Docker

1. Construye la imagen Docker:

```sh
docker build -t fastapi-mongo .
```

2. Inicia los contenedores con Docker Compose:

```sh
docker-compose up -d
```

## Ejecución de la Aplicación

1. Asegúrate de que MongoDB esté corriendo.
2. Ejecuta la aplicación:

```sh
uvicorn app.main:app --reload
```

La API estará disponible en `http://localhost:8000`.

## Endpoints

Algunos de los endpoints disponibles son:

- **`GET /items`**: Obtiene todos los ítems.
- **`POST /items`**: Crea un nuevo ítem.
- **`GET /items/{item_id}`**: Obtiene un ítem específico.
- **`PUT /items/{item_id}`**: Actualiza un ítem específico.
- **`DELETE /items/{item_id}`**: Elimina un ítem específico.

## Configuración

### Variables de Entorno

- **`MONGODB_URL`**: URL de conexión a la base de datos MongoDB.

### Configuración de Seguridad

La seguridad de la API puede configurarse utilizando JWT (JSON Web Tokens) u otros métodos de autenticación definidos en `core/security.py`.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.
