# Task Management API

Una API REST funcional, segura y mantenible para gestión de tareas, construida con FastAPI, SQLAlchemy y PostgreSQL.

## Características

- **Autenticación JWT**: Login seguro con tokens JWT expirables.
- **CRUD completo de tareas**: Crear, leer, actualizar y eliminar tareas.
- **Paginación**: Listado de tareas con paginación configurable.
- **Manejo de errores**: Respuestas HTTP apropiadas (400, 401, 404, 422).
- **Base de datos PostgreSQL**: Configurada con Docker para entorno local.
- **Migraciones**: Usando Alembic para gestión de esquemas.
- **Hash seguro de contraseñas**: Usando Argon2.

## Stack Tecnológico

- Python 3.11.8
- FastAPI
- SQLAlchemy
- PostgreSQL
- Autenticación JWT (python-jose)
- Hash de contraseñas (passlib con Argon2)
- Alembic para migraciones
- Docker para base de datos local

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/miusarname2/prueba-tecnica-Logika.git
   cd prueba-tecnica-Logika
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configura las variables de entorno:
   Copia `.env.example` a `.env` y ajusta los valores si es necesario.

4. Inicia la base de datos PostgreSQL con Docker:
   ```bash
   docker-compose --env-file .env up -d
   ```

5. Ejecuta las migraciones para crear las tablas:
   ```bash
   alembic upgrade head
   ```

6. Crea el usuario inicial (opcional, para desarrollo):
   ```bash
   python -m app.database.seed
   ```

7. Ejecuta la aplicación:
   ```bash
   uvicorn main:app --reload
   ```

La API estará disponible en `http://localhost:8000`.

## Uso

### Autenticación

Para acceder a los endpoints protegidos, primero obtén un token JWT:

```bash
curl -X POST "http://localhost:8000/auth/login" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=admin@example.com&password=admin"
```

Respuesta:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

Usa el token en las cabeceras de las solicitudes:
```
Authorization: Bearer <access_token>
```

## Documentación de la API

Accede a `http://localhost:8000/docs` para la documentación interactiva generada por FastAPI.

### Endpoints

#### Tareas

- **GET /tasks**: Lista tareas con paginación.
  - Parámetros: `page` (int, default=0), `page_size` (int, default=10, max=100), `status` (opcional: pending, in_progress, done)
  
- **POST /tasks**: Crea una nueva tarea.
  - Body: `{"title": "string", "description": "string", "status": "pending"}`

- **GET /tasks/{task_id}**: Obtiene una tarea específica.

- **PUT /tasks/{task_id}**: Actualiza una tarea.
  - Body: campos a actualizar (title, description, status)

- **DELETE /tasks/{task_id}**: Elimina una tarea.

### Usuario Inicial

- **Email**: admin@example.com
- **Password**: admin

Este usuario se crea automáticamente al ejecutar el script de seed. En producción, crea usuarios a través de endpoints dedicados o migraciones.

## Justificación de Índices

- **User.email**: Índice único para búsquedas rápidas durante login y validaciones.
- **Task.status**: Índice para filtrar tareas por estado (e.g., listar solo pendientes).
- **Task.created_at**: Índice para ordenar tareas por fecha de creación.

Estos índices mejoran el rendimiento en consultas comunes sin sobrecargar la base de datos.

## Decisiones de Diseño

- **Identificación de usuario**: Se usa email como identificador único, común en aplicaciones web.
- **Formato del payload de login**: Se usa `username` y `password` en form-data, estándar para OAuth2.
- **Nombres de endpoints**: `/tasks` para CRUD, `/auth/login` para autenticación.
- **Paginación**: Parámetros `page` y `page_size` para control simple.
- **Hash de contraseñas**: Argon2 por ser más seguro que bcrypt en algunos contextos.
- **Expiración de token**: Configurable vía `JWT_EXPIRE_MINUTES` (default 30 minutos).
- **Manejo de errores**: Respuestas JSON con códigos HTTP estándar.


## Desarrollo

- Migraciones: Usa `alembic revision --autogenerate -m "message"` para nuevas migraciones.

## Producción

- Configura variables de entorno apropiadas.
- Usa un servidor ASGI como Gunicorn + Uvicorn.
- Implementa logging y monitoreo.
- Considera usar un proxy reverso como Nginx.