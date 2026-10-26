from pathlib import Path

carpeta = Path('imagenes_optimizadas')  # Cambia "uploads" por tu carpeta

for archivo in carpeta.iterdir():
    if archivo.is_file():
        nuevo_nombre = archivo.name.replace(" ", "_")
        nueva_ruta = archivo.with_name(nuevo_nombre)

        if archivo.name != nuevo_nombre:
            if not nueva_ruta.exists():
                archivo.rename(nueva_ruta)
                print(f"Renombrado: {archivo.name} -> {nuevo_nombre}")
            else:
                print(f"No se renombró porque ya existe: {nuevo_nombre}")
