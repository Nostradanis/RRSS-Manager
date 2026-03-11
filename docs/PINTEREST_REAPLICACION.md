# Guía para reaplicar al acceso a la API de Pinterest

Pinterest ha rechazado tu solicitud de acceso a la API. Esta guía te ayuda a identificar posibles causas y a preparar una nueva solicitud con más probabilidades de aprobación.

## Motivos habituales de rechazo

Según la [comunidad de Pinterest](https://community.pinterest.biz/t/api-access-rejected/40878) y las [Developer Guidelines](https://policy.pinterest.com/en/developer-guidelines):

| Motivo | Cómo evitarlo |
|--------|----------------|
| **Descripción poco clara** | Explica en una sola frase qué hace la app |
| **Video sin flujo OAuth** | El video debe mostrar el proceso de autenticación completo |
| **Video sin integración Pinterest visible** | Muestra cómo se publica un pin real |
| **Parecer SaaS multi-usuario** | Deja claro que es **solo para tu propia cuenta** |
| **Automatización sin consentimiento** | Tu app cumple: el usuario elige cada pin manualmente |

## Tu app cumple las directrices

Tu aplicación **RRSS Manager / Fanpixers** encaja con los usos permitidos:

- ✅ **"Content marketing tools, like Pin schedulers"** — Es un programador/publicador de pins
- ✅ **"The end user must choose each Pin to be published"** — El usuario introduce tablero, texto, enlace e imagen en cada ejecución
- ✅ **Política de privacidad** — Disponible en URL con "fanpixers"

---

## Texto sugerido para la nueva solicitud

### Descripción de la app — versión corta (para copiar)

```
Herramienta de uso personal para publicar pins en mi cuenta de Pinterest. 
Elijo manualmente cada pin (tablero, título, descripción, enlace e imagen) antes de publicar. 
Solo para mi propia cuenta.
```

### Descripción de la app — versión detallada

```
Fanpixers es una herramienta de uso personal que permite publicar pins en mi cuenta de Pinterest. 
El usuario elige manualmente cada pin (tablero, título, descripción, enlace e imagen) antes de publicar. 
Solo uso la app para mi propia cuenta, no para terceros.
```

### Propósito del desarrollador

- Marca: **Uso personal** o **Herramienta interna**
- Evita términos como: "SaaS", "plataforma multi-usuario", "servicio para clientes"

---

## Requisitos del video demo

El video es **crítico**. Debe mostrar:

1. **Flujo OAuth** (si aplica): Cómo obtienes el token de acceso
2. **Ejecución del script**: `python publish_pinterest.py`
3. **Selección manual**: Elegir tablero, escribir título, descripción, enlace
4. **Imagen**: Indicar URL o ruta del archivo
5. **Publicación**: El pin aparece en tu tablero de Pinterest

**Duración sugerida:** 2-4 minutos  
**Formato:** MP4 o enlace a YouTube (no privado)

### Guion sugerido para el video

```
1. [0:00] "Esta es Fanpixers, una herramienta personal para publicar pins en Pinterest."
2. [0:10] "Ejecuto el script y me pide el tablero. Elijo uno de mi lista."
3. [0:25] "Introduzco el título, descripción y enlace manualmente."
4. [0:40] "Añado la imagen (URL o archivo local)."
5. [0:50] "Publico. El pin aparece en mi tablero de Pinterest."
6. [1:00] "Cada pin lo elijo yo. No hay automatización masiva."
```

---

## Checklist antes de enviar

- [ ] **Nombre de la app** incluye "Fanpixers" o es coherente con tu marca
- [ ] **URL de política de privacidad** contiene "fanpixers":  
  `https://nostradanis.github.io/RRSS-Manager/fanpixers-politica-privacidad.html`
- [ ] **Descripción** en una frase clara, mencionando "uso personal" y "solo mi cuenta"
- [ ] **Video** muestra: ejecución, entrada manual de datos, publicación real del pin
- [ ] **Sin términos prohibidos**: no uses "bulk", "automatización masiva", "multi-usuario"

---

## Si vuelven a rechazar

1. **Crear un ticket** en la categoría "Herramientas de desarrollador y API" (como indican en el email)
2. **Pedir motivos concretos**: "¿Podrían indicar qué aspecto de mi solicitud no cumple las directrices?"
3. **Publicar en la comunidad**: [Pinterest Business Community - Developers](https://community.pinterest.biz/c/developers/98) — a veces Pinterest responde por DM con un enlace para abrir ticket

---

## Enlaces útiles

- [Developer Guidelines](https://policy.pinterest.com/en/developer-guidelines)
- [Motivos de denegación (docs)](https://developers.pinterest.com/docs/getting-started/getting-access/)
- [Pinterest Business Community](https://community.pinterest.biz/c/developers/98)
- [Tu política de privacidad](https://nostradanis.github.io/RRSS-Manager/fanpixers-politica-privacidad.html)
- [Resumen de la app](https://nostradanis.github.io/RRSS-Manager/fanpixers-resumen-app.html)
