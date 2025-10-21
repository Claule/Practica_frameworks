from fastapi import FastAPI

# Crear la aplicación FastAPI
app = FastAPI(
    title="API de Tareas - Clase 2",
    description="API REST con operaciones CRUD creada en el curso Backend FUMC",
    version="1.0.0"
)

# Ruta raíz - Endpoint de bienvenida
@app.get("/")
async def root():
    return {
        "mensaje": "¡Bienvenido a la API de Tareas!",
        "version": "1.0.0",
        "endpoints": ["/docs", "/tareas"]
    }

# Endpoint de prueba con parámetro
@app.get("/saludar/{nombre}")
async def saludar(nombre: str):
    return {"mensaje": f"¡Hola, {nombre}! Esta API gestiona tareas."}