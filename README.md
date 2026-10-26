# 🖼️ Optimización de Imágenes

Conjunto de herramientas desarrolladas en **Python** para automatizar el procesamiento, optimización y renombrado de imágenes.

El proyecto está pensado para facilitar la preparación de múltiples imágenes antes de utilizarlas en páginas web, aplicaciones, catálogos o cualquier proyecto donde sea necesario mantener un formato y tamaño uniforme.

## 🚀 Funcionalidades

El proyecto contiene actualmente dos herramientas:

### 1. `Optimizacion.py`

Procesa automáticamente todas las imágenes almacenadas dentro de la carpeta:

```text
imagenes_originales/
```

Las imágenes resultantes se guardan en:

```text
imagenes_optimizadas/
```

El script realiza las siguientes operaciones:

- Detecta imágenes `.jpg`, `.jpeg`, `.png` y `.webp`.
- Corrige automáticamente la orientación utilizando la información EXIF.
- Convierte las imágenes al modo RGB.
- Gestiona imágenes PNG o similares que tengan transparencia.
- Añade un fondo gris claro cuando existe transparencia.
- Redimensiona las imágenes manteniendo su proporción original.
- Evita recortar o deformar la imagen.
- Centra cada imagen dentro de un lienzo de **750 × 500 píxeles**.
- Convierte el resultado al formato **WebP**.
- Utiliza una calidad de compresión del **80 %**.
- Crea automáticamente la carpeta de salida si no existe.
- Procesa varias imágenes de forma automática.

### 2. `Renombrar.py`

Esta herramienta procesa los archivos que se encuentran dentro de:

```text
imagenes_optimizadas/
```

Su función es normalizar los nombres de los archivos.

Por ejemplo:

```text
imagen producto principal.webp
```

se convierte automáticamente en:

```text
imagen_producto_principal.webp
```

El script:

- Reemplaza los espacios por `_`.
- Mantiene la extensión original del archivo.
- Comprueba si el nuevo nombre ya existe.
- Evita sobrescribir accidentalmente archivos existentes.
- Muestra en consola los archivos que han sido renombrados.

---

## 📁 Estructura del proyecto

```text
Optimizacion_imagenes/
│
├── Optimizacion.py
├── Renombrar.py
│
├── imagenes_originales/
│   ├── imagen1.jpg
│   ├── imagen2.png
│   └── imagen3.webp
│
└── imagenes_optimizadas/
    ├── imagen1.webp
    ├── imagen2.webp
    └── imagen3.webp
```

La carpeta `imagenes_optimizadas` puede generarse automáticamente al ejecutar el script de optimización.

---

## 🛠️ Requisitos

Es necesario tener instalado:

- Python 3
- Pillow

Puedes instalar Pillow mediante:

```bash
pip install Pillow
```

---

## ▶️ Uso

### 1. Añadir las imágenes

Coloca las imágenes que quieras procesar dentro de:

```text
imagenes_originales/
```

### 2. Optimizar las imágenes

Ejecuta:

```bash
python Optimizacion.py
```

El programa procesará todas las imágenes compatibles y guardará los resultados dentro de:

```text
imagenes_optimizadas/
```

Durante el proceso aparecerán mensajes como:

```text
OK: imagen.jpg -> imagen.webp
OK: fotografia.png -> fotografia.webp

Conversión terminada.
```

### 3. Normalizar los nombres

Después de optimizar las imágenes puedes ejecutar:

```bash
python Renombrar.py
```

Por ejemplo:

```text
Renombrado: foto producto.webp -> foto_producto.webp
```

---

## ⚙️ Configuración

Los principales parámetros pueden modificarse directamente en `Optimizacion.py`.

```python
ANCHO = 750
ALTO = 500
CALIDAD = 80
```

También puede modificarse el color utilizado como fondo:

```python
COLOR_FONDO = (245, 245, 245)
```

Por defecto se utiliza un gris claro.

Los formatos admitidos son:

```python
.jpg
.jpeg
.png
.webp
```

---

## 💡 Flujo de trabajo

El funcionamiento recomendado es:

```text
Imágenes originales
        ↓
Optimizacion.py
        ↓
Redimensionar + centrar + optimizar
        ↓
Conversión a WebP
        ↓
imagenes_optimizadas/
        ↓
Renombrar.py
        ↓
Nombres normalizados
```

---

## 🎯 Objetivo del proyecto

Esta herramienta busca automatizar tareas repetitivas relacionadas con la preparación de imágenes, permitiendo procesar múltiples archivos de forma rápida y manteniendo unas dimensiones y formato homogéneos.

Puede resultar útil para:

- Páginas web.
- E-commerce.
- Catálogos de productos.
- Aplicaciones móviles.
- Portafolios.
- Gestión de grandes cantidades de imágenes.
- Optimización de recursos web.

---

## 🔮 Posibles mejoras

Algunas funcionalidades que podrían añadirse en futuras versiones:

- Interfaz gráfica.
- Selección de carpetas mediante explorador.
- Drag & Drop.
- Procesamiento recursivo de subcarpetas.
- Configuración personalizada de resolución.
- Selección de calidad WebP.
- Comparación del tamaño original y optimizado.
- Estadísticas del espacio ahorrado.
- Renombrado automático durante la optimización.
- Generación de diferentes tamaños para diseño responsive.

---

## 👨‍💻 Autor

Desarrollado como una herramienta para automatizar la optimización y organización de imágenes mediante **Python**.
