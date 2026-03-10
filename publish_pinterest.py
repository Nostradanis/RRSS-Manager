#!/usr/bin/env python3
"""
RRSS Manager - Publicar pin en Pinterest
Solicita tablero, texto, enlace e imagen para publicar un pin.
"""

import base64
import os
import sys

import requests

# En Windows, intentar leer variables de entorno de usuario desde el registro
if sys.platform == "win32":
    try:
        import winreg
        def _get_user_env(name):
            try:
                key = winreg.OpenKey(
                    winreg.HKEY_CURRENT_USER,
                    r"Environment",
                    0,
                    winreg.KEY_READ
                )
                val, _ = winreg.QueryValueEx(key, name)
                winreg.CloseKey(key)
                return val
            except (FileNotFoundError, OSError):
                return None
    except ImportError:
        _get_user_env = lambda n: None
else:
    _get_user_env = lambda n: None

API_BASE = "https://api.pinterest.com/v5"


def get_pinterest_token():
    """Obtiene PINTEREST_TOKEN desde el entorno o variables de usuario de Windows."""
    token = os.environ.get("PINTEREST_TOKEN")
    if not token and sys.platform == "win32":
        token = _get_user_env("PINTEREST_TOKEN")
    return token


def get_headers():
    """Obtiene el token y devuelve los headers para la API."""
    token = get_pinterest_token()
    if not token:
        print("Error: Define la variable de entorno PINTEREST_TOKEN (cuenta de usuario en Windows).")
        sys.exit(1)
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }


def listar_tableros(headers):
    """Lista los tableros del usuario."""
    url = f"{API_BASE}/boards"
    params = {"page_size": 25}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Error al listar tableros: {response.status_code}")
        print(response.text)
        sys.exit(1)
    data = response.json()
    return data.get("items", [])


def crear_pin(headers, board_id, titulo, descripcion, enlace, imagen_url=None, imagen_base64=None):
    """Crea un pin en Pinterest."""
    url = f"{API_BASE}/pins"
    payload = {
        "board_id": board_id,
        "title": titulo[:100],  # Máximo 100 caracteres
        "description": descripcion[:800] if descripcion else "",  # Máximo 800
        "link": enlace,
    }
    if imagen_url:
        payload["media_source"] = {"source_type": "image_url", "url": imagen_url}
    elif imagen_base64:
        ct = imagen_base64.get("content_type", "image/jpeg")
        data = imagen_base64.get("data")
        payload["media_source"] = {"source_type": "image_base64", "content_type": ct, "data": data}
    else:
        print("Error: Se necesita una imagen (URL o archivo local).")
        sys.exit(1)

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code not in (200, 201):
        print(f"Error al crear el pin: {response.status_code}")
        print(response.text)
        sys.exit(1)
    return response.json()


def es_url(texto):
    """Comprueba si el texto es una URL."""
    return texto.strip().startswith(("http://", "https://"))


def main():
    print("=== RRSS Manager - Publicar en Pinterest ===\n")

    headers = get_headers()

    # 1. Listar tableros
    print("Cargando tus tableros...")
    tableros = listar_tableros(headers)
    if not tableros:
        print("No se encontraron tableros. Crea al menos uno en Pinterest.")
        sys.exit(1)

    print("\nTus tableros:")
    for i, t in enumerate(tableros, 1):
        nombre = t.get("name", "Sin nombre")
        board_id = t.get("id", "")
        print(f"  {i}. {nombre} (ID: {board_id})")

    # 2. Pedir tablero
    while True:
        try:
            opcion = input("\nNúmero del tablero donde publicar (1-{}): ".format(len(tableros)))
            idx = int(opcion)
            if 1 <= idx <= len(tableros):
                tablero = tableros[idx - 1]
                board_id = tablero["id"]
                break
        except ValueError:
            pass
        print("Introduce un número válido.")

    # 3. Pedir texto (título y descripción)
    titulo = input("\nTítulo del pin (máx. 100 caracteres): ").strip()
    if not titulo:
        print("El título es obligatorio.")
        sys.exit(1)
    descripcion = input("Descripción del pin (máx. 800 caracteres, opcional): ").strip()

    # 4. Pedir enlace
    enlace = input("\nEnlace del pin (URL): ").strip()
    if not enlace:
        print("El enlace es obligatorio.")
        sys.exit(1)
    if not es_url(enlace):
        enlace = "https://" + enlace

    # 5. Pedir imagen
    imagen_input = input("\nImagen: URL pública o ruta a archivo local: ").strip()
    if not imagen_input:
        print("La imagen es obligatoria.")
        sys.exit(1)

    imagen_url = None
    imagen_base64 = None

    if es_url(imagen_input):
        imagen_url = imagen_input
    elif os.path.isfile(imagen_input):
        ext = os.path.splitext(imagen_input)[1].lower()
        content_type = "image/jpeg" if ext in (".jpg", ".jpeg") else "image/png" if ext == ".png" else "image/jpeg"
        with open(imagen_input, "rb") as f:
            data_b64 = base64.b64encode(f.read()).decode("utf-8")
        imagen_base64 = {"content_type": content_type, "data": data_b64}
    else:
        print(f"Error: '{imagen_input}' no es una URL válida ni un archivo existente.")
        sys.exit(1)

    # 6. Publicar
    print("\nPublicando pin...")
    resultado = crear_pin(headers, board_id, titulo, descripcion, enlace, imagen_url, imagen_base64)

    pin_id = resultado.get("id", "")
    pin_url = resultado.get("link") or (f"https://www.pinterest.com/pin/{pin_id}/" if pin_id else "")
    print("\n¡Pin publicado correctamente!")
    if pin_url:
        print(f"URL: {pin_url}")
    elif pin_id:
        print(f"ID: {pin_id}")


if __name__ == "__main__":
    main()
