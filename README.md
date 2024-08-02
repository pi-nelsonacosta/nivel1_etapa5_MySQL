
# Objetivo general
Se requiere desarrollar una API que permita interactuar con datos de prueba y realizar peticiones GET, POST y DELETE.

## Características de los datos
Se brinda un ejemplo de la estructura de datos:

### Character
```json
{
    "id": 1,
    "name": "Luke Skywalker",
    "height": 172,
    "mass": 77,
    "hair_color": "blond",
    "skin_color": "fair",
    "eye_color": "blue",
    "birth_year": 1998
}

```
#### Pasos a seguir para ejecutar esta API


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

1. Asegúrate de que Docker este inicializado
2. Ejecuta la aplicación:

```sh
docker-compose down
docker-compose up --build
```

La API estará disponible en `http://localhost:8000`.

## Endpoints

Endpoints disponibles para Gestión de Usuario son:

- **`POST /user/register`**: Registrar un usuario.
- **`POST /user/token`**: Obtener un token de acceso.
- **`GET /user/me`**: Obtiene datos del usuario autenticado.

Endppints disponibles para Gestión de Characters (Personajes) son:

- **`GET /character/getAll`**: Lista de Personajes.
- **`GET /character/get/{id}`**: Listamos las caracteristicas de un personaje en particular.
- **`POST /character/add`**: Agregamos un character (personaje).
- **`DELETE /character/delete/{id}`**: Eliminamos un character (personaje).

Acceso a todos los endpoint (Listado)

- **`GET /docs/all-routes`**: Listado de Endpoints.

### Variables de Entorno

- **`MONGODB_URL`**: URL de conexión a la base de datos MongoDB.

### Enlace a Documentación del Proyecto (Enlace de Google Drive para descargar)

Link -- https://docs.google.com/document/d/1zMwE7s1ecL2JxNIkBabsIbCr3d-zWBfW/edit?usp=sharing&ouid=108611500655874932378&rtpof=true&sd=true

### Enlace a Testing con Postman (Enlae a Google Drive para descargar)

Link -- https://drive.google.com/file/d/1FqIX_DzNTfQBShO8MQzxJWlziEeCYTjo/view?usp=sharing


## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.
