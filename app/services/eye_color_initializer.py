# app/services/eye_color_initializer.py
from app.db import get_database
import random

async def initialize_eye_colors():
    db = get_database()
    eye_colors_collection = db.get_collection("eye_colors")
    
    # Verificamos si la colección ya tiene datos
    if await eye_colors_collection.count_documents({}) == 0:
        # Lista de colores de ojos posibles
        possible_colors = ["Blue", "Brown", "Green", "Hazel", "Amber", "Gray", "Violet", "Red"]
        
        # Seleccionar 8 colores aleatoriamente
        random_eye_colors = random.sample(possible_colors, 8)
        
        # Crear documentos para insertar
        eye_colors_to_insert = [{"color": color} for color in random_eye_colors]
        
        # Insertar en la colección
        await eye_colors_collection.insert_many(eye_colors_to_insert)
        print("EyeColors collection initialized with 8 random colors.")
