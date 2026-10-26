from pathlib import Path
from PIL import Image, ImageOps

ENTRADA = Path("imagenes_originales")
SALIDA = Path("imagenes_optimizadas")

ANCHO = 750
ALTO = 500
CALIDAD = 80

COLOR_FONDO = (245, 245, 245)  # gris claro
FORMATOS_VALIDOS = {".jpg", ".jpeg", ".png", ".webp"}


def convertir_imagen(ruta_entrada: Path):
    SALIDA.mkdir(parents=True, exist_ok=True)

    ruta_salida = SALIDA / f"{ruta_entrada.stem}.webp"

    try:
        with Image.open(ruta_entrada) as img:
            img = ImageOps.exif_transpose(img)

            # Convertir a RGB
            if img.mode in ("RGBA", "LA"):
                fondo_transparencia = Image.new("RGB", img.size, COLOR_FONDO)
                fondo_transparencia.paste(img, mask=img.split()[-1])
                img = fondo_transparencia
            else:
                img = img.convert("RGB")

            # Redimensiona sin recortar
            img.thumbnail((ANCHO, ALTO), Image.Resampling.LANCZOS)

            # Crea lienzo fijo 800x600
            lienzo = Image.new("RGB", (ANCHO, ALTO), COLOR_FONDO)

            # Centra la imagen en el lienzo
            x = (ANCHO - img.width) // 2
            y = (ALTO - img.height) // 2

            lienzo.paste(img, (x, y))

            lienzo.save(
                ruta_salida,
                "WEBP",
                quality=CALIDAD,
                method=6,
            )

            print(f"OK: {ruta_entrada.name} -> {ruta_salida.name}")

    except Exception as e:
        print(f"ERROR: {ruta_entrada.name}: {e}")


def main():
    if not ENTRADA.exists():
        print(f"No existe la carpeta: {ENTRADA}")
        return

    imagenes = [
        archivo for archivo in ENTRADA.iterdir()
        if archivo.suffix.lower() in FORMATOS_VALIDOS
    ]

    if not imagenes:
        print("No se encontraron imágenes.")
        return

    for imagen in imagenes:
        convertir_imagen(imagen)

    print("Conversión terminada.")


if __name__ == "__main__":
    main()
